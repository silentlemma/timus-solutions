import sys

DAY = 1440
HOUR = 60
FIELDS = 3  # flights, delay and flight time


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pos = 1
    now = 0
    for _ in range(n - 1):
        q, delay, flight = (int(w) for w in data[pos : pos + FIELDS])
        pos += FIELDS
        best = None
        for word in data[pos : pos + q]:
            hours, minutes = word.split(":")
            leave = int(hours) * HOUR + int(minutes) + delay
            if leave < now:  # the same flight on a later day
                leave += (now - leave + DAY - 1) // DAY * DAY
            if best is None or leave < best:
                best = leave
        pos += q
        now = best + flight
    print(now)


main()
