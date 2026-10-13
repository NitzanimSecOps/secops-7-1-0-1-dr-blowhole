#!/usr/bin/env python3
"""Self-check for solve.sh. Run:  python3 selftest.py"""
import subprocess
import sys
import tempfile
from pathlib import Path

SOLVE = Path(__file__).resolve().parent / "solve.sh"
SIZE = 10_000_000


def main():
    with tempfile.TemporaryDirectory() as wd:
        target = Path(wd) / "access.log"
        target.write_bytes(b"A" * SIZE)
        subprocess.run(["bash", str(SOLVE), str(target)], timeout=60)
        data = target.read_bytes()
        ok1 = set(data) == {0}
        ok2 = target.stat().st_size == SIZE
    print(("PASS" if ok1 else "FAIL"), "all bytes zeroed (0x00)")
    print(("PASS" if ok2 else "FAIL"), "size preserved")
    print(f"\n{ok1 + ok2}/2 checks passed.")
    return 0 if ok1 and ok2 else 1


if __name__ == "__main__":
    sys.exit(main())
