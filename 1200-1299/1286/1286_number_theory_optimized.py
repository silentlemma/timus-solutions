from math import gcd


def main():
    with open(0, "rb") as source:
        p, q, x, y, x1, y1 = map(int, source.read().split())
    dx, dy = x1 - x, y1 - y
    step = gcd(p, q)
    if step:
        parity_step = step if (p + q) % (2 * step) else 2 * step
        allowed = dx % step == 0 and dy % step == 0 and (dx + dy) % parity_step == 0
    else:
        allowed = dx == dy == 0
    print("YES" if allowed else "NO")


if __name__ == "__main__":
    main()
