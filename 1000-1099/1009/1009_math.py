from os import _exit, write

DIGIT_BITS = 36
BASE = 1 << DIGIT_BITS
length, radix = map(int, open(0, "rb", buffering=0).read().split())
choices = radix - 1
# The legal N+K<=18 domain bounds the next coefficient below a base digit.
encoded = (1 << (DIGIT_BITS * (length + 2))) // (BASE * BASE - choices * BASE - choices)
answer = encoded & (BASE - 1)
write(1, (str(answer) + "\n").encode())
_exit(0)
