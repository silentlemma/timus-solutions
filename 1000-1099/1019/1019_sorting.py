import sys

END = 10**9


def main():
    read = sys.stdin.buffer.readline
    paints = []
    coordinates = {0, END}
    for _ in range(int(read())):
        a, b, color = read().split()
        a, b = int(a), int(b)
        paints.append((a, b, color))
        coordinates.update((a, b))
    points = sorted(coordinates)
    index = {value: position for position, value in enumerate(points)}
    white = bytearray(b"w") * (len(points) - 1)
    # Slice assignment performs the direct repainting in native code.
    for a, b, color in paints:
        left, right = index[a], index[b]
        white[left:right] = color * (right - left)
    best_left = best_right = run_start = 0
    for position, color in enumerate(white):
        if color != ord("w"):
            run_start = position + 1
        elif points[position + 1] - points[run_start] > best_right - best_left:
            best_left, best_right = points[run_start], points[position + 1]
    print(best_left, best_right)


main()
