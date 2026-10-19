"""Checker: plays every game. The input lists the starting rows in plain
form (0 white, 1 black). Each game needs some queries and one claim with
positions in 1..n, at most 500000 lines in all. With 99 games at least 80
claims must be right; other tests (the example) only check the format."""

import sys

GAMES = 99
WINS = 80
LINES = 500000


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    games = int(words[0])
    rows = words[1:1 + games]
    lines = open(output).read().split("\n")
    lines = [line for line in lines if line.strip()]
    if len(lines) > LINES:
        raise Bad("more than %d lines" % LINES)
    at, wins = 0, 0
    for game in range(games):
        n = game + 2
        row = [int(c) for c in rows[game]] if game < len(rows) and len(rows[game]) == n else None
        while True:
            if at == len(lines):
                raise Bad("game %d has no claim" % (game + 1))
            parts = lines[at].split()
            at += 1
            if len(parts) != 3 or parts[0] not in ("?", "!") or not parts[1].isdigit() or not parts[2].isdigit():
                raise Bad("bad line %r" % lines[at - 1])
            v, u = int(parts[1]), int(parts[2])
            if not (1 <= v <= n and 1 <= u <= n and v != u):
                raise Bad("bad positions in game %d" % (game + 1))
            if parts[0] == "!":
                if row is not None and row[v - 1] == row[u - 1]:
                    wins += 1
                break
            if row is not None and row[v - 1] == 1 and row[u - 1] == 0:
                row[v - 1], row[u - 1] = 0, 1
    if at != len(lines):
        raise Bad("extra lines after the last game")
    if games == GAMES and wins < WINS:
        raise Bad("only %d games won" % wins)


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
