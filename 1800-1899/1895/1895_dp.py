from array import array
import sys


def solve(window, capacity, deadlines):
    n = len(deadlines)
    width = n + 1
    state_count = width * width
    target = state_count - 1
    infinity = deadlines[-1] + 1
    releases = [max(0, deadline - window) for deadline in deadlines]
    initial = array("h", [infinity]) * state_count
    initial[0] = -1
    layers, parents = [initial], [None]
    active = [0]
    for busy in range(1, 2 * n + 1):
        current = layers[-1]
        following = array("h", [infinity]) * state_count
        previous = array("h", [-1]) * state_count
        next_active = []
        for state in active:
            first_done, second_done = divmod(state, width)
            earliest = current[state] + 1
            for new_first in range(min(capacity, n - first_done) + 1):
                new_second = min(capacity - new_first, first_done - second_done)
                if new_first + new_second == 0:
                    continue
                ni, nj = first_done + new_first, second_done + new_second
                minute = max(earliest, releases[ni - 1]) if new_first else earliest
                if new_second and minute >= deadlines[second_done]:
                    continue
                if nj < n:
                    remaining_sides = 1 if nj < ni else 2
                    if minute + 1 + remaining_sides > deadlines[nj]:
                        continue
                destination = ni * width + nj
                if minute < following[destination]:
                    if following[destination] == infinity:
                        next_active.append(destination)
                    following[destination] = minute
                    previous[destination] = state
        layers.append(following)
        parents.append(previous)
        if following[target] != infinity:
            first, second = [0] * n, [0] * n
            state = target
            for used in range(busy, 0, -1):
                old_state = parents[used][state]
                ni, nj = divmod(state, width)
                oi, oj = divmod(old_state, width)
                minute = layers[used][state]
                for job in range(oi, ni):
                    first[job] = minute
                for job in range(oj, nj):
                    second[job] = minute
                state = old_state
            return busy, list(zip(first, second))
        if not next_active:
            return None
        active = next_active
    return None


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    window, capacity, n = next(tokens), next(tokens), next(tokens)
    result = solve(window, capacity, [next(tokens) for _ in range(n)])
    if result is None:
        print(-1)
    else:
        busy, starts = result
        print(busy)
        sys.stdout.write("".join(f"{first} {second}\n" for first, second in starts))


if __name__ == "__main__":
    main()
