import sys

# common pieces of English, tried in this order; each one that pays off
# gets a printable character the text never uses
PIECES = (
    "\n| the |the | and |ing | of | to |ed |he |th|in|er|an|re|on|at|en|nd|es|or|ou|ha|is|it|"
    "te|st|ar|al|le|se|ve|me|ne|hi|as|ng|e |s |d |t |, |. |y |o "
).split("|")

ENTRY = 24  # the size of one table line, so a piece must save more than this
CHUNK = 1000  # characters of the coded text per string literal

FIRST = 33  # the first printable character that may become a code
LAST = 126  # and the last one
SPECIAL = '"\\?'  # need a backslash inside a C string


def literal(text):
    """The text as it is written inside a C string literal."""
    for ch in "\\" + SPECIAL.replace("\\", ""):
        text = text.replace(ch, "\\" + ch)
    return text.replace("\n", "\\n")


def main():
    text = sys.stdin.buffer.read().decode("latin-1").replace("\r", "")
    free = [chr(c) for c in range(FIRST, LAST + 1) if chr(c) not in text and chr(c) not in SPECIAL]
    table = []
    for piece in PIECES:
        if not free:
            break
        # every use saves the written length of the piece less one character
        if text.count(piece) * (len(literal(piece)) - 1) > ENTRY:
            code = free.pop(0)
            text = text.replace(piece, code)
            table.append((code, piece))
    out = sys.stdout
    out.write("//CPP\n#include <cstdio>\nconst char *d[] = {\n")
    for i in range(0, len(text), CHUNK):
        out.write('"' + literal(text[i : i + CHUNK]) + '",\n')
    out.write("0};\nint main() {\n    const char *t[256] = {0};\n")
    for code, piece in table:
        out.write('    t[%d] = "%s";\n' % (ord(code), literal(piece)))
    out.write(
        "    for (int k = 0; d[k]; k++)\n"
        "        for (const char *p = d[k]; *p; p++)\n"
        "            if (t[(unsigned char)*p]) fputs(t[(unsigned char)*p], stdout);\n"
        "            else putchar(*p);\n"
        "    return 0;\n}\n"
    )


main()
