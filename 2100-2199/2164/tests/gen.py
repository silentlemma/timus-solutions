import argparse
import random

ROWS = 7
COLUMNS = 9
MAX_LENGTH = 10_000
MOVE_LIMIT = ROWS * COLUMNS
SHORT_LIMIT = 2 * MOVE_LIMIT
BIAS_FACTOR = 4
DIGITS = "123456789"
DRAW_ROW = "132457689"
VERTICAL_WIN = "1212121"
DIAGONAL_WIN = "1223533464484"
MODE_NAMES = (
    "small",
    "random",
    "single",
    "two",
    "periodic",
    "draw",
    "biased",
    "bursts",
    "boundary",
    "mixed",
)


def repeat_to_length(text, length):
    return (text * ((length + len(text) - 1) // len(text)))[:length]


def generate(mode, rng):
    if mode == "small":
        length = rng.randint(1, SHORT_LIMIT)
        return "".join(rng.choices(DIGITS, k=length))
    if mode == "random":
        return "".join(rng.choices(DIGITS, k=MAX_LENGTH))
    if mode == "single":
        return rng.choice(DIGITS) * MAX_LENGTH
    if mode == "two":
        columns = rng.sample(DIGITS, 2)
        return "".join(rng.choices(columns, k=MAX_LENGTH))
    if mode == "periodic":
        length = rng.randint(1, MOVE_LIMIT)
        period = "".join(rng.choices(DIGITS, k=length))
        return repeat_to_length(period, MAX_LENGTH)
    if mode == "draw":
        row = DRAW_ROW
        if rng.randrange(2):
            row = "".join(str(COLUMNS + 1 - int(digit)) for digit in row)
        return repeat_to_length(row, MAX_LENGTH)
    if mode == "biased":
        column = rng.choice(DIGITS)
        return "".join(
            rng.choice(DIGITS) if rng.randrange(BIAS_FACTOR) == 0 else column
            for _ in range(MAX_LENGTH)
        )
    if mode == "bursts":
        parts = []
        length = 0
        while length < MAX_LENGTH:
            part = rng.choice(DIGITS) * rng.randint(1, SHORT_LIMIT)
            parts.append(part)
            length += len(part)
        return "".join(parts)[:MAX_LENGTH]
    if mode == "boundary":
        length = rng.choice((MOVE_LIMIT - 1, MOVE_LIMIT, MOVE_LIMIT + 1))
        return "".join(rng.choices(DIGITS, k=length))
    motifs = (DRAW_ROW * ROWS, VERTICAL_WIN, DIAGONAL_WIN, DIGITS[0] * MOVE_LIMIT)
    parts = []
    length = 0
    while length < MAX_LENGTH:
        part = rng.choice(motifs)
        parts.append(part)
        length += len(part)
    return "".join(parts)[:MAX_LENGTH]


def main():
    aliases = {str(index): mode for index, mode in enumerate(MODE_NAMES, 1)}
    names = ", ".join(f"{number}={name}" for number, name in aliases.items())
    parser = argparse.ArgumentParser(
        description="generate one valid move log; mode aliases: " + names
    )
    parser.add_argument("mode", choices=tuple(aliases) + MODE_NAMES)
    parser.add_argument("seed", type=int, help="seed for deterministic randomness")
    arguments = parser.parse_args()
    mode = aliases.get(arguments.mode, arguments.mode)
    print(generate(mode, random.Random(arguments.seed)))


if __name__ == "__main__":
    main()
