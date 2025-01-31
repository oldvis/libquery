import json
from typing import Any, List


def load_jl(path: str) -> List[Any]:
    """Load a list from a JSONL file."""

    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def save_jl(data: List[Any], path: str) -> None:
    """Save a list as a JSONL file."""

    with open(path, "w", encoding="utf-8") as f:
        for d in data:
            f.write(f"{json.dumps(d, ensure_ascii=False)}\n")
