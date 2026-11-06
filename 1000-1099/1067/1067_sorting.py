from sys import stdin, stdout


def main():
    tokens = iter(stdin.buffer.read().split())
    count = int(next(tokens))
    paths = sorted(tuple(next(tokens).split(b"\\")) for _ in range(count))
    previous = ()
    write = stdout.buffer.write
    for path in paths:
        shared = 0
        while shared < min(len(previous), len(path)) and path[shared] == previous[shared]:
            shared += 1
        for depth in range(shared, len(path)):
            write(b" " * depth + path[depth] + b"\n")
        previous = path


main()
