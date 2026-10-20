import sys

ALPHABET = 26
FIRST_LETTER = ord("a")


def suffix_array(text):
    n = len(text)
    order = list(range(n))
    rank = list(text)
    width = 1
    base = max(n, max(rank)) + 1
    while width < n:
        shifted = rank[width:] + [0] * width
        keys = [first * base + second for first, second in zip(rank, shifted)]
        order.sort(key=keys.__getitem__)
        next_rank = [0] * n
        classes = 1
        previous = keys[order[0]]
        next_rank[order[0]] = classes
        for index in order[1:]:
            if keys[index] != previous:
                classes += 1
                previous = keys[index]
            next_rank[index] = classes
        rank = next_rank
        if classes == n:
            break
        width *= 2
    return order


def lcp_table(text, order):
    n = len(text)
    rank = [0] * n
    for position, index in enumerate(order):
        rank[index] = position
    lcp = [0] * n
    matched = 0
    for index in range(n):
        position = rank[index]
        if position == 0:
            matched = 0
            continue
        other = order[position - 1]
        while index + matched < n and other + matched < n:
            if text[index + matched] != text[other + matched]:
                break
            matched += 1
        lcp[position] = matched
        if matched:
            matched -= 1
    table = [lcp]
    width = 1
    while 2 * width <= n:
        previous = table[-1]
        table.append(
            [
                first if first < second else second
                for first, second in zip(previous, previous[width:])
            ]
        )
        width *= 2
    return rank, table


def common_prefix(first, second, table):
    if first > second:
        first, second = second, first
    level = (second - first).bit_length() - 1
    row = table[level]
    left = row[first + 1]
    right = row[second - (1 << level) + 1]
    return left if left < right else right


def solve(text):
    n = len(text)
    rank, table = lcp_table(text, suffix_array(text))
    representatives = [[] for _ in range(ALPHABET)]
    farthest = [0] * (ALPHABET + 1)
    lowest = ALPHABET + 1
    skipped = 0
    for position, letter in enumerate(text):
        letter -= FIRST_LETTER
        candidates = representatives[letter]
        longest = 0
        current_rank = rank[position]
        for previous, cost in reversed(candidates):
            if longest == n - position:
                break
            if text[previous + longest] != text[position + longest]:
                continue
            matched = common_prefix(rank[previous], current_rank, table)
            if matched > longest:
                longest = matched
                end = position + matched
                if end > farthest[cost]:
                    farthest[cost] = end
                if cost < lowest:
                    lowest = cost
        # Earlier starts with no greater cost dominate this new start.
        if not candidates or skipped < candidates[-1][1]:
            candidates.append((position, skipped))
        while lowest <= ALPHABET and farthest[lowest] < position + 1:
            lowest += 1
        skipped = min(skipped + 1, lowest)
    return n - skipped


def main():
    tokens = sys.stdin.buffer.read().split()
    print(solve(tokens[1]))


if __name__ == "__main__":
    main()
