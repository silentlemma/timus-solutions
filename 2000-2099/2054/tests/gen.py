"""Deterministic seed/mode generator: year, zenith, night, grazing; n=8760."""

from datetime import date, timedelta
import random
import sys

YEAR_HOURS = 8760
HOURS_PER_DAY = 24
MONTHS = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")


def generate(seed, mode):
    randomizer = random.Random(seed)
    if mode == "year":
        latitudes = ("56.00", "0.00", "-66.57", "89.99", "-89.99", "23.44", "23.43", "-23.44")
        latitude = latitudes[seed % len(latitudes)]
        indices = list(range(YEAR_HOURS))
        randomizer.shuffle(indices)
        rows = []
        for index in indices:
            value = date(2001, 1, 1) + timedelta(days=index // HOURS_PER_DAY)
            rows.append(f"{value.day} {MONTHS[value.month - 1]} {index % HOURS_PER_DAY}")
    else:
        latitude, row = {
            "zenith": ("23.44", "21 jun 12"),
            "night": ("89.99", "21 dec 0"),
            "grazing": ("-66.56", "21 jun 12"),
        }[mode]
        rows = [row] * YEAR_HOURS
    return f"{latitude} {len(rows)}\n" + "\n".join(rows) + "\n"


if __name__ == "__main__":
    sys.stdout.write(generate(int(sys.argv[1]), sys.argv[2]))
