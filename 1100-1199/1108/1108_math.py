import sys


def main():
    n = int(sys.stdin.read())
    # the last denominators reach about 27 000 digits, past the default limit
    # on converting integers to text
    sys.set_int_max_str_digits(0)
    out = []
    a = 2
    for _ in range(n):
        out.append(str(a))
        # after the shares 1/a(1) .. 1/a(k) the remainder is 1/(a(k+1) - 1), and the
        # largest share that still leaves something is 1/a(k+1)
        a = a * (a - 1) + 1
    print("\n".join(out))


main()
