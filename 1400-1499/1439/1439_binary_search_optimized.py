import sys


def main():
    read = sys.stdin.buffer.readline
    _, events = map(int, read().split())
    gone = []
    output = bytearray()
    for _ in range(events):
        command, token = read().split()
        room = int(token)
        low, high = 0, len(gone)
        while low < high:
            middle = (low + high) // 2
            if gone[middle] - middle <= room:
                low = middle + 1
            else:
                high = middle
        original = room + low
        if command == b"D":
            gone.insert(low, original)
        else:
            output.extend(f"{original}\n".encode())
    # Input lines are discarded immediately; output holds bytes rather than Python integers.
    sys.stdout.buffer.write(output)


main()
