import heapq
import sys
from bisect import bisect_left


WORD_BITS = 64


class Occurrences:
    __slots__ = ("positions", "words", "summary", "score", "end")

    def __init__(self, positions, role, initial):
        if len(positions) > 1:
            positions = sorted(set(positions))
        words = [0] * ((len(positions) + WORD_BITS - 1) // WORD_BITS)
        score = 0
        previous = 0
        for rank, position in enumerate(positions):
            if initial[position - 1] == role:
                gap = position - previous - 1
                score += gap * (gap + 1) // 2
                previous = position
                words[rank // WORD_BITS] |= 1 << (rank % WORD_BITS)
        gap = len(initial) - previous
        summary = 0
        for block, word in enumerate(words):
            if word:
                summary |= 1 << block
        self.positions = positions
        self.words = words
        self.summary = summary
        self.score = score + gap * (gap + 1) // 2
        self.end = len(initial) + 1

    def change(self, position, direction):
        positions = self.positions
        words = self.words
        rank = bisect_left(positions, position)
        block, offset = divmod(rank, WORD_BITS)
        bit = 1 << offset
        word = words[block]

        # The summary skips empty words when the adjacent occurrence is farther away.
        lower = word & (bit - 1)
        if lower:
            left = positions[block * WORD_BITS + lower.bit_length() - 1]
        else:
            earlier = self.summary & ((1 << block) - 1)
            if earlier:
                previous = earlier.bit_length() - 1
                left = positions[previous * WORD_BITS + words[previous].bit_length() - 1]
            else:
                left = 0

        upper = word >> (offset + 1)
        if upper:
            right = positions[rank + (upper & -upper).bit_length()]
        else:
            later = self.summary >> (block + 1)
            if later:
                following = block + (later & -later).bit_length()
                first = words[following] & -words[following]
                right = positions[following * WORD_BITS + first.bit_length() - 1]
            else:
                right = self.end

        words[block] = word ^ bit
        if not word or not words[block]:
            self.summary ^= 1 << block
        self.score += direction * (position - left) * (right - position)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, q = data[:2]
    roles = data[2 : n + 2]
    candidates = {}
    for position, role in enumerate(roles, 1):
        candidates.setdefault(role, []).append(position)
    updates = data[n + 2 :]
    for index in range(0, 2 * q, 2):
        position, role = updates[index : index + 2]
        candidates.setdefault(role, []).append(position)
    del data

    groups = {role: Occurrences(positions, role, roles) for role, positions in candidates.items()}
    del candidates
    heap = [(group.score, role) for role, group in groups.items() if group.summary]
    heapq.heapify(heap)
    answers = []
    for index in range(0, 2 * q, 2):
        position, role = updates[index : index + 2]
        old_role = roles[position - 1]
        if old_role != role:
            old_group = groups[old_role]
            new_group = groups[role]
            old_group.change(position, 1)
            new_group.change(position, -1)
            roles[position - 1] = role
            heapq.heappush(heap, (old_group.score, old_role))
            heapq.heappush(heap, (new_group.score, role))
        while heap[0][0] != groups[heap[0][1]].score:
            heapq.heappop(heap)
        answers.append(str(heap[0][0]))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
