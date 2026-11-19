import os
from sys import stdout

tokens = open(0, "rb", buffering=0).read().split()
count = int(tokens[0])
print("%.6f" % (sum(map(int, tokens[1 : count + 1])) / count))

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
