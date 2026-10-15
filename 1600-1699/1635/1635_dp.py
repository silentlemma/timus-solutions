import sys


def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    letter = {}  # bit j set where s[j] is the letter
    for j, c in enumerate(s):
        letter[c] = letter.get(c, 0) | 1 << j
    # starts: bit j set when s[j..i] is a palindrome; level[v]: bit j set when
    # the prefix of length j splits into v palindromes at best
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)
    level = [1]  # the empty prefix needs 0
    starts = 0
    for i, c in enumerate(s):
        starts = (starts >> 1) & letter[c] | 1 << i
        if i and s[i - 1] == c:
            starts |= 1 << (i - 1)
        # dp[i + 1] is dp[i] - 1, dp[i] or dp[i] + 1
        best = dp[i] + 1
        prev[i + 1] = i
        for v in (dp[i] - 2, dp[i] - 1):
            if v >= 0 and level[v] & starts:
                hit = level[v] & starts
                best, prev[i + 1] = v + 1, (hit & -hit).bit_length() - 1
                break
        dp[i + 1] = best
        while len(level) <= best:
            level.append(0)
        level[best] |= 1 << (i + 1)
    parts = []
    end = n
    while end:
        parts.append(s[prev[end] : end])
        end = prev[end]
    print(dp[n])
    print(" ".join(reversed(parts)))


main()
