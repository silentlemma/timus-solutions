"""One test with a large dictionary; the number is spelled by random words."""

import random
import sys

LETTERS = "abcdefghijklmnopqrstuvwxyz"
KEYPAD = str.maketrans(LETTERS, "22233344115566070778889990")
MAX_PHONE = 100

seed, words_count, word_length = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = random.Random(seed)
words = [
    "".join(rng.choice(LETTERS) for _ in range(rng.randint(1, word_length)))
    for _ in range(words_count)
]
phone = ""
while True:
    digits = rng.choice(words).translate(KEYPAD)
    if len(phone) + len(digits) > MAX_PHONE:
        break
    phone += digits
print(phone)
print(len(words))
print("\n".join(words))
print(-1)
