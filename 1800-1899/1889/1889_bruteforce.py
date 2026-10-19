import sys

UNKNOWN = "unknown"


def fits(phrases, size):
    # every block of size phrases is one language, and no language is used
    # in two blocks
    used = set()
    for start in range(0, len(phrases), size):
        known = {p for p in phrases[start:start + size] if p != UNKNOWN}
        if len(known) > 1 or known & used:
            return False
        used |= known
    return True


def main():
    words = sys.stdin.read().split()
    n, phrases = int(words[0]), words[1:]
    counts = [k for k in range(1, n + 1) if n % k == 0 and fits(phrases, n // k)]
    print(" ".join(map(str, counts)) if counts else "Igor is wrong.")


main()
