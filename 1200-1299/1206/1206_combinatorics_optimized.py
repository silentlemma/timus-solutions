import os
import sys

FIRST = 36
OTHER = 55
length = int(sys.stdin.buffer.read())
print(FIRST * pow(OTHER, length - 1))

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
