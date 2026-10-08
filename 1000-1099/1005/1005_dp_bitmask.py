import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    w = data[1 : 1 + data[0]]
    total = sum(w)
    # bit s of reach is set when some stones weigh exactly s
    reach = 1
    for x in w:
        reach |= reach << x
    half = total // 2
    lighter = (reach & ((1 << (half + 1)) - 1)).bit_length() - 1
    print(total - 2 * lighter)


main()
