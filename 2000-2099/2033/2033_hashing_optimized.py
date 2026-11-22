RECORDS = 6


def main():
    words = (word for line in open(0, "rb") for word in line.split())
    groups = {}
    for _ in range(RECORDS):
        next(words)
        model, price = next(words), int(next(words))
        if model in groups:
            stats = groups[model]
            stats[0] += 1
            if price < stats[1]:
                stats[1] = price
        else:
            groups[model] = [1, price]
    # The model with most records wins; its cheapest purchase breaks ties.
    answer = min(groups, key=lambda model: (-groups[model][0], groups[model][1], model))
    print(answer.decode())


main()
