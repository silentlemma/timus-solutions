import os
from sys import stdout

offer, increase, demand, decrease = map(int, open(0, "rb", buffering=0).read().split())
if offer >= demand:
    price = offer
else:
    # After this many full rounds, the next offer or reply reaches agreement.
    rounds = (demand - offer - 1) // (increase + decrease)
    price = min(offer + (rounds + 1) * increase, demand - rounds * decrease)
print(price)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
