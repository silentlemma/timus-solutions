import math
import sys

EPS = 1e-9
FIELDS = 4


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    ghosts = [data[1 + FIELDS * i : 1 + FIELDS * (i + 1)] for i in range(n)]
    xs, ys, zs, rs = ([g[t] for g in ghosts] for t in range(FIELDS))
    # a ray along d touches ghost i when d.C_i >= L_i |d|, where L_i is the
    # length of a tangent from the gun: L_i^2 = |C_i|^2 - R_i^2
    norm = [x * x + y * y + z * z for x, y, z in zip(xs, ys, zs)]
    tan2 = [m - r * r for m, r in zip(norm, rs)]
    tan = [math.sqrt(a) for a in tan2]
    dot = [[xs[i] * xs[k] + ys[i] * ys[k] + zs[i] * zs[k] for k in range(n)] for i in range(n)]
    best = []
    # the ray through the centre of ghost i, tested exactly in integers
    for i in range(n):
        hit = [k for k in range(n) if dot[i][k] * dot[i][k] >= tan2[k] * norm[i]]
        if len(hit) > len(best):
            best = hit
    # rays touching two ghosts i and j: d = (a C_i + b C_j + c C_i x C_j) / det
    for i in range(n):
        for j in range(i + 1, n):
            g = dot[i][j]
            det = norm[i] * norm[j] - g * g
            if det == 0:
                continue
            # 1 - |a C_i + b C_j|^2 = Q / det with Q = base + 2 g L_i L_j
            base = det - tan2[i] * norm[j] - tan2[j] * norm[i]
            p = tan2[i] * tan2[j]
            if base < 0 and (2 * g) ** 2 * p < base * base:
                continue  # the two outlines do not meet
            root = math.sqrt(p)
            if base >= 0:
                q = base + 2 * g * root
            else:
                q = ((2 * g) ** 2 * p - base * base) / (2 * g * root - base)
            # a det and b det, rationalised to avoid cancellation
            ad = (tan2[i] * norm[j] ** 2 - tan2[j] * g * g) / (tan[i] * norm[j] + tan[j] * g)
            bd = (tan2[j] * norm[i] ** 2 - tan2[i] * g * g) / (tan[j] * norm[i] + tan[i] * g)
            cx = ys[i] * zs[j] - zs[i] * ys[j]
            cy = zs[i] * xs[j] - xs[i] * zs[j]
            cz = xs[i] * ys[j] - ys[i] * xs[j]
            sq = math.sqrt(q)
            di, dj = dot[i], dot[j]
            for sign in (1, -1) if q > 0 else (1,):
                s = sign * sq
                hit = [
                    k
                    for k in range(n)
                    if k == i
                    or k == j
                    or ad * di[k] + bd * dj[k] + s * (cx * xs[k] + cy * ys[k] + cz * zs[k])
                    >= det * tan[k] * (1 - EPS)
                ]
                if len(hit) > len(best):
                    best = hit
    print(len(best))
    print(" ".join(str(k + 1) for k in best))


main()
