from pathlib import Path
from typing import Iterable


def find_examp(*paths: str | Path, skip: bool = False) -> Iterable[tuple[str, str]]:
    if skip:
        raise StopIteration

    for s in paths:
        path = Path(s)
        if path.is_file() and path.suffix == ".json":
            yield (path.name, path.read_text())
        elif path.is_dir():
            for f in path.iterdir():
                yield from find_examp(f, skip=skip)
