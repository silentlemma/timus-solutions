import sys


def z_function(s):
    n = len(s)
    z = [0] * n
    left = right = 0
    for i in range(1, n):
        k = 0
        if i < right:
            k = min(z[i - left], right - i)
        while i + k < n and s[k] == s[i + k]:
            k += 1
        z[i] = k
        if i + k > right:
            left, right = i, i + k
    return z


def main():
    word, last = sys.stdin.read().split()[:2]
    m, n = len(word), len(last)
    z = z_function(word + "#" + last)
    # from a cut at position p the next piece can end anywhere in
    # p + 1 .. p + z[p]; so the reachable cuts are always 0 .. reach
    parent = [0] * (n + 1)
    reach = 0
    p = 0
    while p <= reach and p < n:
        far = p + z[m + 1 + p]
        for q in range(reach + 1, far + 1):
            parent[q] = p
        reach = max(reach, far)
        p += 1
    if reach < n:
        print("Yes")
        return
    pieces = []
    q = n
    while q > 0:
        pieces.append(last[parent[q]:q])
        q = parent[q]
    print("No")
    print(" ".join(reversed(pieces)))


main()
