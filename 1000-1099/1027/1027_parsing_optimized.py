import sys


OPEN = ord("(")
CLOSE = ord(")")
STAR = ord("*")
ALLOWED = b"=+-*/0123456789\r\n"


def valid(text):
    depth = cursor = 0
    size = len(text)
    while cursor < size:
        if depth == 0:
            opening = text.find(b"(", cursor)
            if opening < 0:
                return text.find(b")", cursor) < 0
            if text.find(b")", cursor, opening) >= 0:
                return False
            cursor = opening
        char = text[cursor]
        cursor += 1
        if char == OPEN:
            if cursor < size and text[cursor] == STAR:
                # Skip the entire opening pair before looking for its close.
                close = text.find(b"*)", cursor + 1)
                if close < 0:
                    return False
                cursor = close + 2
            else:
                depth += 1
        elif char == CLOSE:
            depth -= 1
        elif char not in ALLOWED:
            return False
    return depth == 0


def main():
    sys.stdout.write("YES\n" if valid(sys.stdin.buffer.read()) else "NO\n")


if __name__ == "__main__":
    main()
