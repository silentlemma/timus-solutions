import sys

# times in units of 1/50 s: a car (20 km/h) covers a metre in 9 units and
# Egor (5 km/h) crosses a 2 m lane in 72
METRE = 9
LANE = 72
CAR = 5
UNITS = 50


def main():
    words = iter(sys.stdin.read().split())
    blocked = []
    # a car is on the crossing from METRE d to METRE (d + CAR); a start time
    # s is bad when Egor's time in the car's lane overlaps that
    for lane in range(2):
        for _ in range(int(next(words))):
            d = int(next(words))
            enter = lane * LANE
            blocked.append((METRE * d - enter - LANE, METRE * (d + CAR) - enter))
    blocked.sort()
    start = 0
    for low, high in blocked:
        if low >= start:
            break
        start = max(start, high)
    print("%.6f" % (start / UNITS))


main()
