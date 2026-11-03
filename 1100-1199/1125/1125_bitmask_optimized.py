import sys

COLOUR_XOR = ord("W") ^ ord("B")


def main():
    stream = sys.stdin.buffer
    m, n = map(int, stream.readline().split())
    if m == 0 or n == 0:
        sys.stdout.write("\n" * m)
        return
    final = [bytearray(stream.readline().strip()) for _ in range(m)]
    odd = []
    columns = 0
    for _ in range(m):
        row = sum((int(value) & 1) << c for c, value in enumerate(stream.readline().split()))
        odd.append(row)
        columns ^= row
    squares = {k * k for k in range(m + n)}
    offsets = [(dr, dc) for dr in range(1, m) for dc in range(1, n) if dr * dr + dc * dc in squares]
    full = (1 << n) - 1
    for r in range(m):
        # Row and column count the origin twice; own row restores it once.
        flips = columns ^ odd[r] ^ (full if odd[r].bit_count() & 1 else 0)
        for dr, dc in offsets:
            combined = (odd[r - dr] if r >= dr else 0) ^ (odd[r + dr] if r + dr < m else 0)
            flips ^= (combined << dc) ^ (combined >> dc)
        flips &= full
        while flips:
            bit = flips & -flips
            final[r][bit.bit_length() - 1] ^= COLOUR_XOR
            flips -= bit
    sys.stdout.write("\n".join(row.decode() for row in final) + "\n")


main()
