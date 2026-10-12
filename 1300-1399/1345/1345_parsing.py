import sys

KEYWORDS = set(
    "and array begin case class const div do else end for function if implementation interface"
    " mod not of or procedure program record repeat shl shr string then to type unit until uses"
    " var with while".split()
)
WORD = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")
DIGIT = set("0123456789")


def wrap(kind, text):
    return "<span class=%s>%s</span>" % (kind, text)


def main():
    # bytes above 127 pass through unchanged as latin-1 characters
    text = sys.stdin.buffer.read().decode("latin-1").replace("\r\n", "\n")
    out, i, n = [], 0, len(text)
    while i < n:
        c = text[i]
        if c == "{":
            j = text.find("}", i)
            j = n if j < 0 else j + 1
            out.append(wrap("comment", text[i:j]))
        elif text.startswith("//", i):
            j = text.find("\n", i)
            j = n if j < 0 else j  # the line break is not part of it
            out.append(wrap("comment", text[i:j]))
        elif c == "'":
            j = text.find("'", i + 1)
            j = n if j < 0 else j + 1
            out.append(wrap("string", text[i:j]))
        elif c == "#" and i + 1 < n and text[i + 1] in DIGIT:
            j = i + 1
            while j < n and text[j] in DIGIT:
                j += 1
            out.append(wrap("string", text[i:j]))
        elif c in DIGIT:
            j = i
            while j < n and text[j] in DIGIT:
                j += 1
            # one point is allowed, but only with digits after it
            if j + 1 < n and text[j] == "." and text[j + 1] in DIGIT:
                j += 1
                while j < n and text[j] in DIGIT:
                    j += 1
            out.append(wrap("number", text[i:j]))
        elif c in WORD:
            j = i
            while j < n and (text[j] in WORD or text[j] in DIGIT):
                j += 1
            word = text[i:j]
            out.append(wrap("keyword", word) if word.lower() in KEYWORDS else word)
        else:
            j = i + 1
            out.append(c)
        i = j
    sys.stdout.buffer.write("".join(out).encode("latin-1"))


main()
