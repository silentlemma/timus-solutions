import os
from sys import stdout

READ_CHUNK = 4096
count = int(open(0, "rb", buffering=0).read())
answer = bytearray()
first = True


def city(value):
    global first
    if not first:
        answer.append(ord(" "))
    first = False
    answer.extend(str(value).encode())
    if len(answer) >= READ_CHUNK:
        stdout.buffer.write(answer)
        answer.clear()


# Stream both alternating sides of the cheapest cycle, then the dearest cycle.
pairs = (count - 1) // 2
city(1)
city(count)
for step in range(1, pairs + 1):
    city(step + 1 if step % 2 else count - step)
middle = (count // 2) | 1
if count % 2 == 0 and middle != 1:
    city(middle)
for step in range(pairs, 1, -1):
    city(step if step % 2 else count - step + 1)
answer.append(ord("\n"))
first = True
for value in range(1, count + 1, 2):
    city(value)
for value in range(count - count % 2, 1, -2):
    city(value)
answer.append(ord("\n"))
stdout.buffer.write(answer)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
