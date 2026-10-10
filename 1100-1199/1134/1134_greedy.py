import sys


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    count = [0] * (n + 1)
    for x in data[2 : 2 + m]:
        count[int(x)] += 1
    # card k shows k - 1 and k, so the number x fits cards x and x + 1; going
    # up from the smallest number, card x is useless to anything later, so it
    # is taken first
    used = [False] * (n + 2)
    for x in range(n + 1):
        for card in (x, x + 1):
            if count[x] > 0 and 1 <= card <= n and not used[card]:
                used[card] = True
                count[x] -= 1
        if count[x]:
            print("NO")
            return
    print("YES")


main()
