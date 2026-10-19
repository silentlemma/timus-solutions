"""Accept any model undominated in record count and minimum observed price."""

from pathlib import Path
import sys

RECORDS = 6
FIELDS = 3


def optimal_models(records):
    models = {model for _, model, _ in records}
    answer = set()
    for model in models:
        prices = [price for _, candidate, price in records if candidate == model]
        beaten = False
        for competitor in models:
            other = [price for _, candidate, price in records if candidate == competitor]
            if len(other) > len(prices) or len(other) == len(prices) and min(other) < min(prices):
                beaten = True
        if not beaten:
            answer.add(model)
    return answer


def validate(records, raw):
    try:
        words = raw.decode("ascii").split()
    except UnicodeDecodeError:
        return False
    return len(words) == 1 and words[0] in optimal_models(records)


def main():
    tokens = Path(sys.argv[1]).read_text(encoding="ascii").split()
    records = [
        (tokens[i], tokens[i + 1], int(tokens[i + 2])) for i in range(0, RECORDS * FIELDS, FIELDS)
    ]
    if not validate(records, Path(sys.argv[3]).read_bytes()):
        print("The output is not one optimal model name")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
