import sys

LOWER, UPPER = 1, 2
END = 3
ALPHABET = 26
BYTE_BITS = 8
CHUNK_SIZE = 4096
CLASSES = bytearray(1 << BYTE_BITS)
CLASSES[ord("a") : ord("z") + 1] = bytes([LOWER]) * ALPHABET
CLASSES[ord("A") : ord("Z") + 1] = bytes([UPPER]) * ALPHABET
for character in b".?!":
    CLASSES[character] = END
CLASSES = bytes(CLASSES)


def main():
    read = sys.stdin.buffer.read
    lower, upper, end = LOWER, UPPER, END
    new_sentence, in_word = True, False
    errors = 0
    chunk = read(CHUNK_SIZE)
    while chunk:
        for kind in chunk.translate(CLASSES):
            if kind == lower:
                errors += new_sentence
                new_sentence, in_word = False, True
            elif kind == upper:
                errors += in_word
                new_sentence, in_word = False, True
            else:
                in_word = False
                if kind == end:
                    new_sentence = True
        chunk = read(CHUNK_SIZE)
    print(errors)


if __name__ == "__main__":
    main()
