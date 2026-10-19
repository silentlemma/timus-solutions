import sys
from array import array
from bisect import bisect_right

FIELDS = 6
PERCENT = 100
SOURCE, TARGET, DEPARTURE, DURATION, PROBABILITY, DELAY = range(FIELDS)


def main():
    data = array('I')
    for line in sys.stdin.buffer.read().splitlines():
        data.extend(map(int, line.split()))
    n, m = data[:2]
    source = data[2 + SOURCE::FIELDS]
    target = data[2 + TARGET::FIELDS]
    departure = data[2 + DEPARTURE::FIELDS]
    duration = data[2 + DURATION::FIELDS]
    probability = data[2 + PROBABILITY::FIELDS]
    delay = data[2 + DELAY::FIELDS]
    del data

    # Each airport owns a contiguous slice of the departure and DP arrays.
    begin = array('I', [0]) * (n + 2)
    for a in source:
        begin[a + 1] += 1
    for a in range(1, n + 1):
        begin[a + 1] += begin[a]
    end = begin[:]
    late = array('i', [0]) * m
    infinity = float("inf")
    best = array('d', [infinity]) * m

    # Later departures are processed first, so all connections are ready.
    order = sorted(range(m), key=departure.__getitem__, reverse=True)
    for i in order:
        a, b = source[i], target[i]
        t = departure[i]
        arrival = t + duration[i]
        delayed_arrival = arrival + delay[i]
        if b == n:
            on_time, delayed = arrival, delayed_arrival
        else:
            left, right = begin[b], end[b]
            k = bisect_right(late, -delayed_arrival, left, right) - 1
            if k < left:
                continue
            delayed = best[k]
            k = bisect_right(late, -arrival, k, right) - 1
            on_time = best[k]
        p = probability[i]
        value = ((PERCENT - p) * on_time + p * delayed) / PERCENT
        pos = end[a]
        # A later flight with no worse expectation dominates this departure.
        if pos > begin[a] and best[pos - 1] <= value:
            continue
        late[pos] = -t
        best[pos] = value
        end[a] = pos + 1
    answer = best[end[1] - 1] if end[1] > begin[1] else infinity
    print("Fail" if answer == infinity else "%.6f" % answer)


main()
