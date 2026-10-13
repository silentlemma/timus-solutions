TOP = 30


def main():
    n = int(input())
    count = [0] * (TOP + 2)
    for c in map(int, input().split()):
        count[c] += 1
    # two types share a symmetric alternating row only as ABA...BA, counts differing by one,
    # along the chain of counts, pairing the leftovers of c with c + 1 at once is best
    pairs = 0
    left = 0
    for c in range(1, TOP + 1):
        here = count[c]
        matched = min(left, here)
        pairs += matched
        left = here - matched
    print(n - pairs)


main()
