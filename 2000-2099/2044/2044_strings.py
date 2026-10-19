"""Exact palindrome partition counts with series links and bounded word masks."""

from array import array
import sys

ALPHABET_SIZE = 26
COUNT_LIMIT = 31
MASK = (1 << (COUNT_LIMIT + 1)) - 1
OUTPUT_CHUNK = 1024


def solve(word):
    text = b"\0" + word
    n = len(word)
    length = array("i", [0]) * (n + 2)
    link = array("i", [0]) * (n + 2)
    diff = array("i", [0]) * (n + 2)
    series = array("i", [0]) * (n + 2)
    cache = array("I", [0]) * (n + 2)
    dp = array("I", [0]) * (n + 1)
    dp[0] = 1
    length[0] = -1
    edges = {}
    used = 2
    last = 1
    for i in range(1, n + 1):
        c = text[i]
        code = c - ord("a")
        parent = last
        while text[i - 1 - length[parent]] != c:
            parent = link[parent]
        key = parent * ALPHABET_SIZE + code
        v = edges.get(key, 0)
        if not v:
            v = used
            used += 1
            edges[key] = v
            length[v] = length[parent] + 2
            if length[v] == 1:
                suffix = 1
            else:
                candidate = link[parent]
                while text[i - 1 - length[candidate]] != c:
                    candidate = link[candidate]
                suffix = edges[candidate * ALPHABET_SIZE + code]
            link[v] = suffix
            diff[v] = length[v] - length[suffix]
            series[v] = series[suffix] if diff[v] == diff[suffix] else suffix
        last = v
        value = 0
        while length[v] > 0:
            cut = i - length[series[v]] - diff[v]
            cache[v] = dp[cut]
            suffix = link[v]
            if diff[v] == diff[suffix]:
                cache[v] |= cache[suffix]
            value |= cache[v] << 1
            v = series[v]
        dp[i] = value & MASK
    return dp


def write_masks(dp):
    out = []
    for value in dp[1:]:
        out.append(str(value >> 1))
        if len(out) == OUTPUT_CHUNK:
            sys.stdout.write("\n".join(out) + "\n")
            out.clear()
    if out:
        sys.stdout.write("\n".join(out) + "\n")


def main():
    write_masks(solve(sys.stdin.buffer.read().strip()))


if __name__ == "__main__":
    main()
