import sys

DECIMAL_BASE = 10

sys.set_int_max_str_digits(0)
n = int(sys.stdin.read())
unit = DECIMAL_BASE**n
first = unit // DECIMAL_BASE
# Direct exact counting over B=k*A; no special cases or precomputed prefixes.
print(sum(unit // k - first for k in range(1, DECIMAL_BASE) if unit % k == 0))
