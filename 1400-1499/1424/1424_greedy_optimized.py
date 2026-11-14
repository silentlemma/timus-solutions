from array import array
from heapq import heappop, heappush
from sys import stdin, stdout

ID_BITS = 16
ID_MASK = (1 << ID_BITS) - 1
BLOCK_SIZE = 1 << 14
OUTPUT_BATCH = 1024


def numbers():
    pending = b""
    while block := stdin.buffer.read(BLOCK_SIZE):
        tokens = (pending + block).split()
        pending = tokens.pop() if tokens and not block[-1:].isspace() else b""
        yield from map(int, tokens)
    if pending:
        yield int(pending)


def main():
    values = numbers()
    stops, capacity = next(values), next(values)
    requests, price = next(values), next(values)
    starts = array("H", [0]) * (stops + 1)
    ends = array("H", [0]) * (stops + 1)
    following = array("H", [0]) * (requests + 1)
    finish = array("I", [0]) * (requests + 1)
    for passenger in range(1, requests + 1):
        start, finish[passenger] = next(values), next(values)
        following[passenger], starts[start] = starts[start], passenger

    taken = bytearray(requests + 1)
    heap = []
    riding = 0
    for stop, passenger in enumerate(starts):
        riding -= ends[stop]
        while passenger:
            end = finish[passenger]
            taken[passenger] = 1
            ends[end] += 1
            riding += 1
            # Pack the destination and passenger number into one heap key.
            heappush(heap, -((end << ID_BITS) | passenger))
            if riding > capacity:
                drop = -heappop(heap)
                taken[drop & ID_MASK] = 0
                ends[drop >> ID_BITS] -= 1
                riding -= 1
            passenger = following[passenger]

    stdout.write(f"{sum(taken) * price}\n")
    batch = []
    for passenger, selected in enumerate(taken):
        if selected:
            batch.append(str(passenger))
            if len(batch) == OUTPUT_BATCH:
                stdout.write(" ".join(batch) + " ")
                batch.clear()
    stdout.write(" ".join(batch) + "\n")


if __name__ == "__main__":
    main()
