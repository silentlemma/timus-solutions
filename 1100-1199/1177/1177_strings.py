import sys

QUOTE = ord("'")
STAR, ANY, DASH, OPEN, CLOSE, NOT = (ord(c) for c in "%_-[]^")


def quoted(line, p):
    # the text between quotes starting at p, with doubled quotes undone
    out = bytearray()
    p += 1
    while p < len(line):
        if line[p] == QUOTE:
            if p + 1 < len(line) and line[p + 1] == QUOTE:
                out.append(QUOTE)
                p += 2
                continue
            return bytes(out), p + 1
        out.append(line[p])
        p += 1
    return bytes(out), p


def elements(pattern):
    # %, _, a literal byte, or a set (negated, accepted bytes); a [ with no
    # closing ] can never match, which None stands for
    m, j = len(pattern), 0
    while j < m:
        c = pattern[j]
        if c == OPEN:
            k = j + 1
            negated = k < m and pattern[k] == NOT
            k += negated
            accepted = set()
            while k < m and pattern[k] != CLOSE:
                if k + 2 < m and pattern[k + 1] == DASH and pattern[k + 2] != CLOSE:
                    accepted.update(range(pattern[k], pattern[k + 2] + 1))
                    k += len(b"a-b")
                else:
                    accepted.add(pattern[k])
                    k += 1
            if k == m:
                yield None
                return
            yield negated, accepted
            j = k + 1
        else:
            yield c
            j += 1


def like(text, pattern):
    # bit i of reach: the pattern so far can match exactly text[:i]
    n = len(text)
    full = (1 << (n + 1)) - 1
    at = {}
    for i, c in enumerate(text):
        at[c] = at.get(c, 0) | 1 << i
    reach = 1
    for e in elements(pattern):
        if e is None:
            return False
        if e == STAR:
            reach = full & ~((reach & -reach) - 1) if reach else 0
        elif e == ANY:
            reach = reach << 1 & full
        elif isinstance(e, tuple):
            negated, accepted = e
            good = 0
            for c, mask in at.items():
                if (c in accepted) != negated:
                    good |= mask
            reach = (reach & good) << 1
        else:
            reach = (reach & at.get(e, 0)) << 1
        if not reach:
            return False
    return bool(reach >> n & 1)


def main():
    lines = sys.stdin.buffer.read().split(b"\n")
    n = int(lines[0])
    out = []
    for line in lines[1 : n + 1]:
        line = line.rstrip(b"\r")
        text, p = quoted(line, line.index(b"'"))
        pattern, _ = quoted(line, line.index(b"'", p))
        out.append("YES" if like(text, pattern) else "NO")
    print("\n".join(out))


main()
