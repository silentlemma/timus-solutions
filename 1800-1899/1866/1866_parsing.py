import sys

# (name, syllables in a foot, place of the stressed syllable from 1)
METERS = [("trochee", 2, 1), ("iamb", 2, 2), ("dactyl", 3, 1),
          ("amphibrach", 3, 2), ("anapaest", 3, 3)]


def stresses(line):
    return [("[" in s) for word in line.split() for s in word.split("-") if s]


def main():
    lines = sys.stdin.read().split("\n")
    n = int(lines[0])
    poem = [stresses(line) for line in lines[1:n + 1]]
    for name, foot, place in METERS:
        # the last foot may be cut short, so only the place within a foot
        # matters, and every syllable must agree with it
        if all(s == (i % foot == place - 1) for line in poem for i, s in enumerate(line)):
            print(name)
            return
    print("not a poem")


main()
