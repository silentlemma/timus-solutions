DIRECT = (
    (0, 1, b"AB-\n"),
    (1, 2, b"BC-\n"),
    (2, 3, b"CD-\n"),
    (3, 0, b"DA-\n"),
    (4, 5, b"EF-\n"),
    (5, 6, b"FG-\n"),
    (6, 7, b"GH-\n"),
    (7, 4, b"HE-\n"),
    (0, 4, b"AE-\n"),
    (1, 5, b"BF-\n"),
    (2, 6, b"CG-\n"),
    (3, 7, b"DH-\n"),
)
OPPOSITE = (
    (0, b"BC+\nAB-\nCG-\n"),
    (2, b"BA+\nCB-\nAE-\n"),
    (5, b"EA+\nFE-\nAD-\n"),
    (7, b"DC+\nHD-\nCB-\n"),
)

counts = list(map(int, open(0, "rb", buffering=0).readall().split()))
if 2 * sum(counts[u] for u, _ in OPPOSITE) == sum(counts):
    blocks = []
    for u, v, operation in DIRECT:
        pairs = min(counts[u], counts[v])
        if pairs:
            counts[u] -= pairs
            counts[v] -= pairs
            blocks.append(operation * pairs)
    # Once every adjacent pair has been cleared, at most one opposite pair remains.
    for u, operations in OPPOSITE:
        if counts[u]:
            blocks.append(operations * counts[u])
            break
    open(1, "wb", buffering=0).write(b"".join(blocks) or b"\n")
else:
    print("IMPOSSIBLE")
