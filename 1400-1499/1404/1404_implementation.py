SHIFT = 5  # added to the first letter
LETTERS = 26


def main():
    word = input().strip()
    # each code is the previous code plus the letter, modulo 26: take differences
    prev, plain = SHIFT, []
    for ch in word:
        code = ord(ch) - ord("a")
        plain.append(chr(ord("a") + (code - prev) % LETTERS))
        prev = code
    print("".join(plain))


main()
