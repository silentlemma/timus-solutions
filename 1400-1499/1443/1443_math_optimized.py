TICKS_PER_METER = 10_000


def main():
    with open(0, "rb") as source:
        lines, length, rail = source.read().split()
    lines = int(lines)
    # Rounding recovers the exact number of ticks from the four decimal places.
    length, rail = (round(float(value) * TICKS_PER_METER) for value in (length, rail))
    whole, remainder = divmod(length, rail)
    total = lines * whole
    if remainder:
        total += 1 + (lines - 1) // (rail // remainder)
    print(total)


if __name__ == "__main__":
    main()
