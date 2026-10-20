import sys


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    suits, ranks, rows = next(tokens), next(tokens), next(tokens)
    total = suits * ranks
    left = [-1] * total
    degree = [1] * total
    for card in range(0, total, ranks):
        degree[card] = 0

    for _ in range(rows):
        length = next(tokens)
        previous = -1
        for _ in range(length):
            suit, rank = next(tokens), next(tokens)
            card = (suit - 1) * ranks + rank - 1
            left[card] = previous
            if previous != -1:
                degree[previous] += 1
            previous = card
    del tokens

    order = [card for card in range(total) if degree[card] == 0]
    for card in order:
        # Suit edges precede row edges to keep the output deterministic.
        if (card + 1) % ranks != 0:
            degree[card + 1] -= 1
            if degree[card + 1] == 0:
                order.append(card + 1)
        neighbor = left[card]
        if neighbor != -1:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                order.append(neighbor)

    if len(order) != total:
        sys.stdout.write("NO\n")
        return
    answer = ["YES"]
    answer.extend(f"{card // ranks + 1} {card % ranks + 1}" for card in order)
    sys.stdout.write("\n".join(answer) + "\n")


if __name__ == "__main__":
    main()
