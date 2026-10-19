"""Usage: gen.py SEED MODE; modes: random,max_even,max_odd."""
import random
import sys

seed=int(sys.argv[1])
mode=sys.argv[2]
if mode=='random':
    print(random.Random(seed).randint(4,100000))
elif mode=='max_even':
    print(100000)
elif mode=='max_odd':
    print(99999)
else:
    raise ValueError(mode)
