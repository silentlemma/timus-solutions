import sys

MINUTES = 60
FIRST_HOUR = 7
WITH_LEONID = 13
ALREADY_IN = 42


def main():
    words = sys.stdin.read().split()
    n, m = int(words[0]), int(words[1])
    pos = 2
    place = []
    order = []
    for _ in range(m):
        stops = []
        while words[pos] != "-1":
            stops.append(int(words[pos]))
            pos += 1
        pos += 1
        order.append(stops)
        place.append({s: i for i, s in enumerate(stops)})
    k = int(words[pos])
    pos += 1
    buses = []
    for _ in range(k):
        hh, mm = words[pos].split(":")
        route = int(words[pos + 1]) - 1
        pos += 2
        # the minute this bus left the first stop of its route
        start = (int(hh) - FIRST_HOUR) * MINUTES + int(mm) - place[route][1]
        buses.append((start, route))
    chosen_start, chosen = buses[-1]

    def picked(src, dst):
        """Whether a passenger waiting at src for dst takes the chosen bus:
        no bus seen by Leonid serves the trip and comes to src sooner, or at
        the same minute reaching dst sooner, or as soon with a smaller route.
        Buses not seen at stop 1 either come to src later or need not run."""
        here = place[chosen]
        if src not in here or dst not in here or here[src] >= here[dst]:
            return False
        mine = (chosen_start + here[src], chosen_start + here[dst], chosen)
        for start, route in buses:
            there = place[route]
            if start < 0:
                continue
            if src in there and dst in there and there[src] < there[dst]:
                if (start + there[src], start + there[dst], route) < mine:
                    return False
        return True

    stops = order[chosen]
    one, two = place[chosen][1], place[chosen][2]
    early = stops[one + 1:two]
    late = stops[two:]
    leave_new = any(picked(1, d) for d in early)
    stay_new = any(picked(1, d) for d in late)
    leave_old = any(picked(s, d) for s in stops[:one] for d in early)
    stay_old = any(picked(s, d) for s in stops[:one] for d in late)
    # each group can all ride to a stop of one kind, so the counts are all or
    # nothing for the 13 who got on with Leonid and the 42 already inside
    low = WITH_LEONID * (not leave_new) + ALREADY_IN * (not leave_old)
    high = WITH_LEONID * stay_new + ALREADY_IN * stay_old
    print(low, high)


main()
