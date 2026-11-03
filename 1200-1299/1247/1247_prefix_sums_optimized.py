from itertools import accumulate, count, islice, repeat
from operator import floordiv, sub
from sys import stdin

stream = stdin.buffer
size, limit = map(int, stream.readline().split())
prefix = map(sub, accumulate(map(int, islice(stream, size))), count(1))
# An integer p has p//(N+1)==0 exactly when 0<=p<=N, even for negative p.
outside = map(floordiv, prefix, repeat(limit + 1))
print("NO" if any(outside) else "YES")
