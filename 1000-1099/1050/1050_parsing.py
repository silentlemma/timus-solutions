import sys

BACKSLASH, QUOTE, NEWLINE = ord("\\"), ord('"'), ord("\n")
BLANK = b" \t\r\v\f"


def main():
    # the text is handled as bytes: letters above 127 are copied as they are
    s = sys.stdin.buffer.read()
    n = len(s)
    replace = {}  # position of a quote -> what is printed instead
    quotes = []

    def close():
        """Pairs the quotes of the finished paragraph; an unpaired last one goes away."""
        if len(quotes) % 2:
            replace[quotes.pop()] = b""
        for k, q in enumerate(quotes):
            replace[q] = b"``" if k % 2 == 0 else b"''"
        quotes.clear()

    i = 0
    while i < n:
        c = s[i]
        if c == BACKSLASH:
            # \" is an umlaut; otherwise the command name is the letters after \.
            if i + 1 < n and s[i + 1] == QUOTE:
                i += 2
                continue
            j = i + 1
            while j < n and s[j : j + 1].isalpha():
                j += 1
            if s[i + 1 : j] == b"par":
                close()
            i = j
        elif c == QUOTE:
            quotes.append(i)
            i += 1
        else:
            # a line of only whitespace that ends with a line break ends a paragraph
            if c == NEWLINE:
                j = i + 1
                while j < n and s[j] in BLANK:
                    j += 1
                if j < n and s[j] == NEWLINE:
                    close()
            i += 1
    close()
    out = bytearray()
    start = 0
    for q in sorted(replace):
        out += s[start:q] + replace[q]
        start = q + 1
    out += s[start:]
    sys.stdout.buffer.write(out)


main()
