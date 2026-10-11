import sys


def main():
    words = sys.stdin.read().split()
    k, last = int(words[0]), words[1]
    # row order[j] of the table ends with the j-th character of the
    # sorted last column, which is the first character of row j
    order = sorted(range(len(last)), key=last.__getitem__)
    row, text = k - 1, []
    for _ in range(len(last)):
        row = order[row]
        text.append(last[row])
    print("".join(text))


main()
