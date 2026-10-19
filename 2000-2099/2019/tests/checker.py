"""Accept any type-compatible noncrossing bijection, or a correct impossibility claim."""

from collections import deque
from pathlib import Path
import re
import sys


def read_case(text):
    tokens = text.split()
    if len(tokens) != 2:
        raise ValueError("expected n and word")
    n, word = int(tokens[0]), tokens[1]
    if not 1 <= n <= 5000 or len(word) != 2 * n or re.fullmatch("[A-Za-z]+", word) is None:
        raise ValueError("bad size or alphabet")
    if sum(c.isupper() for c in word) != n:
        raise ValueError("unbalanced endpoint roles")
    return n, word


def reducible(word):
    size = len(word)
    previous = list(range(-1, size - 1))
    following = list(range(1, size + 1))
    alive = [True] * size
    pending = deque(i for i in range(size - 1) if word[i].swapcase() == word[i + 1])
    left = size
    while pending:
        first = pending.popleft()
        if not alive[first]:
            continue
        second = following[first]
        if second == size or not alive[second] or word[first].swapcase() != word[second]:
            continue
        a, b = previous[first], following[second]
        alive[first] = alive[second] = False
        left -= 2
        if a >= 0:
            following[a] = b
        if b < size:
            previous[b] = a
        if a >= 0 and b < size and word[a].swapcase() == word[b]:
            pending.append(a)
    return left == 0


def validate(text, n, word):
    if text.strip() == "Impossible":
        return not reducible(word)
    tokens = text.split()
    if len(tokens) != n or any(re.fullmatch("[0-9]+", token) is None for token in tokens):
        return False
    ids = [int(token) - 1 for token in tokens]
    if set(ids) != set(range(n)):
        return False
    upper = [i for i, c in enumerate(word) if c.isupper()]
    lower = [i for i, c in enumerate(word) if c.islower()]
    partners = [-1] * len(word)
    for index, target in enumerate(ids):
        a, b = upper[index], lower[target]
        if word[a].lower() != word[b]:
            return False
        partners[a], partners[b] = b, a
    closing_positions = []
    for position, other in enumerate(partners):
        if other > position:
            closing_positions.append(other)
        elif not closing_positions or closing_positions.pop() != position:
            return False
    return not closing_positions


if __name__ == "__main__":
    try:
        data = read_case(Path(sys.argv[1]).read_text())
        passed = validate(Path(sys.argv[3]).read_text(), *data)
    except (OSError, ValueError, IndexError):
        passed = False
    if not passed:
        print("Expected a type-compatible noncrossing bijection, or a correct Impossible claim.")
    raise SystemExit(0 if passed else 1)
