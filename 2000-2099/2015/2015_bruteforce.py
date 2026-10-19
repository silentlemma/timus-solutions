import sys


def solve(budget, alone, friends, apartments):
    best_score = -1
    choice = None
    for i, (rooms, price, benefit) in enumerate(apartments, 1):
        if price <= budget:
            score = benefit + alone[rooms - 1]
            if score > best_score:
                best_score, choice = score, (i, 0)
        if rooms == 2 and price <= 2 * budget:
            for j, (friend_budget, friend_benefit) in enumerate(friends, 1):
                if price <= 2 * friend_budget:
                    score = benefit + friend_benefit
                    if score > best_score:
                        best_score, choice = score, (i, j)
    return choice


def render(choice):
    if choice is None:
        return "Forget about apartments. Live in the dormitory.\n"
    apartment, friend = choice
    if friend == 0:
        return f"You should rent the apartment #{apartment} alone.\n"
    return f"You should rent the apartment #{apartment} with the friend #{friend}.\n"


def read_case(tokens):
    budget = next(tokens)
    alone = [next(tokens), next(tokens)]
    friends = [(next(tokens), next(tokens)) for _ in range(next(tokens))]
    apartments = [(next(tokens), next(tokens), next(tokens)) for _ in range(next(tokens))]
    return budget, alone, friends, apartments


if __name__ == "__main__":
    data = read_case(iter(map(int, sys.stdin.buffer.read().split())))
    sys.stdout.write(render(solve(*data)))
