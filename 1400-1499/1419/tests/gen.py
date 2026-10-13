"""Island pictures: SEED MODE WIDTH HEIGHT (dimensions count islands).

cubic: random reflections of cubic tiles joined along a random spanning tree;
       WIDTH and HEIGHT are even, from 4 to 50.
missing: the same construction with the last horizontal bridge removed.
random: independent legal bridge slots with seeded random density;
        WIDTH and HEIGHT are from 1 to 50.
Every mode prints all spaces, including spaces at the ends of rows.
"""

import random
import sys


# Small cubic tiles with complete perimeters; each remains connected after any
# edge deletion. Joining two tiles by replacing two edges preserves this property.
TILES = {
    (4, 4): (
        'O-O-O-O',
        '|\\|/ /|',
        'O O O-O',
        '|\\   \\|',
        'O-O O O',
        '|/ /|\\|',
        'O-O-O-O',
    ),
    (4, 6): (
        'O-O-O-O',
        '|\\ \\|/|',
        'O O O O',
        '|\\|\\ /|',
        'O-O O-O',
        '|     |',
        'O-O O-O',
        '|/| |\\|',
        'O O O O',
        '|/| |\\|',
        'O-O-O-O',
    ),
    (6, 4): (
        'O-O-O-O-O-O',
        '|\\ \\ \\ \\|/|',
        'O-O O-O O O',
        '| | |/   /|',
        'O-O O O O-O',
        '|/ / /|\\ \\|',
        'O-O-O-O-O-O',
    ),
    (6, 6): (
        'O-O-O-O-O-O',
        '|\\ \\ \\ \\|/|',
        'O O-O O O O',
        '|\\ \\ \\|\\ /|',
        'O-O O O-O O',
        '| |/|    /|',
        'O-O O-O-O O',
        '|   | |/ /|',
        'O-O O O O-O',
        '|/| |\\ \\ \\|',
        'O-O-O-O-O-O',
    ),
}


def partition(size, rng):
    assert 4 <= size <= 50 and size % 2 == 0
    parts = [4] * (size // 4)
    if size % 4:
        parts[-1] = 6
    rng.shuffle(parts)
    return parts


def reflect(rows, rng):
    if rng.randrange(2):
        rows = [row[::-1].translate(str.maketrans("/\\", "\\/")) for row in rows]
    if rng.randrange(2):
        rows = [row.translate(str.maketrans("/\\", "\\/")) for row in rows[::-1]]
    return rows


def cubic(w, h, rng):
    widths, heights = partition(w, rng), partition(h, rng)
    rows = [[' '] * (2*w-1) for _ in range(2*h-1)]
    tiles = []
    y = 0
    for th in heights:
        x = 0
        for tw in widths:
            tile = reflect(list(TILES[tw, th]), rng)
            for r, line in enumerate(tile):
                rows[2*y+r][2*x:2*x+len(line)] = line
            tiles.append((x, y, tw, th))
            x += tw
        y += th
    cols = len(widths)
    joins = []
    for i in range(len(tiles)):
        if i % cols + 1 < cols:
            joins.append((i, i+1, 'horizontal'))
        if i + cols < len(tiles):
            joins.append((i, i+cols, 'vertical'))
    rng.shuffle(joins)
    parent = list(range(len(tiles)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for a, b, direction in joins:
        pa, pb = find(a), find(b)
        if pa == pb:
            continue
        parent[pa] = pb
        x, y, tw, th = tiles[a]
        if direction == 'horizontal':
            r = 2 * (y + rng.randrange(th-1))
            c = 2 * (x+tw) - 2
            assert rows[r+1][c] == rows[r+1][c+2] == '|'
            rows[r+1][c] = rows[r+1][c+2] = ' '
            rows[r][c+1] = rows[r+2][c+1] = '-'
        else:
            r = 2 * (y+th) - 2
            c = 2 * (x + rng.randrange(tw-1))
            assert rows[r][c+1] == rows[r+2][c+1] == '-'
            rows[r][c+1] = rows[r+2][c+1] = ' '
            rows[r+1][c] = rows[r+1][c+2] = '|'
    return rows


def main():
    seed, mode, w, h = sys.argv[1:]
    rng = random.Random(int(seed))
    w, h = int(w), int(h)
    assert 1 <= w <= 50 and 1 <= h <= 50
    if mode in ('cubic', 'missing'):
        rows = cubic(w, h, rng)
        if mode == 'missing':
            assert rows[-1][-2] == '-'
            rows[-1][-2] = ' '
    elif mode == 'random':
        rows = [['O' if r % 2 == c % 2 == 0 else ' ' for c in range(2*w-1)]
                for r in range(2*h-1)]
        for r, row in enumerate(rows):
            for c in range(len(row)):
                if r % 2 == 0 and c % 2:
                    row[c] = rng.choice('--- ')
                elif r % 2 and c % 2 == 0:
                    row[c] = rng.choice('||| ')
                elif r % 2 and c % 2:
                    row[c] = rng.choice('/\\ ')
    else:
        raise ValueError('unknown mode: ' + mode)
    # Explicit LF output also when the generator is used directly on Windows.
    data = f'{2*w-1} {2*h-1}\n' + '\n'.join(''.join(row) for row in rows) + '\n'
    sys.stdout.buffer.write(data.encode('utf-8'))


if __name__ == '__main__':
    main()
