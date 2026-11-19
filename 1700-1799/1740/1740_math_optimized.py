import os
import sys

length, period, hours = map(int, sys.stdin.buffer.read().split())
whole, rest = divmod(length, period)
# Both extrema are integers; decimal formatting need not allocate floats.
print(whole * hours, (whole + bool(rest)) * hours)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
