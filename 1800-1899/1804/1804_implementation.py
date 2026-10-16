import sys

MOST = 30


def main():
    lines = sys.stdin.read().split("\n")
    t = int(lines[0])
    out = []
    for line in lines[1:1 + t]:
        x, y = [int(w) for w in line.split() if w.isdigit()]
        first_home = " home " in line
        lowest, highest = None, None
        for g in range(MOST + 1):
            can_pass = can_fail = False
            for o in range(MOST + 1):
                ours, theirs = x + g, y + o
                # goals scored at the other team's stadium
                ours_away, theirs_away = (g, y) if first_home else (x, o)
                # equal on both counts: a coin decides, both may happen
                if (ours, ours_away) >= (theirs, theirs_away):
                    can_pass = True
                if (ours, ours_away) <= (theirs, theirs_away):
                    can_fail = True
            if can_pass and lowest is None:
                lowest = g
            if can_fail:
                highest = g
        out.append("%d %d" % (lowest, highest))
    print("\n".join(out))


main()
