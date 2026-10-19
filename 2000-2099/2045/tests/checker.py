"""Accept any indexed lowercase words with the requested number of distinct palindromes."""

from pathlib import Path
import re
import sys

MAX_LENGTH = 2000
MINIMUM_STABLE = 3


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


def validate(n, raw):
    if not 1 <= n <= MAX_LENGTH:
        return False
    try:
        lines = raw.decode("ascii").strip().splitlines()
    except UnicodeDecodeError:
        return False
    if len(lines) != n:
        return False
    for index, line in enumerate(lines, 1):
        match = re.fullmatch(r"[ \t]*([0-9]+)[ \t]*:[ \t]*(NO|[a-z]+)[ \t]*", line)
        if match is None:
            return False
        try:
            printed = int(match[1])
        except ValueError:
            return False
        if printed != index:
            return False
        word = match[2]
        if word == "NO":
            if index >= min(n, MINIMUM_STABLE):
                return False
        elif len(word) != n or palindrome_count(word) != index:
            return False
    return True


def main():
    n = int(Path(sys.argv[1]).read_text(encoding="ascii"))
    if not validate(n, Path(sys.argv[3]).read_bytes()):
        print("Incorrect row index, word length, alphabet, palindrome count, or NO")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
