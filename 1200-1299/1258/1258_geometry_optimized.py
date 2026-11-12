import sys

NUMBER_FIELDS = 6


def main():
    data = sys.stdin.buffer.read().split()
    width, depth, start_x, start_y, end_x, end_y = map(int, data[:NUMBER_FIELDS])
    # Reflect the endpoint in reverse hit order to undo every bounce.
    for word in reversed(data[NUMBER_FIELDS:]):
        for wall in reversed(word):
            if wall == ord("L"):
                end_x = -end_x
            elif wall == ord("R"):
                end_x = 2 * width - end_x
            elif wall == ord("F"):
                end_y = -end_y
            else:
                end_y = 2 * depth - end_y
    squared = (end_x - start_x) ** 2 + (end_y - start_y) ** 2
    print(f"{squared**0.5:.4f}")


main()
