import sys

WIDTH = 80


def main():
    line = sys.stdin.readline().rstrip("\r\n")
    screen = [" "] * WIDTH
    cursor = 0
    for key in line:
        if key == "<":
            cursor -= 1
        elif key == ">":
            cursor += 1
        else:
            screen[cursor] = key
            cursor += 1
        # past either edge the cursor jumps to the leftmost position
        if not 0 <= cursor < WIDTH:
            cursor = 0
    print("".join(screen))


main()
