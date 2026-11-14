from sys import stdin


PEG_A, PEG_B, PEG_C = b"ABC"
PEG_SUM = PEG_A + PEG_B + PEG_C

stdin.buffer.readline()
target = stdin.buffer.readline().rstrip()
source = PEG_A
moves = 0
for peg in reversed(target):
    moves <<= 1
    if peg != source:
        moves |= 1
        source = PEG_SUM - source - peg
print(moves)
