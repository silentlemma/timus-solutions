from array import array
import sys

START_HEIGHT = 100_000
OUTPUT_BLOCK = 1024


def main():
    tokens = (int(token) for line in sys.stdin.buffer for token in line.split())
    count = next(tokens)
    at_height = array("H", [0]) * (START_HEIGHT + 1)
    coordinates = [0] * (count + 1)
    for flag in range(1, count + 1):
        coordinates[flag] = next(tokens)
        at_height[next(tokens)] = flag

    path = array("H")
    right = False
    previous_x = 0
    for flag in reversed(at_height):
        if not flag:
            continue
        if not path:
            path.append(flag)
            previous_x = coordinates[flag]
            continue
        x = coordinates[flag]
        step = x > previous_x
        # Extend the current monotone run or start the next one at a turn.
        if len(path) == 1 or step != right:
            path.append(flag)
        else:
            path[-1] = flag
        right = step
        previous_x = x

    output = sys.stdout
    output.write(f"{len(path)}\n")
    for start in range(0, len(path), OUTPUT_BLOCK):
        end = start + OUTPUT_BLOCK
        output.write(" ".join(map(str, path[start:end])))
        output.write(" " if end < len(path) else "\n")


if __name__ == "__main__":
    main()
