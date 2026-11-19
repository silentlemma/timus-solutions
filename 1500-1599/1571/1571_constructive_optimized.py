import os
from sys import stdout

SMALL = 2


def free_language(spoken):
    if b"english" not in spoken:
        return b"english"
    for letter in range(ord("a"), ord("z") + 1):
        candidate = bytes((letter,))
        if candidate not in spoken:
            return candidate
    for first in range(ord("a"), ord("z") + 1):
        for second in range(ord("a"), ord("z") + 1):
            candidate = bytes((first, second))
            if candidate not in spoken:
                return candidate


words = open(0, "rb", buffering=0).read().split()
count = int(words[0])
languages = words[1 : count + 1]
spoken = set(languages)
if len(spoken) < count:
    print(0 if count == SMALL else "Impossible")
elif count == 1:
    print(0)
elif count == SMALL:
    print(1)
    stdout.flush()
    stdout.buffer.write(languages[0] + b"-" + languages[1] + b"\n")
else:
    hub = free_language(spoken)
    print(count)
    # Keep text and byte output ordered before emitting the edges.
    stdout.flush()
    for language in languages:
        stdout.buffer.write(language + b"-" + hub + b"\n")

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
