import sys


def main():
    text = sys.stdin.buffer.read().split()[0]
    suffixes = sorted(text[i:] for i in range(len(text)))
    answer = len(text) * (len(text) + 1) // 2
    # In sorted order, previously seen prefixes of a suffix are exactly
    # the prefixes it shares with its immediate predecessor.
    for previous, current in zip(suffixes, suffixes[1:]):
        # Prefix equality is monotone. Binary search uses C-level byte
        # comparisons instead of a Python loop over every shared character.
        low, high = 0, min(len(previous), len(current))
        while low < high:
            middle = (low + high + 1) // 2
            if previous[:middle] == current[:middle]:
                low = middle
            else:
                high = middle - 1
        answer -= low
    print(answer)


main()
