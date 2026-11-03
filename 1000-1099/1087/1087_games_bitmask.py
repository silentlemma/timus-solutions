stones, _ = map(int, input().split())
moves = list(map(int, input().split()))
# The always-legal-move promise forces the pile and all moves to be
# multiples of the smallest move: repeatedly taking that move proves it.
unit = min(moves)
stones //= unit
move_mask = 0
for take in moves:
    move_mask |= 1 << (take // unit)

remaining = (1 << (stones + 1)) - 2
target = 1 << stones
while remaining & target:
    # The first unclassified positive position is losing. Every allowed
    # move from that position marks a larger winning position in one shift.
    lowest = remaining & -remaining
    if lowest == target:
        print(2)
        break
    remaining ^= lowest
    remaining &= ~(move_mask << (lowest.bit_length() - 1))
else:
    print(1)
