import operator
import re
import sys

LIMIT = 10**7
NUMBER = re.compile(r"-?\d+$")
END = -1


def divide(a, b):
    q = abs(a) // abs(b)  # rounds towards zero
    return q if (a < 0) == (b < 0) else -q


def remainder(a, b):
    r = abs(a) % abs(b)  # the remainder of a towards zero, then made non-negative
    return (r if a >= 0 else -r) % abs(b)


OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": divide,
    "%": remainder,
    "or": operator.or_,
    "and": operator.and_,
    "xor": operator.xor,
}
TESTS = {
    "==": operator.eq,
    "!=": operator.ne,
    ">=": operator.ge,
    ">": operator.gt,
    "<=": operator.le,
    "<": operator.lt,
}


def main():
    # a line is "label:", "label: command" or "command"; lines with only a label are no commands
    labels = {}
    commands = []
    for line in sys.stdin.read().split("\n"):
        tokens = line.split()
        if tokens and tokens[0].endswith(":"):
            labels[tokens[0][:-1].lower()] = len(commands)
            tokens = tokens[1:]
        if tokens:
            commands.append(tokens)
    names = {}  # variable name -> slot

    def slot(name):
        return names.setdefault(name, len(names))

    values = []
    assigned = []
    out = []

    def operand(tok):
        # a getter for a number or a variable
        if NUMBER.match(tok):
            v = int(tok)
            return lambda: v
        k = slot(tok)
        return lambda: values[k]

    ops = []
    for pc, t in enumerate(commands):
        head = t[0].lower()
        nxt = pc + 1
        if t[1:2] == ["="]:
            k = slot(t[0])
            rest = t[2:]  # a value, "not" and a value, or a value, an operation and a value
            if len(rest) == 1:
                f = operand(rest[0])
            elif len(rest) == 2:
                g = operand(rest[1])

                def f(g=g):
                    return ~g()

            else:
                x, name, y = rest
                a, b, op = operand(x), operand(y), OPS[name.lower()]

                def f(a=a, b=b, op=op):
                    return op(a(), b())

            def run(k=k, f=f, nxt=nxt):
                values[k] = f()
                assigned[k] = True
                return nxt

        elif head == "end":

            def run():
                return END

        elif head == "print":
            g = operand(t[1])

            def run(g=g, nxt=nxt):
                out.append(str(g()))
                return nxt

        elif head == "goto":
            target = labels[t[1].lower()]

            def run(target=target):
                return target

        else:  # a conditional jump: two values around a comparison, then a label
            _, x, name, y, _, label = t
            a, b, test = operand(x), operand(y), TESTS[name]
            target = labels[label.lower()]

            def run(a=a, b=b, test=test, target=target, nxt=nxt):
                return target if test(a(), b()) else nxt

        ops.append(run)
    values.extend([0] * len(names))
    assigned.extend([False] * len(names))
    pc = 0
    executed = 0
    size = len(ops)
    while 0 <= pc < size and executed < LIMIT:
        pc = ops[pc]()
        executed += 1
    if pc != END and executed == LIMIT:
        # ten million commands done and the program still runs
        out.append("Program terminated. Variables state:")
        out += ["%s: %d" % (n, values[k]) for n, k in sorted(names.items()) if assigned[k]]
    sys.stdout.write("".join(line + "\n" for line in out))


main()
