import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # every sum from 1 to reach is made of the notes taken so far; a note
    # no larger than reach + 1 extends that to reach + note
    reach = 0
    for note in sorted(int(x) for x in data[1 : n + 1]):
        if note > reach + 1:
            break
        reach += note
    print(reach + 1)


main()
