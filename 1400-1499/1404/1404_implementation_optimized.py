LETTERS = 26
FIRST = ord("a")
SHIFT = 5

word = bytearray(input().strip(), "ascii")
for i in range(len(word) - 1, 0, -1):
    word[i] = FIRST + (word[i] - word[i - 1]) % LETTERS
word[0] = FIRST + (word[0] - FIRST - SHIFT) % LETTERS
print(word.decode())
