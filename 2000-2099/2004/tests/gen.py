"""Usage: gen.py SEED MODE; MODE is an order from 16 through 20."""

import sys

MIN_GENERATED_ORDER = 16
MAX_ORDER = 20

if __name__ == "__main__":
    order = int(sys.argv[2])
    if not MIN_GENERATED_ORDER <= order <= MAX_ORDER:
        raise ValueError("order outside generated modes")
    print(order)
