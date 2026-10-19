import random
import sys


def main():
    kind, size, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    values = list(range(1, size + 1))
    if kind == "reverse":
        values.reverse()
    elif kind == "reverse_prefix":
        values[:-1] = values[:-1][::-1]
    elif kind == "random":
        random.Random(seed).shuffle(values)
    elif kind == "alternating":
        values = values[::2] + values[1::2]
    elif kind == "left":
        values = values[1:] + values[:1]
    elif kind == "right":
        values = values[-1:] + values[:-1]
    else:
        assert kind == "identity"
    print(size)
    print(*values)


if __name__ == "__main__":
    main()
