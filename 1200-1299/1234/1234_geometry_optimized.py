TENTHS = 10


def tenths(token):
    whole, _, fraction = token.partition(b".")
    return int(whole) * TENTHS + int(fraction or b"0")


def fits(q, p, b, a):
    if q > b:
        return False
    if p <= a:
        return True
    total, difference = (p + q) ** 2, (p - q) ** 2
    return (a + b) ** 2 * difference + (a - b) ** 2 * total >= 2 * total * difference


def main():
    with open(0, "rb") as stream:
        x, y, z, a, b = map(tenths, stream.read().split())
    q, p, _ = sorted((x, y, z))
    b, a = sorted((a, b))
    print("YES" if fits(q, p, b, a) else "NO")


if __name__ == "__main__":
    main()
