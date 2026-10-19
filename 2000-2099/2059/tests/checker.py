"""Stream Case #i rows and compare exact integer counts without loading large outputs."""

from pathlib import Path
import sys

MAX_WORD_LENGTH = 200000
MAX_INPUT_BYTES = 8 * 1024 * 1024
VALUES_PER_ROW = 3
TOKENS_PER_ROW = VALUES_PER_ROW + 2


def row(line, index, limit):
    fields = line.split()
    if len(fields) != TOKENS_PER_ROW or fields[:2] != [b"Case", f"#{index}:".encode()]:
        raise ValueError("invalid Case row or number")
    values = tuple(map(int, fields[2:]))
    if any(value < 0 for value in values) or sum(values) > limit:
        raise ValueError("counts outside palindrome-union bound")
    return values


def check(input_path, expected_path, actual_path):
    try:
        if input_path.stat().st_size > MAX_INPUT_BYTES:
            return False, "input exceeds total size bound"
        with input_path.open("rb") as inp, expected_path.open("rb") as expected:
            with actual_path.open("rb") as actual:
                total = int(inp.readline())
                if total < 0:
                    return False, "negative test count"
                for index in range(1, total + 1):
                    a = inp.readline().rstrip(b"\r\n")
                    b = inp.readline().rstrip(b"\r\n")
                    if not (0 < len(a) <= MAX_WORD_LENGTH and 0 < len(b) <= MAX_WORD_LENGTH):
                        return False, "invalid input word length"
                    limit = len(a) + len(b)
                    wanted = row(expected.readline(), index, limit)
                    observed = row(actual.readline(), index, limit)
                    if observed != wanted:
                        return False, f"wrong counts at case {index}"
                if any(line.strip() for line in actual):
                    return False, "extra output"
                if any(line.strip() for line in expected):
                    return False, "extra expected rows"
                if inp.read().strip():
                    return False, "extra input"
        return True, ""
    except (OSError, ValueError, OverflowError) as error:
        return False, str(error)


def main():
    passed, detail = check(*(Path(value) for value in sys.argv[1:]))
    if detail:
        print(detail)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
