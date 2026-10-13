import sys

OPEN = ord(".")
FLAT = ord("-")
UPRIGHT = ord("|")
SECRET = ord("#")


def main():
    pic = [line.rstrip(b"\r\n") for line in sys.stdin.buffer]
    while pic and not pic[-1]:
        pic.pop()
    h = len(pic)
    w = max((len(line) for line in pic), default=0)
    # walls run along the middle lines of the cells, so the four quarters
    # around a corner of the grid always meet: the corners are the places
    # an agent can be, and a cell joins some of its four corners
    side = w + 1
    parent = list(range((h + 1) * side))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b

    secrets = []
    for r, line in enumerate(pic):
        top, bottom = r * side, (r + 1) * side
        for c, ch in enumerate(line):
            if ch == OPEN:  # joins all four corners
                union(top + c, top + c + 1)
                union(top + c, bottom + c)
                union(top + c, bottom + c + 1)
            elif ch == FLAT:  # keeps the upper and the lower pair apart
                union(top + c, top + c + 1)
                union(bottom + c, bottom + c + 1)
            elif ch == UPRIGHT:  # keeps the left and the right pair apart
                union(top + c, bottom + c)
                union(top + c + 1, bottom + c + 1)
            elif ch == SECRET:  # numbered from the right within a row
                secrets.append((r, -c, (top + c, top + c + 1, bottom + c, bottom + c + 1)))
    secrets.sort()
    # an agent may not pass through a secret, so two secrets are joined when
    # some corner of one shares a region with some corner of the other
    regions = [{find(v) for v in corners} for _, _, corners in secrets]
    print("\n".join("".join("1" if a & b else "0" for b in regions) for a in regions))


main()
