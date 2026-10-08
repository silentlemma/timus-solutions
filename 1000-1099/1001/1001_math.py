import math
import sys

nums = sys.stdin.buffer.read().split()
out = ["%.4f" % math.sqrt(int(x)) for x in reversed(nums)]
sys.stdout.write("\n".join(out) + ("\n" if out else ""))
