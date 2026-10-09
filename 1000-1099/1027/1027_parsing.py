import sys

# characters allowed inside an arithmetic expression besides the brackets
EXPRESSION = set("=+-*/0123456789\r\n")


def valid(s):
    depth, i = 0, 0
    while i < len(s):
        if s.startswith("(*", i):
            # a comment ends at the first *) after its opening pair
            end = s.find("*)", i + 2)
            if end < 0:
                return False
            i = end + 2
            continue
        c = s[i]
        if c == "(":
            depth += 1
        elif c == ")":
            if depth == 0:
                return False
            depth -= 1
        elif depth > 0 and c not in EXPRESSION:
            return False
        i += 1
    return depth == 0


print("YES" if valid(sys.stdin.read()) else "NO")
