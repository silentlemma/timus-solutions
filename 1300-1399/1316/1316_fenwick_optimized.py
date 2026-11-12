import sys

CENTS = 100
MAX_PRICE = 10000 * CENTS


def main():
    # Stream the log directly; a million list slots cost less than keeping all parsed operations.
    tree = [0] * (MAX_PRICE + 1)
    revenue = 0
    for line in sys.stdin.buffer:
        words = line.split()
        kind = words[0]
        if kind == b"QUIT":
            break
        whole, _, fraction = words[1].partition(b".")
        price = int(whole or b"0") * CENTS + int(fraction.ljust(2, b"0"))
        index = MAX_PRICE - price + 1
        if kind == b"SALE":
            eligible = 0
            while index:
                eligible += tree[index]
                index &= index - 1
            amount = int(words[2])
            revenue += amount if amount < eligible else eligible
        else:
            delta = 1 if kind == b"BID" else -1
            while index <= MAX_PRICE:
                tree[index] += delta
                index += index & -index
    print(f"{revenue // CENTS}.{revenue % CENTS:02d}")


main()
