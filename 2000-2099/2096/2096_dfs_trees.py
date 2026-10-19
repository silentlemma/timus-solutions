import sys
from array import array


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    activities = array("i", map(int, read().split()))
    child = array("i", [-1]) * (m + 1)
    sibling = array("i", [-1]) * (m + 1)
    query_head = array("i", [-1]) * (m + 1)
    query_next = array("i")
    query_day = array("i")
    query_begin = array("i", [0]) * (m + 2)
    change_begin = array("i", [0]) * (m + 2)
    first = array("i")
    stop = array("i")
    step = array("i")
    value = array("i")

    for plan in range(1, m + 1):
        query_begin[plan] = len(query_day)
        queries = int(read())
        for _ in range(queries):
            target, day = map(int, read().split())
            query_next.append(query_head[target])
            query_head[target] = len(query_day)
            query_day.append(day - 1)

        parent, changes = map(int, read().split())
        sibling[plan] = child[parent]
        child[parent] = plan
        change_begin[plan] = len(first)
        for _ in range(changes):
            day, count, period, activity = map(int, read().split())
            first.append(day - 1)
            stop.append(day - 1 + count * period)
            step.append(period)
            value.append(activity)

    query_begin[m + 1] = len(query_day)
    change_begin[m + 1] = len(first)
    answers = array("i", [0]) * len(query_day)
    history = []
    pending = array("i", [0])

    while pending:
        plan = pending.pop()
        if plan < 0:
            plan = -plan
            for change in range(change_begin[plan + 1] - 1, change_begin[plan] - 1, -1):
                activities[first[change] : stop[change] : step[change]] = history.pop()
            continue

        for change in range(change_begin[plan], change_begin[plan + 1]):
            day, end, period = first[change], stop[change], step[change]
            old = activities[day:end:period]
            history.append(old)
            activities[day:end:period] = array("i", [value[change]]) * len(old)

        query = query_head[plan]
        while query != -1:
            answers[query] = activities[query_day[query]]
            query = query_next[query]

        if plan:
            pending.append(-plan)
        descendant = child[plan]
        while descendant != -1:
            pending.append(descendant)
            descendant = sibling[descendant]

    write = sys.stdout.write
    for plan in range(1, m + 1):
        write(" ".join(map(str, answers[query_begin[plan] : query_begin[plan + 1]])))
        write("\n")


if __name__ == "__main__":
    main()
