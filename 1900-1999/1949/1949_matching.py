import sys

INPUT_FIELDS = 3


def select(movies, students):
    size = len(movies)
    following = [0] * size
    preceding = [0] * size
    for first, (_, finish, count) in enumerate(movies):
        for second, (start, _, next_count) in enumerate(movies):
            if finish <= start and count <= next_count:
                following[first] |= 1 << second
                preceding[second] |= 1 << first
    left_match = [-1] * size
    right_match = [-1] * size
    chosen = matching = 0
    active = 0
    answer = []

    for candidate in range(size):
        old_left = left_match[:]
        old_right = right_match[:]
        old_matching = matching
        visited = 0

        def extend_left(vertex):
            nonlocal visited
            neighbors = following[vertex] & active
            while neighbors:
                bit = neighbors & -neighbors
                neighbors -= bit
                if visited & bit:
                    continue
                visited |= bit
                target = bit.bit_length() - 1
                partner = right_match[target]
                if partner < 0 or extend_left(partner):
                    left_match[vertex] = target
                    right_match[target] = vertex
                    return True
            return False

        # Add the left copy before allowing the new right copy as a target.
        matching += extend_left(candidate)
        active |= 1 << candidate
        visited = 0

        def extend_right(vertex):
            nonlocal visited
            neighbors = preceding[vertex] & active
            while neighbors:
                bit = neighbors & -neighbors
                neighbors -= bit
                if visited & bit:
                    continue
                visited |= bit
                target = bit.bit_length() - 1
                partner = left_match[target]
                if partner < 0 or extend_right(partner):
                    right_match[vertex] = target
                    left_match[target] = vertex
                    return True
            return False

        matching += extend_right(candidate)
        if chosen + 1 - matching <= students:
            answer.append("1")
            chosen += 1
        else:
            answer.append("0")
            active ^= 1 << candidate
            left_match, right_match = old_left, old_right
            matching = old_matching
    return "".join(answer)


def main():
    words = list(map(int, sys.stdin.buffer.read().split()))
    size, students = words[:2]
    movies = [
        tuple(words[start : start + INPUT_FIELDS])
        for start in range(2, len(words), INPUT_FIELDS)
    ]
    assert len(movies) == size
    print(select(movies, students))


if __name__ == "__main__":
    main()
