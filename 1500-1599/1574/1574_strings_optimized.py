import os
import sys

OPEN_BRACKET = 40


balance = lowest = count = 0
# Count minimum-height prefixes online rather than retaining every prefix sum.
for bracket in sys.stdin.buffer.read().strip():
    balance += 1 if bracket == OPEN_BRACKET else -1
    if balance < lowest:
        lowest, count = balance, 1
    elif balance == lowest:
        count += 1
print(count if balance == 0 else 0)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
