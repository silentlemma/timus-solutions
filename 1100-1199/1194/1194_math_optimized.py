import os
from sys import stdout

hobbits, couples = map(int, open(0, "rb", buffering=0).readline().split())
# Only the header affects the total, so leave the potentially long split log unread.
print(hobbits * (hobbits - 1) // 2 - couples)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
