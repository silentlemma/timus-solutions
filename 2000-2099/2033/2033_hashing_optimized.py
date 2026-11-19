import os
from sys import stdout

RECORDS = 6
tokens = iter(open(0, "rb", buffering=0).read().split())
groups = {}
for _ in range(RECORDS):
    next(tokens)
    model, price = next(tokens), int(next(tokens))
    count, cheapest = groups.get(model, (0, price))
    groups[model] = count + 1, min(cheapest, price)
best = min(groups, key=lambda model: (-groups[model][0], groups[model][1], model))
stdout.buffer.write(best + b"\n")

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
