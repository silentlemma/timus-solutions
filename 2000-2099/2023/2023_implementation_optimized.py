import sys


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    count = int(next(tokens))
    position = steps = 0
    for _ in range(count):
        initial = next(tokens)[0]
        target = 0 if initial in b"APOR" else 1 if initial in b"BMS" else 2
        steps += abs(target - position)
        position = target
    print(steps)


main()
