import os
from sys import stdout

power = int(open(0, "rb", buffering=0).read())
# The linear case and the smallest Pythagorean triple are the only cases.
# Fermat excludes powers above two, while a zeroth power makes the sum unequal to the third term.
if power == 1:
    print("1 2 3")
elif power == 2:
    print("3 4 5")
else:
    print(-1)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
