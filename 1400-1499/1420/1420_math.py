import sys


def main():
    ar, ai, br, bi = map(int, sys.stdin.read().split())
    norm = br * br + bi * bi
    if norm == 0:
        print(0)  # no remainder is shorter than zero
        return
    # a / b = (x + y i) / norm; every quotient q lies within 1 of it
    x, y = ar * br + ai * bi, ai * br - ar * bi
    fx, fy = x // norm, y // norm
    count = 0
    for qr in range(fx - 1, fx + 2):
        for qi in range(fy - 1, fy + 2):
            rr = ar - (br * qr - bi * qi)
            ri = ai - (br * qi + bi * qr)
            count += rr * rr + ri * ri < norm
    print(count)


main()
