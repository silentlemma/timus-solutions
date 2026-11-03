import sys


def main():
    data = iter(sys.stdin.read().split())
    n = int(next(data))
    # every sum from 1 to reach is made of the notes taken so far; a note
    # no larger than reach + 1 extends that to reach + note
    reach = 0
    for _ in range(n):
        note = int(next(data))
        if note > reach + 1:
            break
        reach += note
    print(reach + 1)


main()
