import sys

LABEL_BASE = 1_000_000_001


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    size = data[0]
    values = data[1:]
    good_until = [size] * size
    for offset in range(2):
        next_edge = {}
        limit = size
        for position in range(size - 2 - offset, -1, -2):
            first = values[position]
            second = values[position + 1]
            if first == 0 or second == 0 or first == second:
                limit = position
            else:
                if first > second:
                    first, second = second, first
                key = first * LABEL_BASE + second
                following = next_edge.get(key, size)
                if following < limit:
                    limit = following
                next_edge[key] = position
            # The first forbidden pair is excluded from a valid edge block.
            good_until[position] = limit

    leaf_count = 1
    while leaf_count < size:
        leaf_count *= 2
    tree = [0] * (2 * leaf_count)
    tree[leaf_count : leaf_count + size] = values
    for node in range(leaf_count - 1, 0, -1):
        first = tree[2 * node]
        second = tree[2 * node + 1]
        tree[node] = first if first > second else second

    answer = 0
    for start in range(size - 1):
        vertices = values[start]
        edges = values[start + 1]
        if vertices == 0 or edges > (size - start - 2) // 2:
            continue
        if edges == 0:
            answer += 1
            continue
        end = start + 2 + 2 * edges
        if end > good_until[start + 2]:
            continue

        left = leaf_count + start + 2
        right = leaf_count + end
        maximum = 0
        while left < right:
            if left % 2:
                if tree[left] > maximum:
                    maximum = tree[left]
                left += 1
            if right % 2:
                right -= 1
                if tree[right] > maximum:
                    maximum = tree[right]
            left //= 2
            right //= 2
        if maximum <= vertices:
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()
