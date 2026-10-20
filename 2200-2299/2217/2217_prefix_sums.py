import sys

ZERO = ord("0")


def possible(n, s):
    if n % 2 == 0 and s.count(b"0") % 2 != 0:
        return False

    balance = 0
    for i in range(n // 2):
        # A zero can move left, so the suffix must supply at least as many zeros.
        balance += (s[n - 1 - i] == ZERO) - (s[i] == ZERO)
        if balance < 0:
            return False
    return True


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    print("YES" if possible(n, data[1]) else "NO")


if __name__ == "__main__":
    main()
