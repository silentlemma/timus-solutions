import os
from sys import stdout

LARGEST = 10
ways = [1]
for count in range(1, LARGEST + 1):
    total, choose = 0, 1
    for tied in range(1, count + 1):
        choose = choose * (count - tied + 1) // tied
        total += choose * ways[count - tied]
    ways.append(total)
answers = []
for token in open(0, "rb", buffering=0).read().split():
    count = int(token)
    if count < 0:
        break
    answers.append(str(ways[count]))
if answers:
    print("\n".join(answers))

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
