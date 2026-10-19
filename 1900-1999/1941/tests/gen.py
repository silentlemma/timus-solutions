"""Deterministic maximal tests, with closed-form window counts."""

import argparse
import sys

MAX_PATTERN = 8000
MAX_TEXT = 500000
ALPHABET = 729000


def token(code):
    return bytes((33 + code // 8100, 33 + code // 90 % 90, 33 + code % 90))


def generate(mode):
    size = 1 if mode == "single" else MAX_PATTERN
    if mode in ("single", "constant", "blocked", "outsiders"):
        pattern = [b"!!!"] * size
    elif mode == "churn":
        pattern = [b"!!!"] * (size // 2) + [b"zzz"] * (size // 2)
    elif mode == "unique_tail":
        pattern = [token(ALPHABET - size + index) for index in range(size)]
    else:
        pattern = [token(index) for index in range(size)]
    if mode in ("single", "constant"):
        text = [b"!!!"] * MAX_TEXT
    elif mode == "blocked":
        text = [
            b"zzz" if index % size == size - 1 else b"!!!" for index in range(MAX_TEXT)
        ]
    elif mode == "outsiders":
        text = [b"zzz"] * MAX_TEXT
    elif mode == "churn":
        text = [b"!!!" if index % 2 == 0 else b"zzz" for index in range(MAX_TEXT)]
    elif mode == "unique_head":
        text = [token(index) for index in range(MAX_TEXT)]
    elif mode == "unique_tail":
        text = [token(ALPHABET - MAX_TEXT + index) for index in range(MAX_TEXT)]
    else:
        text = [pattern[index % size] for index in range(MAX_TEXT)]
    return b" ".join(pattern) + b"\n" + b" ".join(text) + b"\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode",
        choices=[
            "single",
            "constant",
            "period",
            "blocked",
            "outsiders",
            "churn",
            "unique_head",
            "unique_tail",
        ],
    )
    sys.stdout.buffer.write(generate(parser.parse_args().mode))
