DIGITS = 10


def count_tickets(half):
    ways = [1]
    for _ in range(half):
        following = [0] * (len(ways) + DIGITS - 1)
        window = 0
        for value in range(len(following)):
            if value < len(ways):
                window += ways[value]
            if value >= DIGITS:
                window -= ways[value - DIGITS]
            following[value] = window
        ways = following
    return sum(count * count for count in ways)


print(count_tickets(int(input()) // 2))
