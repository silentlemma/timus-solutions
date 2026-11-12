from collections import deque
import sys

COLOR_COUNT = 3
TRIANGLE_SIZE = 3


def main():
    n = int(sys.stdin.buffer.readline())
    color = [b"RGB".index(letter) for letter in sys.stdin.buffer.readline().strip()]
    counts = [color.count(value) for value in range(COLOR_COUNT)]
    left = [(vertex - 1) % n for vertex in range(n)]
    right = [(vertex + 1) % n for vertex in range(n)]
    alive = [True] * n
    pending = deque(vertex for vertex in range(n) if color[left[vertex]] != color[right[vertex]])
    cuts = []
    remaining = n
    while remaining > TRIANGLE_SIZE:
        if 1 in counts:
            anchor = next(
                vertex for vertex in range(n) if alive[vertex] and counts[color[vertex]] == 1
            )
            vertex = right[right[anchor]]
            while right[vertex] != anchor:
                cuts.append((anchor + 1, vertex + 1))
                vertex = right[vertex]
            break
        vertex = pending.popleft()
        if not alive[vertex] or color[left[vertex]] == color[right[vertex]]:
            continue
        before, after = left[vertex], right[vertex]
        cuts.append((before + 1, after + 1))
        alive[vertex] = False
        right[before], left[after] = after, before
        counts[color[vertex]] -= 1
        remaining -= 1
        # Only the two surviving neighbours can change their eligibility.
        pending.extend((before, after))
    print(len(cuts))
    sys.stdout.write("".join(f"{a} {b}\n" for a, b in cuts))


main()
