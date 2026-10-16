import sys

# the line has at most 10^5 pieces of each length, fewer than the 9 * 10^5
# numbers of six digits, so the answer has at most six digits
DIGITS = 6


def main():
    s = sys.stdin.readline().strip()
    starts = [i for i in range(len(s)) if s[i] != "0"]
    seen = set()
    for length in range(1, DIGITS + 1):
        seen.update(s[i:i + length] for i in starts if i + length <= len(s))
    answer = 1
    while str(answer) in seen:
        answer += 1
    print(answer)


main()
