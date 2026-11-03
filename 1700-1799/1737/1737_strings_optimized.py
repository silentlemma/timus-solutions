import sys

LIMIT = 100000
LETTERS = "abc"
PERIOD = len(LETTERS)
WORD_COUNT = PERIOD * (PERIOD - 1)

n = int(sys.stdin.read())
write = sys.stdout.write
if n == 1:
    for letter in LETTERS:
        write(letter + "\n")
elif WORD_COUNT * n > LIMIT:
    write("TOO LONG\n")
else:
    for first in LETTERS:
        for second in LETTERS:
            if first != second:
                third = next(c for c in LETTERS if c != first and c != second)
                pattern = first + second + third
                write(pattern * (n // PERIOD) + pattern[: n % PERIOD] + "\n")
