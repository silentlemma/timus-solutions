import os
from sys import stdout

PENALTY_PER_REJECTION = 20


values = map(int, open(0, "rb", buffering=0).read().split())
winner, runner_up = next(values), next(values)
print(
    "Dirty debug :(" if runner_up - PENALTY_PER_REJECTION * sum(values) < winner else "No chance."
)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
