LOG_NUMERATOR = 301_029_995_663
SCALE = 1_000_000_000_000


def main():
    with open(0, "rb") as stream:
        n = int(stream.read())
    # Both parities use the greatest even exponent no larger than n.
    print((n & ~1) * LOG_NUMERATOR // SCALE)


if __name__ == "__main__":
    main()
