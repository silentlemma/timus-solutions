import os
import sys

length = int(sys.stdin.buffer.read())
# ceil(log2 n) is the optimal fold count; no output list is needed to count it.
print((length - 1).bit_length())
folds = []
while length > 1:
    folded = length // 2
    folds.append(str(folded))
    length -= folded
print(" ".join(folds))

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
