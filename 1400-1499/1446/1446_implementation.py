import sys

HOUSES = ["Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"]


def main():
    lines = sys.stdin.read().split("\n")
    n = int(lines[0])
    lists = {house: [] for house in HOUSES}
    for i in range(n):
        # names keep their inner spaces, so only the line break is dropped
        name, house = lines[1 + 2 * i].rstrip("\r"), lines[2 + 2 * i].strip()
        lists[house].append(name)
    blocks = ["%s:\n%s\n" % (house, "\n".join(lists[house])) for house in HOUSES]
    sys.stdout.write("\n".join(blocks))


main()
