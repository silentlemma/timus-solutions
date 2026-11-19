import os
import sys

value = int(sys.stdin.buffer.read())
print(value * value, value, sep="\n")

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
