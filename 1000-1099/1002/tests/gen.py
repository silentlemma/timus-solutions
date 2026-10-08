"""Deterministic input modes:

SEED COUNT LENGTH: legacy random dictionary and a phone spelled by its words.
limit SEED: 50,000 words and almost 300 KB, with a 100-digit phone.
random SEED COUNT: many small dictionaries, with arbitrary or spellable phones.
"""

import random
import sys

LETTERS = "abcdefghijklmnopqrstuvwxyz"
KEYPAD = str.maketrans(LETTERS, "22233344115566070778889990")
MAX_PHONE = 100

mode = sys.argv[1]
if mode in ("limit", "random"):
    sys.stdout.reconfigure(newline="\n")

if mode == "limit":
    rng = random.Random(int(sys.argv[2]))
    words = [
        "".join(rng.choice(LETTERS) for _ in range(4 if i < 1000 else 5))
        for i in range(50000)
    ]
    phone = "".join(words[rng.randrange(1000, len(words))].translate(KEYPAD) for _ in range(20))
    print(phone)
    print(len(words))
    print("\n".join(words))
    print(-1)
    sys.exit()

if mode == "random":
    rng = random.Random(int(sys.argv[2]))
    for case in range(int(sys.argv[3])):
        words = [
            "".join(rng.choice("ijabcdefoqz") for _ in range(rng.randint(1, 6)))
            for _ in range(rng.randint(4, 18))
        ]
        if case % 2:
            phone = "".join(rng.choice(words).translate(KEYPAD) for _ in range(rng.randint(1, 5)))
        else:
            phone = "".join(rng.choice("0123") for _ in range(rng.randint(1, 22)))
        print(phone)
        print(len(words))
        print("\n".join(words))
    print(-1)
    sys.exit()

seed, words_count, word_length = int(mode), int(sys.argv[2]), int(sys.argv[3])
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
