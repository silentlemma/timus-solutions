import sys

LIMIT = 10**6


def main():
    data = sys.stdin.buffer.read().replace(b"\r", b"").decode()
    first, rest = data.split("\n", 1)
    n = int(first)
    # a template runs from the start of a line to its '#'
    text = [""]
    for _ in range(n):
        end = rest.index("#")
        text.append(rest[:end])
        rest = rest[end + 1 :]
        if rest.startswith("\n"):
            rest = rest[1:]
    # pieces of each template: plain text and template numbers
    pieces = [[]]
    for t in text[1:]:
        parts = t.split("*")
        row = [parts[0]]
        for p in parts[1:]:
            row += [int(p[0]), p[1:]]
        pieces.append(row)
    # size: the fully expanded length, capped above the limit; state 1
    # marks templates being expanded, so meeting one again is a cycle
    size, state = [0] * (n + 1), [0] * (n + 1)

    def measure(i):
        state[i] = 1
        for p in pieces[i]:
            if isinstance(p, str):
                size[i] += len(p)
            elif state[p] == 1 or state[p] == 0 and not measure(p):
                return False
            else:
                size[i] += size[p]
            size[i] = min(size[i], LIMIT + 1)
        state[i] = 2
        return True

    if not measure(1) or size[1] > LIMIT:
        print("#")
        return
    done = {}

    def build(i):
        if i not in done:
            done[i] = "".join(p if isinstance(p, str) else build(p) for p in pieces[i])
        return done[i]

    sys.stdout.write(build(1) + "\n")


main()
