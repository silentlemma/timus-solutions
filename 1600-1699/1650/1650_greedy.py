from heapq import heapify, heappop, heappush
from os import _exit, write
import sys

CITY_BITS = 16
CITY_MASK = (1 << CITY_BITS) - 1
REBUILD_FACTOR = 3
REBUILD_MARGIN = 1024


def packed_key(total, city):
    # At most n+k<=60000 cities: the low sixteen bits identify the city.
    return (-total << CITY_BITS) + city


def main():
    source = sys.stdin.buffer
    n = int(source.readline())
    ids, people, totals = {}, {}, []
    for _ in range(n):
        who, name, wealth = source.readline().split()
        if name not in ids:
            ids[name] = len(totals)
            totals.append(0)
        city, wealth = ids[name], int(wealth)
        people[who] = [city, wealth]
        totals[city] += wealth
    last_day, trips = map(int, source.readline().split())
    days = [0] * len(totals)
    frequency = {}
    for value in totals:
        frequency[value] = frequency.get(value, 0) + 1
    heap = [packed_key(value, city) for city, value in enumerate(totals)]
    heapify(heap)
    push, pop = heappush, heappop

    def add(city, delta):
        old = totals[city]
        frequency[old] -= 1
        if frequency[old] == 0:
            del frequency[old]
        value = old + delta
        totals[city] = value
        frequency[value] = frequency.get(value, 0) + 1
        push(heap, packed_key(value, city))

    def credit(length):
        if length == 0:
            return
        while True:
            key = heap[0]
            city, value = key & CITY_MASK, -(key >> CITY_BITS)
            if value == totals[city]:
                break
            pop(heap)
        # Count cities, not valid duplicate heap entries after a return trip.
        if frequency[value] == 1:
            days[city] += length

    today = 1
    for _ in range(trips):
        day, who, name = source.readline().split()
        day = int(day)
        credit(day + 1 - today)
        today = day + 1
        if name not in ids:
            city = ids[name] = len(totals)
            totals.append(0)
            days.append(0)
            frequency[0] = frequency.get(0, 0) + 1
            push(heap, city)
        person = people[who]
        origin, wealth = person
        target = ids[name]
        if target != origin:
            add(origin, -wealth)
            add(target, wealth)
            person[0] = target
        if len(heap) > REBUILD_FACTOR * len(totals) + REBUILD_MARGIN:
            heap = [packed_key(value, city) for city, value in enumerate(totals)]
            heapify(heap)
    credit(last_day + 1 - today)
    answer = b"".join(
        name + b" " + str(days[ids[name]]).encode() + b"\n"
        for name in sorted(ids)
        if days[ids[name]]
    )
    view = memoryview(answer)
    offset = 0
    while offset < len(view):
        offset += write(1, view[offset:])
    _exit(0)


main()
