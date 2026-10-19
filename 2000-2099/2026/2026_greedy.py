ALPHABET = 26


def solve(pattern, limit):
    fixed = {ord(letter) - ord("a") + 1 for letter in pattern if letter != "?"}
    positive = [i for i, letter in enumerate(pattern) if letter == "?" and i % 2 == 0]
    negative = [i for i, letter in enumerate(pattern) if letter == "?" and i % 2 == 1]
    needed = max(0, limit - len(fixed))
    if len(positive) + len(negative) < needed:
        return "-1"
    missing = [value for value in range(1, ALPHABET + 1) if value not in fixed]
    low = [0]
    high = [0]
    for value in missing:
        low.append(low[-1] + value - 1)
    for value in reversed(missing):
        high.append(high[-1] + ALPHABET - value)
    choices = range(max(0, needed - len(negative)), min(needed, len(positive)) + 1)
    positives = min(choices, key=lambda count: high[count] + low[needed - count])
    negatives = needed - positives
    answer = list(pattern)
    for index in positive:
        answer[index] = "z"
    for index in negative:
        answer[index] = "a"
    for at in range(positives):
        answer[positive[at]] = chr(ord("a") + missing[-1 - at] - 1)
    for at in range(negatives):
        answer[negative[at]] = chr(ord("a") + missing[at] - 1)
    return "".join(answer)


def main():
    import sys

    pattern, limit = sys.stdin.read().split()
    print(solve(pattern, int(limit)))


if __name__ == "__main__":
    main()
