"""Check any optimal completion with an independent two-capacity letter DP."""

from pathlib import Path
import sys

ALPHABET = 26
FIRST = ord("a")


def quality(text):
    return sum(
        (1 if i % 2 == 0 else -1) * (ord(letter) - FIRST + 1) for i, letter in enumerate(text)
    )


def optimal_quality(pattern, limit):
    fixed = set(pattern) - {"?"}
    positive = sum(letter == "?" and i % 2 == 0 for i, letter in enumerate(pattern))
    negative = pattern.count("?") - positive
    needed = max(0, limit - len(fixed))
    if positive + negative < needed:
        return None
    baseline = quality(
        "".join(("z" if i % 2 == 0 else "a") if c == "?" else c for i, c in enumerate(pattern))
    )
    positive, negative = min(positive, needed), min(negative, needed)
    states = {(0, 0): 0}
    for value in range(1, ALPHABET + 1):
        if chr(FIRST + value - 1) in fixed:
            continue
        following = dict(states)
        for (plus, minus), cost in states.items():
            if plus + minus == needed:
                continue
            if plus < positive:
                key = plus + 1, minus
                candidate = cost + ALPHABET - value
                if key not in following or candidate < following[key]:
                    following[key] = candidate
            if minus < negative:
                key = plus, minus + 1
                candidate = cost + value - 1
                if key not in following or candidate < following[key]:
                    following[key] = candidate
        states = following
    loss = min(cost for (plus, minus), cost in states.items() if plus + minus == needed)
    return baseline - loss


def validate(pattern, limit, raw, target):
    try:
        tokens = raw.decode("ascii").split()
    except UnicodeDecodeError:
        return False
    if len(tokens) != 1:
        return False
    answer = tokens[0]
    if target is None:
        return answer == "-1"
    if len(answer) != len(pattern) or any(not "a" <= c <= "z" for c in answer):
        return False
    if any(a != "?" and a != b for a, b in zip(pattern, answer)):
        return False
    return len(set(answer)) >= limit and quality(answer) == target


def main():
    pattern, token = Path(sys.argv[1]).read_text(encoding="ascii").split()
    limit = int(token)
    target = optimal_quality(pattern, limit)
    actual = Path(sys.argv[3]).read_bytes()
    if not validate(pattern, limit, actual, target):
        print("Invalid or nonoptimal completion")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
