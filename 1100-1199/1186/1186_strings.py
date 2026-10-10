import sys
from collections import Counter


def number(s, i):
    # the number starting at s[i] (1 if there is none) and where it ends
    j = i
    while j < len(s) and s[j].isdigit():
        j += 1
    return (int(s[i:j]) if j > i else 1), j


def totals(formula):
    result = Counter()
    for term in formula.split("+"):
        times, i = number(term, 0)
        # one level per open bracket; a closing bracket multiplies its level
        # by the number after it and adds it to the level outside
        stack = [Counter()]
        while i < len(term):
            c = term[i]
            if c == "(":
                stack.append(Counter())
                i += 1
            elif c == ")":
                inner = stack.pop()
                k, i = number(term, i + 1)
                for name, count in inner.items():
                    stack[-1][name] += count * k
            else:
                j = i + 1
                if j < len(term) and term[j].islower():
                    j += 1
                k, end = number(term, j)
                stack[-1][term[i:j]] += k
                i = end
        for name, count in stack[0].items():
            result[name] += count * times
    return result


def main():
    lines = sys.stdin.read().split()
    left, n = lines[0], int(lines[1])
    want = totals(left)
    for right in lines[2 : 2 + n]:
        print("%s%s%s" % (left, "==" if totals(right) == want else "!=", right))


main()
