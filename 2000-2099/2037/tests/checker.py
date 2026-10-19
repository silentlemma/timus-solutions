"""Check indexed binary words by their distinct nonempty palindromes."""

from pathlib import Path
import re
import sys

SMALL_LIMIT = 7
STABLE_MIN = 8


def minimum(n):
    if n <= SMALL_LIMIT:
        return n
    return SMALL_LIMIT if n == STABLE_MIN else STABLE_MIN


def palindrome_count(word):
    text = "#" + word
    lengths, links, children = [0, -1], [1, 1], [{}, {}]
    last = 0
    for at in range(1, len(text)):
        char = text[at]
        node = last
        while text[at - lengths[node] - 1] != char:
            node = links[node]
        if char in children[node]:
            last = children[node][char]
            continue
        last = len(lengths)
        lengths.append(lengths[node] + 2)
        links.append(0)
        children.append({})
        children[node][char] = last
        if lengths[last] > 1:
            node = links[node]
            while text[at - lengths[node] - 1] != char:
                node = links[node]
            links[last] = children[node][char]
    return len(lengths) - 2


def validate_row(n, index, word):
    if not 1 <= index <= n:
        return False
    if word == "NO":
        return index < minimum(n)
    return len(word) == n and all(char in "ab" for char in word) and palindrome_count(word) == index


def validate(n, raw):
    try:
        lines = raw.decode("ascii").strip().splitlines()
    except UnicodeDecodeError:
        return False
    if len(lines) != n:
        return False
    for index, line in enumerate(lines, 1):
        match = re.fullmatch(r"[ \t]*([0-9]+)[ \t]*:[ \t]*(NO|[ab]+)[ \t]*", line)
        if match is None:
            return False
        try:
            printed_index = int(match[1])
        except ValueError:
            return False
        if printed_index != index or not validate_row(n, index, match[2]):
            return False
    return True


def main():
    n = int(Path(sys.argv[1]).read_text(encoding="ascii"))
    if not validate(n, Path(sys.argv[3]).read_bytes()):
        print("Incorrect indexed word or distinct palindrome count")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
