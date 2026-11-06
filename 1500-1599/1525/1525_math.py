from sys import stdin

BUFFER_SIZE = 4096
MOVES = {
    ord(letter): (axis, step)
    for axis, pair in enumerate(("lr", "du", "bf"))
    for letter, step in zip(pair, (-1, 1))
}


def main():
    source = stdin.buffer
    sizes = list(map(int, source.readline().split()))
    position = [0] * len(sizes)
    low = position.copy()
    high = position.copy()
    while block := source.read(BUFFER_SIZE):
        for letter in block:
            move = MOVES.get(letter)
            if move is None:
                continue
            axis, step = move
            value = position[axis] + step
            position[axis] = value
            if value < low[axis]:
                low[axis] = value
            elif value > high[axis]:
                high[axis] = value
    total = 1
    for size, bottom, top in zip(sizes, low, high):
        total *= max(1, size - (top - bottom))
    print(total)


main()
