DISCRIMINANT_SHIFT = 3


def integer_root(value):
    # Start at a power of two above the root, then improve by integer Newton steps.
    root = 1 << ((value.bit_length() + 1) // 2)
    while True:
        next_root = (root + value // root) // 2
        if next_root >= root:
            return root
        root = next_root


def main():
    # 8 S + 1 is the exact square of 2 N + 1.
    total = int(input())
    print((integer_root((total << DISCRIMINANT_SHIFT) + 1) - 1) // 2)


main()
