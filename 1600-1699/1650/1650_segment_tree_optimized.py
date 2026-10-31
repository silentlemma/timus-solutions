import sys


def main():
    source = sys.stdin.buffer
    n = int(source.readline())
    ids, people, totals = {}, {}, []

    def city_id(name):
        if name not in ids:
            ids[name] = len(ids)
            totals.append(0)
        return ids[name]

    for _ in range(n):
        who, city, wealth = source.readline().split()
        city, wealth = city_id(city), int(wealth)
        people[who] = (city, wealth)
        totals[city] += wealth
    m, k = map(int, source.readline().split())
    # each move introduces at most one city; no move records need to be stored.
    size = 1
    while size < len(ids) + k:
        size *= 2
    # a max tree over cities: the best total and the one city that reaches it,
    # or minus one when several cities do
    best = [0] * (2 * size)
    where = [-1] * size + list(range(size))
    best[size : size + len(totals)] = totals
    days = [0] * size
    for i in range(size - 1, 0, -1):
        a, b = 2 * i, 2 * i + 1
        if best[a] == best[b]:
            best[i] = best[a]
        else:
            w = a if best[a] > best[b] else b
            best[i], where[i] = best[w], where[w]

    def add(city, amount):
        i = size + city
        best[i] += amount
        i //= 2
        while i:
            a, b = 2 * i, 2 * i + 1
            # minus one denotes a tie, replacing a full multiplicity array.
            value, winner = best[a], -1
            if best[a] != best[b]:
                w = a if best[a] > best[b] else b
                value, winner = best[w], where[w]
            # unchanged maxima and tie status cannot affect an ancestor.
            if value == best[i] and winner == where[i]:
                break
            best[i], where[i] = value, winner
            i //= 2

    today = 1
    for _ in range(k):
        day, who, city = source.readline().split()
        day = int(day)
        # a strict leader only; the moves of a day count from the next morning
        if where[1] >= 0:
            days[where[1]] += day + 1 - today
        today = day + 1
        origin, wealth = people[who]
        target = city_id(city)
        if target != origin:
            add(origin, -wealth)
            add(target, wealth)
            people[who] = (target, wealth)
    if where[1] >= 0:
        days[where[1]] += m + 1 - today
    sys.stdout.write(
        "".join(f"{name.decode()} {days[ids[name]]}\n" for name in sorted(ids) if days[ids[name]])
    )


main()
