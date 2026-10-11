"""Checker. Timus compiles and runs the archive; this checker cannot
compile C++, so it accepts archives in the one layout these solutions
print and runs that layout itself: the //CPP line, string literals with
the coded text, a table of codes, and the fixed decoding loop. The
output of the archive must equal the input (line ends aside), and for
inputs of at least 20000 characters, as the statement promises, the
archive must be strictly shorter than the input."""

import re
import sys

LONG = 20000
HEAD = ["//CPP", "#include <cstdio>", "const char *d[] = {"]
MIDDLE = ["0};", "int main() {", "    const char *t[256] = {0};"]
TAIL = [
    "    for (int k = 0; d[k]; k++)",
    "        for (const char *p = d[k]; *p; p++)",
    "            if (t[(unsigned char)*p]) fputs(t[(unsigned char)*p], stdout);",
    "            else putchar(*p);",
    "    return 0;",
    "}",
]
ESCAPES = {"n": "\n", '"': '"', "\\": "\\", "?": "?"}
CODES = 256


def fail(reason):
    print(reason)
    sys.exit(1)


def unescape(body):
    out, i = [], 0
    while i < len(body):
        ch = body[i]
        if ch == '"':
            fail("a bare quote inside a string")
        if ch == "\\":
            if i + 1 >= len(body) or body[i + 1] not in ESCAPES:
                fail("an unknown escape in a string")
            out.append(ESCAPES[body[i + 1]])
            i += 2
        else:
            out.append(ch)
            i += 1
    return "".join(out)


def main():
    inp, _, output = sys.argv[1:4]
    text = open(inp, newline="").read().replace("\r", "")
    archive = open(output, newline="").read().replace("\r", "")
    if len(text) >= LONG and len(archive) >= len(text):
        fail("the archive has %d characters, the text %d" % (len(archive), len(text)))
    lines = archive.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    if lines[: len(HEAD)] != HEAD:
        fail("the archive does not start with the expected lines")
    pos = len(HEAD)
    data = []
    while pos < len(lines) and lines[pos] != MIDDLE[0]:
        m = re.fullmatch(r'"(.*)",', lines[pos])
        if not m:
            fail("line %d is not a string of the data" % (pos + 1))
        data.append(unescape(m.group(1)))
        pos += 1
    if lines[pos : pos + len(MIDDLE)] != MIDDLE:
        fail("the data is not followed by the expected lines")
    pos += len(MIDDLE)
    table = {}
    while pos < len(lines) and lines[pos] != TAIL[0]:
        m = re.fullmatch(r'    t\[(\d+)\] = "(.*)";', lines[pos])
        if not m or not 0 < int(m.group(1)) < CODES:
            fail("line %d is not an entry of the table" % (pos + 1))
        table[chr(int(m.group(1)))] = unescape(m.group(2))
        pos += 1
    if lines[pos:] != TAIL:
        fail("the archive does not end with the decoding loop")
    printed = "".join(table.get(ch, ch) for ch in "".join(data))
    if printed != text:
        fail("the archive prints a different text")


if __name__ == "__main__":
    main()
