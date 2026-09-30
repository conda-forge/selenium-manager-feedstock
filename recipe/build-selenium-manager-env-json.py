import sys
import os
from pathlib import Path
import json

IS_WIN = os.name == "nt"

PREFIX = Path(os.environ["PREFIX"])
ENV_D_JSON_PATH = PREFIX / "etc/conda/env_vars.d/selenium-manager.json"
EXE = (
    "Scripts/selenium-manager.exe" if IS_WIN else "bin/selenium-manager"
)

ENV_JSON_CONTENT = {"SE_MANAGER_PATH": (PREFIX / EXE).as_posix()}

def main() -> int:
    ENV_D_JSON_PATH.parent.mkdir(parents=True)
    ENV_D_JSON_PATH.write_text(
        json.dumps(ENV_JSON_CONTENT), encoding="utf-8", newline="\n"
    )
    print(f"... wrote {ENV_D_JSON_PATH}")
    print(ENV_D_JSON_PATH.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
