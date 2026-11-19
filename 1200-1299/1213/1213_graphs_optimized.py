import os
from sys import stdout

with open(0) as source:
    tokens = (word for line in source for word in line.split())
    names = {next(tokens)}
    for partition in tokens:
        if partition == "#":
            break
        left, right = partition.split("-")
        names.add(left)
        names.add(right)
print(len(names) - 1)

# Finish the standalone answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
