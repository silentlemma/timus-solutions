import sys


def main():
    lines = sys.stdin.read().split("\n")
    n = int(lines[0])
    # a name is the whole line, spaces included; only the line end goes
    names = [line.rstrip("\r") for line in lines[1 : 1 + n]]
    print(n - len(set(names)))


main()
