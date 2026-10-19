"""Usage: gen.py SEED N; emits the size N, with1<=N<=100."""
import sys

size=int(sys.argv[2])
assert 1<=size<=100
print(size)
