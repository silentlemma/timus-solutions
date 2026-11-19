import os
import sys

THREE = 3
FOUR = 4
heads = int(sys.stdin.buffer.read())
if heads < FOUR:
    answer = heads
else:
    threes, remainder = divmod(heads, THREE)
    if remainder == 1:
        threes, remainder = threes - 1, FOUR
    answer = pow(THREE, threes) * max(remainder, 1)
print(answer)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
