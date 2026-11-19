import os
from sys import stdout

WEIGHT_VALUES = 101
GROUP_SIZE = 4


MIN_DIAMETER = 600
values = map(int, open(0, "rb", buffering=0).read().split())
count = next(values)
frequencies = [0] * WEIGHT_VALUES
for _ in range(count):
    frequencies[next(values) - MIN_DIAMETER] += 1
print(sum(frequency // GROUP_SIZE for frequency in frequencies))

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
