import sys

WIDTH = 40


def main():
    data = sys.stdin.buffer.read().replace(b"\r", b"").decode("latin-1")
    lines = data.split("\n")
    n = int(lines[0])
    # a rule s1-s2 matches words ending in s1s2 and carries s2 over
    rules = []
    for line in lines[1 : n + 1]:
        left, _, right = line.strip().partition("-")
        rules.append(((left + right).lower(), len(right)))
    text = "\n".join(lines[n + 1 :])
    out = []
    col = 0
    i = 0
    while i < len(text):
        c = text[i]
        if c == "\n":
            out.append(c)
            col = 0
            i += 1
            continue
        if not c.isascii() or not c.isalpha():
            # a full line moves a separator to the next one
            if col == WIDTH:
                out.append("\n")
                col = 0
            out.append(c)
            col += 1
            i += 1
            continue
        start = i
        while i < len(text) and text[i].isascii() and text[i].isalpha():
            i += 1
        word = text[start:i]
        if col + len(word) <= WIDTH:
            out.append(word)
            col += len(word)
            continue
        # the shortest carried part whose head and '-' still fit
        lower = word.lower()
        carry = min(
            (
                cut
                for pattern, cut in rules
                if lower.endswith(pattern) and col + len(word) - cut + 1 <= WIDTH
            ),
            default=0,
        )
        if carry:
            out.append(word[:-carry] + "-\n" + word[-carry:])
        else:
            out.append("\n" + word)
            carry = len(word)
        col = carry
    sys.stdout.write("".join(out))


main()
