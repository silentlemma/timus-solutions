from array import array
import sys

ALPHABET_SIZE = 26
FIRST_LETTER = ord("a")
TARGET_PARTS = 5
UNREACHABLE = TARGET_PARTS + 1
ODD_ROOT = 0
EMPTY_ROOT = 1
OUTER_SPLIT = 3


def partition(text):
    size = len(text)
    capacity = size + 2
    data = b"\0" + text
    edges = array("I", [0]) * (capacity * ALPHABET_SIZE)
    lengths = array("i", [0]) * capacity
    links = array("I", [0]) * capacity
    differences = array("I", [0]) * capacity
    series = array("I", [0]) * capacity
    lengths[ODD_ROOT] = -1
    best_even = bytearray([UNREACHABLE]) * (size + 1)
    best_odd = bytearray([UNREACHABLE]) * (size + 1)
    best_even[0] = 0
    previous_even = array("I", [0]) * (size + 1)
    previous_odd = array("I", [0]) * (size + 1)
    group_even = bytearray([UNREACHABLE]) * capacity
    group_odd = bytearray([UNREACHABLE]) * capacity
    start_even = array("I", [0]) * capacity
    start_odd = array("I", [0]) * capacity
    nodes = 2
    last = EMPTY_ROOT
    for position in range(1, size + 1):
        letter = data[position]
        code = letter - FIRST_LETTER
        current = last
        while data[position - lengths[current] - 1] != letter:
            current = links[current]
        slot = current * ALPHABET_SIZE + code
        following = edges[slot]
        if following == 0:
            following = nodes
            nodes += 1
            edges[slot] = following
            lengths[following] = lengths[current] + 2
            if lengths[following] == 1:
                links[following] = EMPTY_ROOT
            else:
                suffix = links[current]
                while data[position - lengths[suffix] - 1] != letter:
                    suffix = links[suffix]
                links[following] = edges[suffix * ALPHABET_SIZE + code]
            suffix = links[following]
            differences[following] = lengths[following] - lengths[suffix]
            series[following] = (
                series[suffix]
                if differences[following] == differences[suffix]
                else suffix
            )
        last = following
        current = last
        while lengths[current] > 0:
            base = position - lengths[series[current]] - differences[current]
            group_even[current] = best_even[base]
            group_odd[current] = best_odd[base]
            start_even[current] = start_odd[current] = base
            suffix = links[current]
            if differences[current] == differences[suffix]:
                if group_even[suffix] < group_even[current]:
                    group_even[current] = group_even[suffix]
                    start_even[current] = start_even[suffix]
                if group_odd[suffix] < group_odd[current]:
                    group_odd[current] = group_odd[suffix]
                    start_odd[current] = start_odd[suffix]
            candidate = group_even[current] + 1
            if candidate < best_odd[position]:
                best_odd[position] = candidate
                previous_odd[position] = start_even[current]
            candidate = group_odd[current] + 1
            if candidate < best_even[position]:
                best_even[position] = candidate
                previous_even[position] = start_odd[current]
            current = series[current]
    if best_odd[size] > TARGET_PARTS:
        return None
    result = []
    position = size
    parity = 1
    while position:
        before = previous_odd[position] if parity else previous_even[position]
        result.append(text[before:position])
        position = before
        parity ^= 1
    result.reverse()
    while len(result) < TARGET_PARTS:
        long = next(
            (i for i, part in enumerate(result) if len(part) >= OUTER_SPLIT), None
        )
        if long is not None:
            part = result[long]
            result[long : long + 1] = [part[:1], part[1:-1], part[-1:]]
        else:
            doubles = [i for i, part in enumerate(result) if len(part) == 2]
            for index in reversed(doubles[:2]):
                part = result[index]
                result[index : index + 1] = [part[:1], part[1:]]
    return result


def main():
    result = partition(sys.stdin.buffer.read().strip())
    if result is None:
        sys.stdout.buffer.write(b"NO\n")
    else:
        sys.stdout.buffer.write(b"YES\n" + b"\n".join(result) + b"\n")


if __name__ == "__main__":
    main()
