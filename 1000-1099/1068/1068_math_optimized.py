import os
from sys import stdout

last = int(open(0, "rb", buffering=0).read())
print((1 + last) * (abs(last - 1) + 1) // 2)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
