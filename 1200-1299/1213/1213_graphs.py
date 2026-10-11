import sys


def main():
    lines = sys.stdin.read().split()
    names = {lines[0]}
    for line in lines[1:]:
        if line == "#":
            break
        names.update(line.split("-"))
    # every other compartment must be emptied through one opened partition,
    # and the partitions of a tree towards the airlock are enough
    print(len(names) - 1)


main()
