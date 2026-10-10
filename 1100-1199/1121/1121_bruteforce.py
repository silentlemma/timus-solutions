import sys

REACH = 5


def main():
    tok = iter(map(int, sys.stdin.buffer.read().split()))
    h, w = next(tok), next(tok)
    grid = [[next(tok) for _ in range(w)] for _ in range(h)]
    # the cells at each distance 1..5, as offsets around a crossing
    rings = [
        [(dr, dc) for dr in range(-d, d + 1) for dc in range(-d, d + 1) if abs(dr) + abs(dc) == d]
        for d in range(1, REACH + 1)
    ]
    out = []
    for r in range(h):
        row = []
        for c in range(w):
            if grid[r][c]:
                row.append(-1)
                continue
            found = 0
            for ring in rings:
                for dr, dc in ring:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < h and 0 <= cc < w:
                        # each type counts once however many branches share it
                        found |= grid[rr][cc]
                if found:
                    break
            row.append(found)
        out.append(" ".join(map(str, row)))
    print("\n".join(out))


main()
