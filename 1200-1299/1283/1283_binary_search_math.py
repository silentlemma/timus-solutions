import os
import sys

PERCENT = 100

gold, limit, fee = map(int, sys.stdin.buffer.read().split())
if gold <= limit:
    answer = 0
else:
    numerator = PERCENT - fee
    upper = 1
    # Exponential search brackets the first successful exact integer comparison.
    while gold * pow(numerator, upper) > limit * pow(PERCENT, upper):
        upper *= 2
    lower = upper // 2
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if gold * pow(numerator, middle) > limit * pow(PERCENT, middle):
            lower = middle
        else:
            upper = middle
    answer = upper
print(answer)
sys.stdout.flush()
os._exit(0)
