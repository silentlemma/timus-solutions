import sys


BLOCK_SIDE = 2


def reconstruct(photo):
    rows, columns = len(photo), len(photo[0])
    counts = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            value = photo[row][column]
            if row:
                value -= counts[row - 1][column]
            if column:
                value -= counts[row][column - 1]
            if row and column:
                value -= counts[row - 1][column - 1]
            counts[row][column] = value
    layers = []
    for level in range(min(rows, columns) // BLOCK_SIDE):
        layer = []
        for row in range(rows // BLOCK_SIDE - level):
            line = []
            for column in range(columns // BLOCK_SIDE - level):
                x = level + BLOCK_SIDE * row
                y = level + BLOCK_SIDE * column
                line.append('R' if counts[x][y] > level // BLOCK_SIDE else 'W')
            layer.append(''.join(line))
        layers.append(layer)
    return layers


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    rows, columns = next(data), next(data)
    photo = [[next(data) for _ in range(columns)] for _ in range(rows)]
    layers = reconstruct(photo)
    print('\n\n'.join('\n'.join(layer) for layer in layers))


if __name__ == '__main__':
    main()
