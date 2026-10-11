"""Checker: the output must be a PIBAS program, one line of at most 32000
characters, that prints exactly its own text. The program is run by a
small interpreter of the grammar in the statement: statements separated
by semicolons, assignments V=expression and outputs ?expression, where an
expression is a sum of variables, quoted constants and $(V,start,length).
"""

import re
import sys

LONGEST = 32000


class Bad(Exception):
    pass


def split(text, sep):
    """Splits at sep outside quotes and parentheses."""
    parts, depth, quote, start = [], 0, None, 0
    for i, c in enumerate(text):
        if quote:
            if c == quote:
                quote = None
        elif c in "'\"":
            quote = c
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        elif c == sep and depth == 0:
            parts.append(text[start:i])
            start = i + 1
    if quote or depth:
        raise Bad("unbalanced quotes or parentheses")
    parts.append(text[start:])
    return parts


def value(term, variables):
    if re.fullmatch(r"[A-Z]", term):
        if term not in variables:
            raise Bad("variable %s used before it is set" % term)
        return variables[term]
    if len(term) >= 2 and term[0] in "'\"" and term[-1] == term[0]:
        body = term[1:-1]
        if term[0] in body:
            raise Bad("a quote inside its own constant")
        return body
    m = re.fullmatch(r"\$\(([A-Z]),(\d+),(\d+)\)", term)
    if m:
        s = value(m.group(1), variables)
        start, length = int(m.group(2)), int(m.group(3))
        if start < 1 or start - 1 + length > len(s):
            raise Bad("substring out of range")
        return s[start - 1 : start - 1 + length]
    raise Bad("not an expression: %r" % term[:40])


def run(program):
    variables, out = {}, []
    for statement in split(program, ";"):
        if statement.startswith("?"):
            out.append("".join(value(t, variables) for t in split(statement[1:], "+")))
        elif len(statement) > 2 and statement[1] == "=" and re.fullmatch(r"[A-Z]", statement[0]):
            variables[statement[0]] = "".join(
                value(t, variables) for t in split(statement[2:], "+")
            )
        else:
            raise Bad("not a statement: %r" % statement[:40])
    return "".join(out)


def main():
    output = sys.argv[3]
    lines = open(output).read().split("\n")
    program = lines[0].rstrip("\r")
    if any(line.strip() for line in lines[1:]):
        print("the program must fit on one line")
        sys.exit(1)
    if not program or len(program) > LONGEST:
        print("the program is empty or too long")
        sys.exit(1)
    try:
        printed = run(program)
    except Bad as e:
        print(e)
        sys.exit(1)
    if printed != program:
        print("the program prints %r" % printed[:80])
        sys.exit(1)


if __name__ == "__main__":
    main()
