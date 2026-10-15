import sys

FIELDS = 3  # name, city, wealth


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    people = data[1 : 1 + FIELDS * n]
    pos = 1 + FIELDS * n
    m, k = int(data[pos]), int(data[pos + 1])
    moves = data[pos + 2 : pos + 2 + FIELDS * k]
    city_id = {}
    for name in people[1::FIELDS] + moves[2::FIELDS]:
        city_id.setdefault(name, len(city_id))
    size = 1
    while size < len(city_id):
        size *= 2
    # a max tree over cities: the best total, how many leaves reach it,
    # and one of them
    best = [0] * (2 * size)
    count = [1] * size + [1] * size
    where = list(range(-size, 0)) + list(range(size))
    for i in range(size - 1, 0, -1):
        count[i] = count[2 * i] + count[2 * i + 1]
        where[i] = where[2 * i]

    def add(city, amount):
        i = city + size
        best[i] += amount
        i //= 2
        while i:
            a, b = 2 * i, 2 * i + 1
            if best[a] > best[b]:
                best[i], count[i], where[i] = best[a], count[a], where[a]
            elif best[a] < best[b]:
                best[i], count[i], where[i] = best[b], count[b], where[b]
            else:
                best[i], count[i], where[i] = best[a], count[a] + count[b], where[a]
            i //= 2

    home, wealth = {}, {}
    for i in range(n):
        name, city, money = people[FIELDS * i : FIELDS * (i + 1)]
        home[name], wealth[name] = city_id[city], int(money)
        add(city_id[city], int(money))
    days = {}

    def lead(span):
        if span > 0 and count[1] == 1:  # a strict leader only
            days[where[1]] = days.get(where[1], 0) + span

    today = 1
    for i in range(k):
        day, name, city = moves[FIELDS * i : FIELDS * (i + 1)]
        day = int(day)
        # the moves of a day count from the next morning
        lead(day + 1 - today)
        today = max(today, day + 1)
        add(home[name], -wealth[name])
        home[name] = city_id[city]
        add(home[name], wealth[name])
    lead(m + 1 - today)
    names = {v: c for c, v in city_id.items()}
    out = sorted((names[c], d) for c, d in days.items())
    sys.stdout.write("".join("%s %d\n" % (c.decode(), d) for c, d in out))


main()
