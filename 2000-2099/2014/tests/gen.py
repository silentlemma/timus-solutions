"""Usage: seed mode. Modes: negative, negative_reverse, negative_shuffled,
positive_reverse, alternating, alternating_reverse, early_income_late_notice,
late_income, random. All use 100000 distinct valid nonleap-year minutes.
"""

from datetime import datetime, timedelta
import random
import sys

COUNT = 100000
MAX_AMOUNT = 50000
YEAR_MINUTES = 365 * 24 * 60


def generate(seed, mode):
    rng = random.Random(seed)
    keys = list(range(COUNT))
    if mode in ("negative_reverse", "positive_reverse", "alternating_reverse"):
        keys.reverse()
    elif mode == "negative_shuffled":
        rng.shuffle(keys)
    elif mode == "early_income_late_notice":
        keys = list(range(COUNT // 2, COUNT)) + list(range(COUNT // 2))
    elif mode == "random":
        keys = rng.sample(range(YEAR_MINUTES), COUNT)
    if mode.startswith("negative"):
        amounts = [-MAX_AMOUNT] * COUNT
    elif mode == "positive_reverse":
        amounts = [MAX_AMOUNT] * COUNT
    elif mode in ("alternating", "alternating_reverse"):
        amounts = [-MAX_AMOUNT if key % 2 == 0 else MAX_AMOUNT for key in keys]
    elif mode in ("early_income_late_notice", "late_income"):
        amounts = [-MAX_AMOUNT] * (COUNT // 2) + [MAX_AMOUNT] * (COUNT // 2)
    elif mode == "random":
        amounts = [rng.choice((-1, 1)) * rng.randint(1, MAX_AMOUNT) for _ in keys]
    else:
        raise ValueError("unknown mode")
    first = datetime(2025, 1, 1)
    lines = [str(COUNT)]
    for key, amount in zip(keys, amounts):
        date = first + timedelta(minutes=key)
        lines.append(f"{amount:+d} {date:%d.%m %H:%M}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
