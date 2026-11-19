import os
from sys import stdout

SWARM_MINIMUM = 250
THRONG_MINIMUM = 100
HORDE_MINIMUM = 50
LOTS_MINIMUM = 20
SEVERAL_MINIMUM = 5


LEGION_MIN = 1000
ZOUNDS_MIN = 500

count = int(open(0, "rb", buffering=0).read())
if count >= LEGION_MIN:
    word = "legion"
elif count >= ZOUNDS_MIN:
    word = "zounds"
elif count >= SWARM_MINIMUM:
    word = "swarm"
elif count >= THRONG_MINIMUM:
    word = "throng"
elif count >= HORDE_MINIMUM:
    word = "horde"
elif count >= LOTS_MINIMUM:
    word = "lots"
elif count >= 10:
    word = "pack"
elif count >= SEVERAL_MINIMUM:
    word = "several"
else:
    word = "few"
print(word)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
