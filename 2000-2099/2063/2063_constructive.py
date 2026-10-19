import sys

# FNV-1a of the whole input seeds splitmix64; the arrangements are never
# decoded, they only make the seed differ between tests
FNV_OFFSET = 0xCBF29CE484222325
FNV_PRIME = 0x100000001B3
GOLDEN = 0x9E3779B97F4A7C15
MIX_A = 0xBF58476D1CE4E5B9
MIX_B = 0x94D049BB133111EB
SHIFT_A = 30
SHIFT_B = 27
SHIFT_C = 31
MASK = (1 << 64) - 1


def main():
    data = sys.stdin.buffer.read()
    state = FNV_OFFSET
    for c in data:
        state = ((state ^ c) * FNV_PRIME) & MASK
    games = int(data.split()[0])
    out = []
    for game in range(games):
        n = game + 2
        # a bubble sort network: every white ball ends left of every black one
        step = ["? %d %d" % (i, i + 1) for i in range(1, n)]
        for end in range(n - 1, 0, -1):
            out.extend(step[:end])
        state = (state + GOLDEN) & MASK
        z = state
        z = ((z ^ (z >> SHIFT_A)) * MIX_A) & MASK
        z = ((z ^ (z >> SHIFT_B)) * MIX_B) & MASK
        z ^= z >> SHIFT_C
        j = 1 + z % (n - 1)
        out.append("! %d %d" % (j, j + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
