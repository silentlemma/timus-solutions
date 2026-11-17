import sys

words = (int(word) for line in sys.stdin.buffer for word in line.split())
common = {next(words) for _ in range(next(words))}
for _ in range(2):
    own = [next(words) for _ in range(next(words))]
    common.intersection_update(own)
print(len(common))
