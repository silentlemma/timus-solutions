import re
import sys

# common pieces of English, tried along with the frequent words of the text
PIECES = (
    "\n| the |the | and |ing | of | to |ed |he |th|in|er|an|re|on|at|en|nd|es|or|ou|ha|is|it|"
    "te|st|ar|al|le|se|ve|me|ne|hi|as|ng|e |s |d |t |, |. |y |o "
).split("|")

LINE = 17  # a table line without its piece: '    t[NNN] = "";' and a line end
CHUNK = 1000  # characters of the coded text per string literal
WORDS = 300  # the most promising words of the text that are tried

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
    used = set(text)
    free = [chr(c) for c in range(FIRST, LAST + 1) if chr(c) not in used and chr(c) not in SPECIAL]
    # words of the text, with the space before them and without
    counts = {}
    for m in re.finditer(r"[A-Za-z]+", text):
        word = m.group(0)
        if len(word) < 2:
            continue
        if m.start() > 0 and text[m.start() - 1] == " ":
            key = " " + word
            counts[key] = counts.get(key, 0) + 1
        counts[word] = counts.get(word, 0) + 1
    words = sorted(counts, key=lambda w: (-counts[w] * (len(w) - 1), w))[:WORDS]
    # a piece made only of characters of the text can never match a code
    candidates = [p for p in PIECES if all(ch in used for ch in p)]
    estimate = {p: text.count(p) * (len(literal(p)) - 1) for p in candidates}
    for w in words:
        estimate[w] = max(estimate.get(w, 0), counts[w] * (len(w) - 1))
    order = sorted(estimate, key=lambda p: (-estimate[p], p))
    table = []
    for piece in order:
        if not free:
            break
        cost = len(literal(piece))
        # every use saves the written length of the piece less one character
        if text.count(piece) * (cost - 1) > LINE + cost:
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
