import sys

NONE = -1  # no term starts here
BIG = 2**63 - 1  # a glued number that does not fit is cut to this


class Parser:
    def __init__(self, s):
        self.s = s
        self.pos = 0

    def accept(self, c):
        if self.pos < len(self.s) and self.s[self.pos] == c:
            self.pos += 1
            return True
        return False

    def term(self):
        """A number, an operation with its arguments, a bracket, or NONE."""
        s = self.s
        if self.pos < len(s) and s[self.pos].isdigit():
            start = self.pos
            while self.pos < len(s) and s[self.pos].isdigit():
                self.pos += 1
            return int(s[start : self.pos])
        for sign in "+*/":
            if self.accept(sign):
                return self.fold(sign)
        if self.accept("("):
            x = self.glue(False)
            self.accept(")")
            return x
        return NONE

    def fold(self, sign):
        """The arguments of an operation are glued terms split by ';'."""
        a = self.glue(True)
        while self.accept(";"):
            b = self.glue(True)
            if sign == "+":
                a += b
            elif sign == "*":
                a *= b
            else:
                a = 0 if b == 0 else a // b
        return a

    def glue(self, inside):
        """Terms written one after another are glued as decimal strings.
        Inside an operation ';' ends the argument; elsewhere it glues the
        whole rest, and a missing term counts as 1."""
        parts = []
        x = self.term()
        while x != NONE or not parts:
            parts.append(x)
            if self.pos < len(self.s) and self.s[self.pos] == ";":
                if inside:
                    break
                self.pos += 1
                parts.append(self.glue(False))
            x = self.term()
        return min(int("".join(str(abs(p)) for p in parts)), BIG)


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()  # the text ends with a line break, not with an empty line
    out = []
    for i, line in enumerate(lines, 1):
        value = Parser(line.rstrip("\r")).glue(False)
        out.append("Expression %d evaluates to: %d" % (i, value))
    sys.stdout.write("".join(x + "\n" for x in out))


main()
