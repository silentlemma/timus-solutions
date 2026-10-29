import sys

BATCH_SIZE = 1024


def main():
    # the input is parsed line by line instead of all at once, and the answers
    # go out in batches of 1024 lines
    numbers = (int(token) for line in sys.stdin.buffer for token in line.split())
    n = next(numbers)
    # before[i] is the sum of the first i readings
    before = [0] * (n + 1)
    for i in range(1, n + 1):
        before[i] = before[i - 1] + next(numbers)
    answers = []
    for _ in range(next(numbers)):
        i, j = next(numbers), next(numbers)
        answers.append(str(before[j] - before[i - 1]))
        if len(answers) == BATCH_SIZE:
            sys.stdout.write("\n".join(answers) + "\n")
            answers.clear()
    if answers:
        sys.stdout.write("\n".join(answers) + "\n")


main()
