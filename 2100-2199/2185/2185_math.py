import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    count = data[0]
    steps = data[2 : count + 2]
    queries = data[count + 2 :]
    del data
    limit = max(max(queries), -min(queries) - 1)
    left, right, offset = 0, limit, 0
    removed = []

    for step in steps:
        if left + offset < 0:
            offset += step
        else:
            offset -= step
        cut = -offset
        if left < cut <= right:
            center = 2 * cut - 1
            # Opposite values stay complementary after every remaining step.
            if cut - left <= right - cut + 1:
                removed.append((left, cut, center))
                left = cut
            else:
                removed.append((cut, right + 1, center))
                right = cut - 1
    del steps

    answers = [0] * (limit + 1)
    for index in range(left, right + 1):
        answers[index] = index + offset
    for begin, end, center in reversed(removed):
        for index in range(begin, end):
            answers[index] = -answers[center - index] - 1
    del removed

    output = [str(answers[x] if x >= 0 else -answers[-x - 1] - 1) for x in queries]
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
