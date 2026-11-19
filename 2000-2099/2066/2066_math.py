import os
from sys import stdout

small, middle, large = sorted(map(int, open(0, "rb", buffering=0).read().split()))
# For non-negative sorted operands, only all-subtraction and subtracting
# the product of the two larger operands can attain the minimum.
print(min(small - middle - large, small - middle * large))

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
