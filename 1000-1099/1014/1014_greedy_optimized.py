import os
from sys import stdout

BASE = 10
value = int(open(0, "rb", buffering=0).read())
if value == 0:
    answer = str(BASE)
elif value == 1:
    answer = "1"
else:
    digits = []
    for digit in range(BASE - 1, 1, -1):
        while value % digit == 0:
            digits.append(str(digit))
            value //= digit
    answer = "".join(reversed(digits)) if value == 1 else "-1"
print(answer)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
