import sys

DIM = 3
VERTICES = 4
FACES = ((0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 3, 1), (1, 2, 3, 0))  # a face and the vertex opposite


def main():
    data = [int(w) for w in sys.stdin.read().split()]
    points = [data[DIM * i:DIM * (i + 1)] for i in range(len(data) // DIM)]
    vertices = points[:VERTICES]
    n = data[DIM * VERTICES]
    rest = data[DIM * VERTICES + 1:]
    stars = [rest[DIM * i:DIM * (i + 1)] for i in range(n)]
    normals = []
    for i, j, k, opposite in FACES:
        a, b, c, d = vertices[i], vertices[j], vertices[k], vertices[opposite]
        u = [b[t] - a[t] for t in range(DIM)]
        v = [c[t] - a[t] for t in range(DIM)]
        cross = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]
        # point the cross product, twice the face area long, away from the body
        if sum(cross[t] * (d[t] - a[t]) for t in range(DIM)) > 0:
            cross = [-x for x in cross]
        normals.append(cross)
    # a lit face gives area * intensity * cosine = (cross . star) / 2, and the
    # doubled total is a plain integer sum; the body is convex, so no shadows
    total = sum(max(0, sum(x * s for x, s in zip(cross, star)))
                for cross in normals for star in stars)
    print("%d.00000" % total)


main()
