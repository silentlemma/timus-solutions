import sys


def main():
    depth, position = map(int, sys.stdin.buffer.read().split())
    index = position - 1
    bits = index.bit_length()
    left_num, left_den = 0, 1
    right_num, right_den = 1, depth - 1 - bits
    # Leading zero bits move only the right denominator.
    for bit in range(bits - 1, -1, -1):
        if (index >> bit) & 1:
            left_num += right_num
            left_den += right_den
        else:
            right_num += left_num
            right_den += left_den
    print(left_num + right_num, left_den + right_den)


if __name__ == "__main__":
    main()
