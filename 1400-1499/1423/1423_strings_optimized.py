from os import _exit, write


def main():
    values = open(0, "rb", buffering=0).read().split()
    size = int(values[0])
    first, second = values[1], values[2]
    offset = (first + first).find(second)
    answer = -1 if offset < 0 else (size - offset) % size
    write(1, (str(answer) + "\n").encode())
    _exit(0)


main()
