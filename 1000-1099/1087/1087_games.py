import sys


def main():
    tok = list(map(int, sys.stdin.read().split()))
    n, m = tok[0], tok[1]
    moves = sorted(set(tok[2 : 2 + m]))
    # win[x]: the player to move with x stones left wins; with none left the
    # other player has just taken the last stone and lost
    win = [True] + [False] * n
    for x in range(1, n + 1):
        win[x] = any(not win[x - k] for k in moves if k <= x)
    print(1 if win[n] else 2)


main()
