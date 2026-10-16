import sys

MOST = 100
# how many letters may be taken off each end before undoing a doubling
EDGE = 5
UNDO = str.maketrans("01", "10")


def main():
    word = sys.stdin.readline().strip()
    sys.setrecursionlimit(MOST * MOST)
    best = {}

    def plan(s):
        """The fewest phrases that build s, with the way to do it: either all
        letters one by one, or a few letters at each end around the double
        of a shorter word; a word free of these repeats always has that
        shape with short ends."""
        if s in best:
            return best[s]
        result = (len(s), None)
        for a in range(min(EDGE, len(s)) + 1):
            for b in range(min(EDGE, len(s) - a) + 1):
                core = s[a:len(s) - b]
                if len(core) < 2 or len(core) % 2:
                    continue
                if core[0::2].translate(UNDO) != core[1::2]:
                    continue
                cost = a + b + 1 + plan(core[0::2])[0]
                if cost < result[0]:
                    result = (cost, (a, b))
        best[s] = result
        return result

    def phrases(s, out):
        cost, cut = best[s] if s in best else plan(s)
        if cut is None:
            out.extend("back " + c for c in s)
            return
        a, b = cut
        core = s[a:len(s) - b]
        phrases(core[0::2], out)
        out.append("double")
        out.extend("front " + c for c in reversed(s[:a]))
        out.extend("back " + c for c in s[len(s) - b:])

    cost = plan(word)[0]
    if cost > MOST:
        print(-1)
        return
    out = []
    phrases(word, out)
    print(len(out))
    print("\n".join(out))


main()
