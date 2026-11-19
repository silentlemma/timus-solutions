import os
from sys import stdout

tokens = open(0, "rb", buffering=0).read().split()
count = int(tokens[0])
prefix = tokens[count + 1]
answer = b"\n".join(word for word in tokens[1 : count + 1] if word.startswith(prefix))
if answer:
    stdout.buffer.write(answer + b"\n")

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
