import sys

MAX_COLOR = 100
SPACE = ord(" ")

# the colours, at most 100, fit in a bytearray, their texts are made once,
# and the answer is built as bytes
words = (word for line in sys.stdin.buffer for word in line.split())
n = int(next(words))
grid = bytearray(map(int, words))
colors = [str(value).encode() for value in range(MAX_COLOR + 1)]
answer = bytearray()
# diagonal holds the cells with row + column = diagonal; each is read from
# its lowest row up
for diagonal in range(2 * n - 1):
    for row in range(min(diagonal, n - 1), max(0, diagonal - n + 1) - 1, -1):
        answer.extend(colors[grid[row * n + diagonal - row]])
        answer.append(SPACE)
answer[-1] = 10
sys.stdout.buffer.write(answer)
