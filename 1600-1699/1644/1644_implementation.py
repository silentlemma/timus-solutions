KNOWN_HUNGRY, KNOWN_FULL = 2, 10  # given in the statement


def main():
    data = open(0).read().split()
    hungry, full = KNOWN_HUNGRY, KNOWN_FULL
    for count, verdict in zip(data[1::2], data[2::2]):
        if verdict == "hungry":
            hungry = max(hungry, int(count))
        else:
            full = min(full, int(count))
    # the smallest satisfying amount must exceed the largest hungry one
    print(full if full > hungry else "Inconsistent")


main()
