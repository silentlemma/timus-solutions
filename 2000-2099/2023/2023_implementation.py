import sys


def solve(names):
    position = steps = 0
    for name in names:
        initial = name[0]
        target = 0 if initial in "APOR" else 1 if initial in "BMS" else 2
        steps += abs(target - position)
        position = target
    return steps


def main():
    tokens = sys.stdin.read().split()
    count = int(tokens[0])
    print(solve(tokens[1 : count + 1]))


if __name__ == "__main__":
    main()
