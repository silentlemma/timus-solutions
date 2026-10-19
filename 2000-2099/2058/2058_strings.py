"""Minimum odd/even palindromic factorizations of every prefix."""

from array import array
import sys

ALPHABET_SIZE = 26
FIRST_LETTER = ord("a")


def solve(word):
    size = len(word)
    infinity = size + 1
    data = b"\0" + word
    length = array("i", [-1, 0])
    link = [0, 0]
    difference = array("i", [0, 0])
    series = array("i", [0, 0])
    cache_odd = [infinity, infinity]
    cache_even = [infinity, infinity]
    odd = array("i", [infinity]) * (size + 1)
    even = array("i", [infinity]) * (size + 1)
    even[0] = 0
    edges = {}
    last = 1
    output = bytearray()
    for end in range(1, size + 1):
        letter = data[end]
        code = letter - FIRST_LETTER
        node = last
        while data[end - length[node] - 1] != letter:
            node = link[node]
        key = node * ALPHABET_SIZE + code
        found = edges.get(key, 0)
        if not found:
            found = len(length)
            new_length = length[node] + 2
            if new_length == 1:
                suffix = 1
            else:
                candidate = link[node]
                while data[end - length[candidate] - 1] != letter:
                    candidate = link[candidate]
                suffix = edges[candidate * ALPHABET_SIZE + code]
            length.append(new_length)
            link.append(suffix)
            step = new_length - length[suffix]
            difference.append(step)
            series.append(series[suffix] if step == difference[suffix] else suffix)
            cache_odd.append(infinity)
            cache_even.append(infinity)
            edges[key] = found
        last = found
        current_odd = current_even = infinity
        node = last
        while length[node] > 0:
            suffix = link[node]
            before = end - length[series[node]] - difference[node]
            value_odd, value_even = odd[before], even[before]
            if difference[node] == difference[suffix]:
                previous = cache_odd[suffix]
                if previous < value_odd:
                    value_odd = previous
                previous = cache_even[suffix]
                if previous < value_even:
                    value_even = previous
            if value_odd == infinity:
                value_odd = infinity
            if value_even == infinity:
                value_even = infinity
            cache_odd[node], cache_even[node] = value_odd, value_even
            if value_even + 1 < current_odd:
                current_odd = value_even + 1
            if value_odd + 1 < current_even:
                current_even = value_odd + 1
            node = series[node]
        odd[end], even[end] = current_odd, current_even
        answer_odd = current_odd if current_odd < infinity else -1
        answer_even = current_even if current_even < infinity else -2
        output.extend(f"{answer_odd} {answer_even}\n".encode())
    return output


def main():
    sys.stdout.buffer.write(solve(sys.stdin.buffer.readline().strip()))


if __name__ == "__main__":
    main()
