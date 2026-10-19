import sys

LABELS = ("left", "right")


def read_case(tokens):
    count, group_count = next(tokens), next(tokens)
    friends = []
    for _ in range(count):
        row = []
        friend = next(tokens)
        while friend:
            row.append(friend - 1)
            friend = next(tokens)
        friends.append(row)
    groups = []
    for _ in range(group_count):
        time, size = next(tokens), next(tokens)
        groups.append((time, [next(tokens) - 1 for _ in range(size)]))
    return friends, groups


def solve(friends, groups):
    count = len(friends)
    queues = [[], []]
    which = [-1] * count
    position = [-1] * count
    next_completion = [0, 0]
    answer = [None] * count
    for now, students in groups:
        for side, queue in enumerate(queues):
            if queue and next_completion[side] <= now:
                served = min(len(queue), now - next_completion[side] + 1)
                for at, student in enumerate(queue[:served]):
                    answer[student] = (next_completion[side] + at, side)
                    which[student] = -1
                del queue[:served]
                for at, student in enumerate(queue):
                    position[student] = at
                next_completion[side] = next_completion[side] + served if queue else 0
        for student in students:
            best = [len(queues[0]), len(queues[1])]
            for friend in friends[student]:
                side = which[friend]
                if side >= 0:
                    best[side] = min(best[side], position[friend] + 1)
            side = 0 if best[0] < best[1] else 1
            queue = queues[side]
            at = best[side]
            queue.insert(at, student)
            which[student] = side
            for index in range(at, len(queue)):
                position[queue[index]] = index
            if len(queue) == 1:
                next_completion[side] = now + 1
    for side, queue in enumerate(queues):
        for at, student in enumerate(queue):
            answer[student] = (next_completion[side] + at, side)
    return answer


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    answers = solve(*read_case(tokens))
    sys.stdout.write("".join(f"{time} {LABELS[side]}\n" for time, side in answers))
