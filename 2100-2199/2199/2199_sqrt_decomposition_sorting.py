import math
import sys
from bisect import bisect_left, bisect_right

VALUE_LIMIT = 10**9
INFINITY = 2 * VALUE_LIMIT + 1
BLOCK_SCALE = 3
GROUP_SHIFT = 4
GROUP_SIZE = 1 << GROUP_SHIFT
GROUP_MASK = GROUP_SIZE - 1


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, q = data[:2]
    days = data[2 : n + 2]
    order = sorted(range(n), key=days.__getitem__)
    abs_order = sorted(range(n), key=lambda i: abs(days[i]))
    size = max(1, BLOCK_SCALE * n // max(1, math.isqrt(q)))
    buckets = [[] for _ in range((n + size - 1) // size)]
    query_bits = q.bit_length()
    query_mask = (1 << query_bits) - 1
    query_left = [0] * q
    offset = n + 2
    for query in range(q):
        left, right = data[offset], data[offset + 1]
        left -= 1
        query_left[query] = left
        buckets[left // size].append((right << query_bits) | query)
        offset += 2
    del data
    answers = [None] * q
    previous_days = [-1] * n
    next_days = [-1] * n
    before = [-1] * n
    after = [-1] * n
    update_begin = [0] * n
    update_end = [0] * n
    target_split = [0] * n
    for block, queries in enumerate(buckets):
        if not queries:
            continue
        queries.sort()
        start = block * size
        boundary = min(n, start + size)
        stop = queries[-1] >> query_bits
        # The reverse deletion order records neighbors for later insertions.
        fringe_order = [day for day in abs_order if start <= day < boundary]
        last = -1
        for day in fringe_order:
            previous_days[day] = last
            if last >= 0:
                next_days[last] = day
            last = day
        next_days[last] = -1
        for day in range(start, boundary):
            previous, following = previous_days[day], next_days[day]
            before[day], after[day] = previous, following
            if previous >= 0:
                next_days[previous] = following
            if following >= 0:
                previous_days[following] = previous
        fringe_score = [INFINITY] * (boundary - start + 1)
        fringe_first = [0] * (boundary - start + 1)
        fringe_second = [0] * (boundary - start + 1)
        best = INFINITY
        first = second = 0
        for day in range(boundary - 1, start - 1, -1):
            for other in (before[day], after[day]):
                if other >= 0:
                    score = abs(days[day] + days[other])
                    if score < best:
                        best, first, second = score, day, other
            fringe_score[day - start] = best
            fringe_first[day - start] = first
            fringe_second[day - start] = second
        # A closest pair is adjacent in the order of absolute values.
        last = -1
        for day in abs_order:
            if boundary <= day < stop:
                previous_days[day] = last
                if last >= 0:
                    next_days[last] = day
                last = day
        if last >= 0:
            next_days[last] = -1
        for day in range(stop - 1, boundary - 1, -1):
            previous, following = previous_days[day], next_days[day]
            before[day], after[day] = previous, following
            if previous >= 0:
                next_days[previous] = following
            if following >= 0:
                previous_days[following] = previous
        # A new core point becomes nearest throughout one interval of reflected values.
        fringe = sorted(range(start, boundary), key=lambda day: -days[day])
        targets = [-2 * days[day] for day in fringe]
        last = -1
        position = 0
        for day in order:
            if boundary <= day < stop:
                while position < len(fringe) and targets[position] < 2 * days[day]:
                    position += 1
                target_split[day] = position
                previous_days[day] = last
                if last >= 0:
                    next_days[last] = day
                last = day
        if last >= 0:
            next_days[last] = -1
        for day in range(stop - 1, boundary - 1, -1):
            previous, following = previous_days[day], next_days[day]
            value = days[day]
            rank = target_split[day]
            lo = days[previous] + value if previous >= 0 else -2 * INFINITY
            hi = days[following] + value if following >= 0 else 2 * INFINITY
            # Equal distances keep the earlier partner; empty intervals need no search.
            if (
                (previous < 0 or days[previous] != value)
                and (following < 0 or days[following] != value)
                and (
                    (rank and targets[rank - 1] > lo) or (rank < len(fringe) and targets[rank] < hi)
                )
            ):
                update_begin[day] = bisect_right(targets, lo, 0, rank)
                update_end[day] = bisect_left(targets, hi, rank)
            else:
                update_begin[day] = update_end[day] = 0
            if previous >= 0:
                next_days[previous] = following
            if following >= 0:
                previous_days[following] = previous
        partners = [-1] * len(fringe)
        group_count = (len(fringe) + GROUP_MASK) >> GROUP_SHIFT
        tree_size = 1 << (group_count - 1).bit_length()
        groups = [-1] * (2 * tree_size)
        fringe_ranks = [0] * (boundary - start)
        for rank, day in enumerate(fringe):
            fringe_ranks[day - start] = rank
        end = boundary
        core_score = INFINITY
        core_first = core_second = 0
        for packed in queries:
            right = packed >> query_bits
            query = packed & query_mask
            left = query_left[query]
            if right <= boundary:
                last = -1
                best = INFINITY
                first = second = 0
                for day in fringe_order:
                    if left <= day < right:
                        if last >= 0:
                            score = abs(days[day] + days[last])
                            if score < best:
                                best, first, second = score, day, last
                        last = day
            else:
                while end < right:
                    for other in (before[end], after[end]):
                        if other >= 0:
                            score = abs(days[end] + days[other])
                            if score < core_score:
                                core_score, core_first, core_second = score, end, other
                    lo, hi = update_begin[end], update_end[end]
                    if lo < hi:
                        first_group = (lo + GROUP_MASK) >> GROUP_SHIFT
                        last_group = hi >> GROUP_SHIFT
                        if first_group <= last_group:
                            for rank in range(lo, first_group << GROUP_SHIFT):
                                partners[rank] = end
                            lo_node = first_group + tree_size
                            hi_node = last_group + tree_size
                            while lo_node < hi_node:
                                if lo_node & 1:
                                    groups[lo_node] = end
                                    lo_node += 1
                                if hi_node & 1:
                                    hi_node -= 1
                                    groups[hi_node] = end
                                lo_node >>= 1
                                hi_node >>= 1
                            for rank in range(last_group << GROUP_SHIFT, hi):
                                partners[rank] = end
                        else:
                            for rank in range(lo, hi):
                                partners[rank] = end
                    end += 1
                best, first, second = core_score, core_first, core_second
                rank = left - start
                if fringe_score[rank] < best:
                    best, first, second = (
                        fringe_score[rank],
                        fringe_first[rank],
                        fringe_second[rank],
                    )
                # Days are increasing timestamps, so the latest assignment wins.
                for node in range(1, tree_size):
                    stamp = groups[node]
                    child = node * 2
                    if stamp > groups[child]:
                        groups[child] = stamp
                    if stamp > groups[child + 1]:
                        groups[child + 1] = stamp
                for day in range(left, boundary):
                    rank = fringe_ranks[day - start]
                    other = max(partners[rank], groups[tree_size + (rank >> GROUP_SHIFT)])
                    score = abs(days[day] + days[other])
                    if score < best:
                        best, first, second = score, day, other
            first, second = min(first, second), max(first, second)
            answers[query] = f"{first + 1} {second + 1}"
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    solve()
