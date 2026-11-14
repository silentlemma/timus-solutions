from collections import deque
import sys

STEP = 10
UNREACHABLE = 10001
GOOD = ord("1")


def plan(good, limit):
    n = len(good)
    costs = [0] + [UNREACHABLE] * limit
    history = []
    best = (0, 0, 0) if n < STEP else (UNREACHABLE, 0, 0)
    for place in range(STEP, n + limit + 1, STEP):
        next_costs = [UNREACHABLE] * (limit + 1)
        parents = bytearray(limit + 1)
        window = deque()
        for friends in range(min(limit, place) + 1):
            # A block ending with a friend adds 1 to STEP friends.
            friend_parent = window[0] if window else 0
            friend_cost = costs[friend_parent] + 1 if window else UNREACHABLE

            # A block ending with a conductor adds at most STEP - 1 friends.
            if window and window[0] == friends - STEP:
                window.popleft()
            while window and costs[window[-1]] >= costs[friends]:
                window.pop()
            window.append(friends)
            conductor_parent = window[0]
            conductors = place - friends
            if conductors > n:
                continue
            conductor_cost = UNREACHABLE
            if conductors:
                conductor_cost = costs[conductor_parent] + (good[conductors - 1] == GOOD)
            if conductor_cost <= friend_cost:
                next_costs[friends] = conductor_cost
                parents[friends] = 2 * conductor_parent
            else:
                next_costs[friends] = friend_cost
                parents[friends] = 2 * friend_parent + 1
            if n - conductors < STEP and next_costs[friends] < best[0]:
                best = next_costs[friends], place, friends
        costs = next_costs
        history.append(parents)

    score, place, friends = best
    inserted = []
    while place:
        parent, fined_friend = divmod(history[place // STEP - 1][friends], 2)
        if fined_friend:
            inserted.append(place)
        first = place - STEP + 1
        inserted.extend(range(first + friends - parent - fined_friend - 1, first - 1, -1))
        friends = parent
        place -= STEP
    inserted.reverse()
    return score, inserted


def main():
    data = sys.stdin.buffer.read().split()
    _, limit = map(int, data[:2])
    score, inserted = plan(data[2] if len(data) > 2 else b"", limit)
    print(score)
    print(len(inserted), *inserted)


if __name__ == "__main__":
    main()
