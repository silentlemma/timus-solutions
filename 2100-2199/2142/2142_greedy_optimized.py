import os
import sys

red, blue, dual, need_red, need_blue, neutral = map(int, sys.stdin.buffer.read().split())
missing = max(0, need_red - red) + max(0, need_blue - blue)
if missing <= dual and red + blue + dual >= need_red + need_blue + neutral:
    print("It is a kind of magic")
else:
    print("There are no miracles in life")

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
