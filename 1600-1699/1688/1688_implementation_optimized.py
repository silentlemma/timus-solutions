import sys

SHARES = 3  # a bill is split three ways


def main():
    # stream tokens by line instead of retaining up to 3000 bills and their strings.
    words = (word for line in sys.stdin.buffer for word in line.split())
    threshold = SHARES * int(next(words))
    visits = int(next(words))
    total = 0
    answer = 0
    for i in range(1, visits + 1):
        total += int(next(words))
        # Vanya's share total / 3 exceeds n exactly when total > 3n
        if not answer and total > threshold:
            answer = i
    print(f"Free after {answer} times." if answer else "Team.GOV!")


main()
