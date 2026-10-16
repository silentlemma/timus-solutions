import sys
from collections import deque

# every description is three words: amount, "of", name
WORDS = 3


def main():
    words = sys.stdin.read().split()
    m = int(words[0])
    stock = {words[i + 2]: int(words[i]) for i in range(1, WORDS * m + 1, WORDS)}
    start = WORDS * m + 2
    n = int(words[start - 1])
    # each customer: [product, wanted, amount told at the last visit]
    line = deque([words[i + 2], int(words[i]), -1]
                 for i in range(start, start + WORDS * n, WORDS))
    minutes = 0
    while line:
        customer = line.popleft()
        minutes += 1
        product, wanted, seen = customer
        left = stock.get(product, 0)
        if left >= wanted:
            stock[product] = left - wanted
        elif left == seen:
            # the same rest as before the call: take it all
            stock[product] = 0
        elif left > 0:
            # let the next one forward and call home; if the next one is
            # the last of the line, it is Mark's turn
            customer[2] = left
            if not line:
                break
            line.insert(1, customer)
    print(minutes)


main()
