import os
import sys

# This short standalone job trades JIT throughput for bounded startup memory.
try:
    import pypyjit
except ImportError:
    pass
else:
    pypyjit.set_param("off")

RIGHT = 62
LEFT = 60


header, row = sys.stdin.buffer.read().split(None, 1)
count = int(header)
seen = right = turns = 0
for character in row:
    if character == RIGHT:
        right += 1
        seen += 1
    elif character == LEFT:
        turns += right
        seen += 1
    if seen == count:
        break
print(turns)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
