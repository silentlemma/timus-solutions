"""Validate any complete near-perfect round-robin schedule with distinct leaders."""

from pathlib import Path
import sys


def check(cannons, output):
    size = 2 * cannons + 1
    tokens = output.split()
    if len(tokens) != size * size:
        return False, "wrong number of matrix entries"
    try:
        values = list(map(int, tokens))
    except ValueError:
        return False, "noninteger matrix entry"
    matrix = [values[start : start + size] for start in range(0, len(values), size)]
    for person in range(size):
        if matrix[person][person] != 0:
            return False, "nonzero diagonal"
    used = [set() for _ in range(size)]
    pair_counts = [0] * size
    for left in range(size):
        for right in range(left + 1, size):
            label = matrix[left][right]
            if not 1 <= label <= size:
                return False, "off-diagonal round label out of range"
            if matrix[right][left] != label:
                return False, "asymmetric matrix"
            participants = used[label - 1]
            if left in participants or right in participants:
                return False, "participant assigned twice in one round"
            participants.update((left, right))
            pair_counts[label - 1] += 1
    all_people = set(range(size))
    leaders = []
    for pairs, participants in zip(pair_counts, used):
        if pairs != cannons:
            return False, "wrong number of pairs in a round"
        missing = all_people - participants
        if len(missing) != 1:
            return False, "round does not have exactly one leader"
        leaders.append(missing.pop())
    if len(set(leaders)) != size:
        return False, "a participant leads more than once"
    return True, "valid pair schedule with one distinct leader per round"


if __name__ == "__main__":
    cannons = int(Path(sys.argv[1]).read_text())
    accepted, reason = check(cannons, Path(sys.argv[3]).read_text())
    print(reason)
    sys.exit(0 if accepted else 1)
