from os import _exit, write


def main():
    values = map(int, open(0, "rb", buffering=0).read().split())
    next(values)  # Exactly n distinct obstacle tokens follow the exit coordinate.
    exit_at = next(values)
    left = right = None
    for wall in values:
        # A barrier inside the open interval makes reachability impossible forever.
        if 0 < wall < exit_at or exit_at < wall < 0:
            write(1, b"Impossible\n")
            _exit(0)
        if wall < 0 and (left is None or wall > left):
            left = wall
        elif wall > 0 and (right is None or wall < right):
            right = wall
    if exit_at > 0:
        answer = str(exit_at) + " " + str(exit_at - 2 * left) + "\n"
    else:
        answer = str(2 * right - exit_at) + " " + str(-exit_at) + "\n"
    write(1, answer.encode())
    _exit(0)


main()
