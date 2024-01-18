from pathlib import Path
import sys


def register() -> None:
    sys.path.insert(0, Path(".").parent.as_posix())
    return None


register()
