from array import array
from os import _exit

INPUT_BLOCK = 512
OUTPUT_BLOCK = 128


def numbers():
    source = open(0, "rb", buffering=0)
    tail = b""
    while block := source.read(INPUT_BLOCK):
        parts = (tail + block).split()
        tail = parts.pop() if block[-1] > ord(" ") else b""
        yield from map(int, parts)
    if tail:
        yield int(tail)


def arrange(counts):
    total = sum(counts)
    largest = max(range(len(counts)), key=counts.__getitem__)
    answer = array("H", [largest + 1]) * total
    dominant = counts[largest] > (total + 1) // 2
    at = 2 * counts[largest] - total if dominant else 2 * counts[largest]
    if not dominant and at >= total:
        at = 1
    for kind, count in enumerate(counts):
        if kind == largest:
            continue
        if dominant:
            answer[at : at + 2 * count : 2] = array("H", [kind + 1]) * count
            at += 2 * count
        else:
            while count:
                take = min(count, (total - at + 1) // 2)
                answer[at : at + 2 * take : 2] = array("H", [kind + 1]) * take
                count -= take
                at += 2 * take
                if at >= total:
                    at = 1
    return answer


def main():
    values = numbers()
    next(values)
    counts = array("H", values)
    answer = arrange(counts)
    target = open(1, "wb", buffering=0)
    for first in range(0, len(answer), OUTPUT_BLOCK):
        target.write((" ".join(map(str, answer[first : first + OUTPUT_BLOCK])) + "\n").encode())
    _exit(0)


main()
