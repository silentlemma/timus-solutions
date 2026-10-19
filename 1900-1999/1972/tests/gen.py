"""Print seed nD for any dimension D=1..16 (modes n1,...,n16).
Seed encodes start*32 + Hamming distance; distance must be 1..D.
Large-output fixtures are generated even though their inputs are tiny.
"""
import sys


SEED_BASE = 32
MAX_DIMENSIONS = 16


def build(seed, mode):
    if not mode.startswith('n'):
        raise ValueError('Expected mode n1,...,n16')
    dimensions = int(mode[1:])
    start, distance = divmod(seed, SEED_BASE)
    if not 1 <= dimensions <= MAX_DIMENSIONS or not 1 <= distance <= dimensions:
        raise ValueError('Invalid dimension or Hamming distance')
    if not 0 <= start < 1 << dimensions:
        raise ValueError('Starting configuration outside cube')
    finish = start ^ ((1 << distance) - 1)
    lines = [str(dimensions)]
    for mask in (start, finish):
        enabled = [str(i + 1) for i in range(dimensions) if mask & (1 << i)]
        lines.append(' '.join([str(len(enabled)), *enabled]))
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    sys.stdout.write(build(int(sys.argv[1]), sys.argv[2]))
