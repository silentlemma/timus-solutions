import sys
from array import array

# chunks bound token storage even when all input is on one line.
# every input integer has at most ten digits; only an unfinished token is kept.
INPUT_BUFFER = 8192


def numbers():
    tail = b""
    while chunk := sys.stdin.buffer.read(INPUT_BUFFER):
        parts = (tail + chunk).split()
        tail = parts.pop() if chunk[-1:] > b" " else b""
        yield from map(int, parts)
    if tail:
        yield int(tail)


def main():
    nums = numbers()
    n, m = next(nums), next(nums)
    # each subject is at most 1000, so an unsigned short holds it exactly.
    rules = array("H", (next(nums) for _ in range(2 * m)))
    place = [0] * (n + 1)
    for i in range(n):
        place[next(nums)] = i
    # the plan is right exactly when every rule points forward in it; a
    # rule from a subject to itself can never hold
    print("YES" if all(place[rules[i]] < place[rules[i + 1]] for i in range(0, 2 * m, 2)) else "NO")


main()
