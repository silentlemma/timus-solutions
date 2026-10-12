"""About 100000 characters of Pascal-like text: a seed and a mode. Mode 1
mixes words, keywords in random case, numbers, strings, character codes
and both kinds of comments, mode 2 adds Cyrillic letters, which the
judge gives as bytes above 127, inside strings, mode 3 ends without a
line break. Mode 4 is exactly 100000 characters dominated by one multiline
brace comment; mode 5 by one quoted string. Mode 6 fills the size limit
with short conditional assignments; mode 7 with seeded random complete
statements. Modes 4-7 emit complete Pascal programs with a final newline."""

import random
import sys

LENGTH = 100000
KEYWORDS = "begin end for to do if then else var string procedure function and or not".split()
LATIN = "abcdefghijklmnopqrstuvwxyz"
CYRILLIC_A, CYRILLIC_YA = 0x410, 0x44F


def piece(rng, mode):
    kind = rng.randrange(9)
    if kind == 0:
        word = rng.choice(KEYWORDS)
        return "".join(c.upper() if rng.random() < 0.5 else c for c in word)
    if kind == 1:
        return rng.choice("_" + LATIN) + "".join(
            rng.choices(LATIN + "0123456789_", k=rng.randint(0, 6))
        )
    if kind == 2:
        number = str(rng.randint(0, 99999))
        return number + rng.choice(["", "." + str(rng.randint(0, 999)), ".", ".."])
    if kind == 3:
        inner = "".join(rng.choices(LATIN + " {}/#1", k=rng.randint(0, 8)))
        if mode == 2:
            inner += chr(rng.randint(CYRILLIC_A, CYRILLIC_YA))
        return "'" + inner + "'"
    if kind == 4:
        return "#" + str(rng.randint(0, 255))
    if kind == 5:
        inner = "".join(rng.choices(LATIN + " '{/#9", k=rng.randint(0, 10)))
        return "{" + inner.replace("}", "") + "}"
    if kind == 6:
        return "//" + "".join(rng.choices(LATIN + " '{}#7", k=rng.randint(0, 10))) + "\n"
    if kind == 7:
        return rng.choice([" ", "  ", "\n", ";", ":=", "(", ")", ".", ",", "+", "-", "<", ">"])
    return " "


def boundary_program(seed, mode):
    rng = random.Random(seed)
    if mode == 4:
        prefix, suffix = "begin\n{", "}\nend.\n"
        alphabet = " abcXYZ0123'#/{\n"
    elif mode == 5:
        prefix, suffix = "begin\n  writeln('", "');\nend.\n"
        alphabet = ' abcXYZ0123#/{}</>&"'
    else:
        prefix, suffix = "program Stress;\nvar x: real;\nbegin\n", "end.\n"
        parts, size = [prefix], len(prefix)
        while True:
            if mode == 6:
                part = "if 0=0 then x:=1;\n"
            else:
                a, b = rng.randrange(1000), rng.randrange(1, 1000)
                part = rng.choice(
                    [
                        f"x := -{a}.{b:03d} + ({b} / 2);\n",
                        f"if {a}={b} then x:={a};\n",
                        f"writeln('begin <&> // {{{a}}}', #0, #255);\n",
                        f"{{ // '{a} #13\nsecond line }}x:={b};\n",
                        f"x:={a}; // '{{ #255 end. {b}\n",
                        f"writeln('', #00065, 'x{a}');\n",
                    ]
                )
            # Reserve an empty comment for exact-length padding.
            if size + len(part) + len(suffix) + 3 > LENGTH:
                break
            parts.append(part)
            size += len(part)
        padding = LENGTH - size - len(suffix)
        return "".join(parts) + "{" + " " * (padding - 3) + "}\n" + suffix
    size = LENGTH - len(prefix) - len(suffix)
    return prefix + "".join(rng.choices(alphabet, k=size)) + suffix


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    if mode in (4, 5, 6, 7):
        sys.stdout.buffer.write(boundary_program(seed, mode).encode("utf-8"))
        return
    rng = random.Random(seed)
    parts, size = [], 0
    while size < LENGTH - 100:
        part = piece(rng, mode)
        parts.append(part)
        size += len(part)
    text = "".join(parts).rstrip("\n")
    if mode != 3:
        text += "\n"
    sys.stdout.buffer.write(text.encode("utf-8"))


main()
