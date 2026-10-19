"""Check any optimal option: any feasible globally optimal option is accepted."""

from pathlib import Path
import re
import sys

NO_OPTION = "Forget about apartments. Live in the dormitory."
ALONE = re.compile(r"You should rent the apartment #([1-9][0-9]*) alone\.")
SHARED = re.compile(
    r"You should rent the apartment #([1-9][0-9]*) with the friend #([1-9][0-9]*)\."
)


def read_case(text):
    tokens = iter(map(int, text.split()))
    budget = next(tokens)
    alone = [next(tokens), next(tokens)]
    friends = [(next(tokens), next(tokens)) for _ in range(next(tokens))]
    apartments = [(next(tokens), next(tokens), next(tokens)) for _ in range(next(tokens))]
    if next(tokens, None) is not None:
        raise ValueError("extra input")
    return budget, alone, friends, apartments


def validate(text, budget, alone, friends, apartments):
    text = text.strip()
    best = -1
    for rooms, price, benefit in apartments:
        if price <= budget:
            best = max(best, benefit + alone[rooms - 1])
        if rooms == 2 and price <= 2 * budget:
            for money, value in friends:
                if price <= 2 * money:
                    best = max(best, benefit + value)
    if text == NO_OPTION:
        return best < 0
    match = ALONE.fullmatch(text)
    friend = 0
    if match:
        apartment = int(match.group(1))
    else:
        match = SHARED.fullmatch(text)
        if not match:
            return False
        apartment, friend = map(int, match.groups())
    if not 1 <= apartment <= len(apartments):
        return False
    rooms, price, benefit = apartments[apartment - 1]
    if friend:
        if rooms != 2 or not 1 <= friend <= len(friends):
            return False
        money, value = friends[friend - 1]
        if price > 2 * budget or price > 2 * money:
            return False
        score = benefit + value
    else:
        if price > budget:
            return False
        score = benefit + alone[rooms - 1]
    return score == best


if __name__ == "__main__":
    try:
        data = read_case(Path(sys.argv[1]).read_text())
        passed = validate(Path(sys.argv[3]).read_text(), *data)
    except (OSError, ValueError, IndexError, StopIteration):
        passed = False
    if not passed:
        print("Expected a feasible option with maximum total benefit, in the required format.")
    raise SystemExit(0 if passed else 1)
