import os
from sys import stdout

source = open(0, encoding="utf8")
minimum, maximum = map(int, source.readline().split())
text = source.readline().rstrip("\r\n")
position = messages = 0
while position < len(text):
    end = position
    limit = min(len(text), position + maximum)
    while end < limit and (text[end].isalpha() or text[end] == " "):
        end += 1
    # Scanned letters belong to this message, so the lookahead is never repeated.
    position += max(minimum, end - position)
    messages += 1
print(messages)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
