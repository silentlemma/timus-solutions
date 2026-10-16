import sys

NOTES = [10, 50, 100, 500, 1000, 5000]


def main():
    data = list(map(int, sys.stdin.read().split()))
    counts, price = data[:len(NOTES)], data[len(NOTES)]
    total = sum(c * note for c, note in zip(counts, NOTES))
    smallest = min(note for c, note in zip(counts, NOTES) if c > 0)
    # k tickets fit when k * price <= total, and taking away the smallest
    # note must leave too little: total - smallest < k * price
    answers = range((total - smallest) // price + 1, total // price + 1)
    print(len(answers))
    print(*answers)


main()
