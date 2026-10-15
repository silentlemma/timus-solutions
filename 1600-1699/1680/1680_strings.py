import sys


def main():
    lines = sys.stdin.read().split("\n")
    n, q = (int(w) for w in lines[0].split()[1:])
    taken = set()
    for line in lines[1:n + 1]:
        team = line.strip()
        # the university is everything before " #k"; names differing only
        # in letter case are the same university
        university = team.rsplit("#", 1)[0].rstrip().lower() if "#" in team else team.lower()
        if university in taken:
            continue
        if len(taken) == q:
            print(team)
            return
        taken.add(university)


main()
