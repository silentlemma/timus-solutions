import sys


def solve(south, north):
    i = j = elapsed = 0
    while i < len(south) and j < len(north):
        a, b = south[i], north[j]
        go_a = a != "L" or b == "L"
        go_b = b != "L" or a == "L"
        i += go_a
        j += go_b
        elapsed += 1
    return elapsed + len(south) - i + len(north) - j


if __name__ == "__main__":
    print(solve(*sys.stdin.read().split()))
