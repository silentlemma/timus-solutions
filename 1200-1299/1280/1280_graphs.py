import sys


def main():
    nums = map(int, sys.stdin.buffer.read().split())
    n, m = next(nums), next(nums)
    rules = [(next(nums), next(nums)) for _ in range(m)]
    place = [0] * (n + 1)
    for i in range(n):
        place[next(nums)] = i
    # the plan is right exactly when every rule points forward in it; a
    # rule from a subject to itself can never hold
    print("YES" if all(place[s] < place[u] for s, u in rules) else "NO")


main()
