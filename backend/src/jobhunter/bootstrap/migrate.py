"""Explicit offline schema upgrade; no listener and no data-directory creation."""

import argparse
import json
import os
from pathlib import Path

from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def main() -> None:
    os.umask(0o077)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-directory", type=Path, required=True)
    args = parser.parse_args()
    try:
        with Store.open(args.data_directory, migration=True) as store:
            outcome = store.migrate()
            print(
                json.dumps(
                    {
                        "outcome": outcome,
                        "data_directory": str(store.directory),
                        "schema_version": 2,
                    }
                ),
                flush=True,
            )
    except Failure as exc:
        print(json.dumps(exc.body()), flush=True)
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
