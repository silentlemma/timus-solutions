from os import _exit, write


def cooking_time(steaks, capacity):
    if steaks <= capacity:
        return 2
    return (2 * steaks + capacity - 1) // capacity


def main():
    steaks, capacity = map(int, open(0, "rb", buffering=0).read().split())
    write(1, (str(cooking_time(steaks, capacity)) + "\n").encode())
    _exit(0)


main()
