"""Supported launcher: acquire storage before opening a loopback listener."""

import ipaddress
import json
import logging
import os
from pathlib import Path

import uvicorn

from jobhunter.bootstrap.container import create_app
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def main() -> None:
    os.umask(0o077)
    # Third-party parser/framework logs must never emit rejected payloads or SQL.
    for name in ("urlstd", "sqlalchemy", "uvicorn.error", "uvicorn.access"):
        logger = logging.getLogger(name)
        logger.handlers = [logging.NullHandler()]
        logger.propagate = False
        logger.disabled = True
    try:
        host = os.environ.get("JOBHUNTER_BIND", "127.0.0.1")
        if host not in ("127.0.0.1", "::1") or not ipaddress.ip_address(host).is_loopback:
            raise Failure("ACCESS_DENIED")
        port = int(os.environ.get("JOBHUNTER_PORT", "8765"))
        if not 1 <= port <= 65535:
            raise Failure("BAD_REQUEST")
        authority = f"[{host}]:{port}" if ":" in host else f"{host}:{port}"
        hosts = tuple(os.environ.get("JOBHUNTER_ALLOWED_HOSTS", authority).split(","))
        origins = tuple(filter(None, os.environ.get("JOBHUNTER_ALLOWED_ORIGINS", "").split(",")))
        for allowed in hosts:
            hostname = allowed.rsplit(":", 1)[0].strip("[]")
            if hostname not in ("127.0.0.1", "::1", "localhost") or allowed.rsplit(":", 1)[
                -1
            ] != str(port):
                raise Failure("ACCESS_DENIED")
        for origin in origins:
            from urllib.parse import urlsplit

            parsed = urlsplit(origin)
            if (
                parsed.scheme not in ("http", "https")
                or parsed.hostname not in ("127.0.0.1", "::1", "localhost")
                or parsed.username is not None
                or parsed.password is not None
                or parsed.path
                or parsed.query
                or parsed.fragment
                or "*" in origin
            ):
                raise Failure("ACCESS_DENIED")
            _ = parsed.port
        configured = os.environ.get("JOBHUNTER_DATA_DIRECTORY")
        with Store.open(Path(configured) if configured is not None else None) as store:
            print(
                json.dumps(
                    {
                        "outcome": store.outcome,
                        "data_directory": str(store.directory),
                        "schema_version": 1,
                    }
                ),
                flush=True,
            )
            uvicorn.run(
                create_app(store, hosts=hosts, origins=origins),
                host=host,
                port=port,
                access_log=False,
                log_config=None,
                proxy_headers=False,
            )
    except Failure as exc:
        print(json.dumps(exc.body()), flush=True)
        raise SystemExit(1) from None
    except (ValueError, OSError):
        print(json.dumps(Failure("BAD_REQUEST").body()), flush=True)
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
