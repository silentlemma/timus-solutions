import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    exponent, query_count = data[:2]
    count = 1 << exponent
    prefix = [0] * (count + 1)
    total = 0
    for index in range(count):
        total += data[index + 2]
        prefix[index + 1] = total

    times = [[0] * count]
    half = 1
    for _ in range(exponent):
        previous = times[-1]
        width = half * 2
        current = [0] * (count - width + 1)
        for left in range(len(current)):
            # Equal volumes make the merge time the difference of the two sums.
            difference = 2 * prefix[left + half] - prefix[left] - prefix[left + width]
            if difference < 0:
                difference = -difference
            ready = previous[left]
            other = previous[left + half]
            if other > ready:
                ready = other
            current[left] = ready + difference
        times.append(current)
        half = width

    answers = []
    offset = count + 2
    for _ in range(query_count):
        left, power = data[offset : offset + 2]
        answers.append(str(times[power][left - 1]) + ".0")
        offset += 2
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
