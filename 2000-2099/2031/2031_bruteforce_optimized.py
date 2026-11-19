import os
from sys import stdout

BASE = 10
LIMIT = BASE * BASE - 1
# The statement specifies how each digit looks upside down.
TURN = "01????9?86"
count = int(open(0, "rb", buffering=0).read())
run = 0
for value in range(1, LIMIT + 1):
    run = run + 1 if TURN[value // BASE] != "?" and TURN[value % BASE] != "?" else 0
    if run >= count:
        print(" ".join(TURN[x % BASE] + TURN[x // BASE] for x in range(value, value - count, -1)))
        break
else:
    print("Glupenky Pierre")

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
