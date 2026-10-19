import sys

MOD = 1_000_000_007


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    k, t = data[:2]
    width = k + 1
    cards = data[2 : 2 + width]
    initial = data[2 + width : 2 + 2 * width]
    x, y = data[-2:]
    remaining = [c - s for c, s in zip(cards, initial)]
    total = sum(remaining)
    deck = total - t

    choose = [[0] * (total + 1) for _ in range(total + 1)]
    for n in range(total + 1):
        choose[n][0] = 1
        for j in range(1, n + 1):
            choose[n][j] = choose[n - 1][j - 1] + choose[n - 1][j]
    reduced = [[value % MOD for value in row] for row in choose]

    # All conditional probabilities have the same denominator.
    ways = [[0] * (y + 1) for _ in range(deck + 1)]
    for useful in range(deck + 1):
        count = 0
        for opened in range(y + 1):
            if opened <= useful and y - opened <= deck - useful:
                count += choose[useful][opened] * choose[deck - useful][y - opened]
            ways[useful][opened] = count

    answer = 0
    colored = total - remaining[0]
    for zeros in range(max(0, t - colored), min(remaining[0], t) + 1):
        needed = t - zeros
        baseline = 0
        events = []
        for color in range(1, width):
            for drawn in range(min(remaining[color], needed) + 1):
                hand = initial[0] + zeros + initial[color] + drawn
                useful = cards[0] + cards[color] - hand
                score = 0
                if useful <= deck and hand >= x:
                    score = ways[useful][min(y, hand - x)]
                if drawn == 0:
                    baseline = max(baseline, score)
                else:
                    events.append((score, color, drawn))
        events.sort()

        product = [0] * (needed + 1)
        product[0] = 1
        subtotal = baseline * product[needed] % MOD
        for score, color, drawn in events:
            coefficients = reduced[remaining[color]]
            quotient = [0] * (needed - drawn + 1)
            # Divide out the old color factor, whose constant coefficient is one.
            for degree in range(len(quotient)):
                value = product[degree]
                for j in range(1, min(drawn - 1, degree) + 1):
                    value -= coefficients[j] * quotient[degree - j]
                quotient[degree] = value % MOD
            previous = product[needed]
            coefficient = coefficients[drawn]
            for degree, value in enumerate(quotient):
                target = degree + drawn
                product[target] = (product[target] + coefficient * value) % MOD
            increase = product[needed] - previous
            subtotal = (subtotal + max(baseline, score) % MOD * increase) % MOD
        answer = (answer + reduced[remaining[0]][zeros] * subtotal) % MOD

    denominator = reduced[total][t] * reduced[deck][y] % MOD
    print(answer * pow(denominator, MOD - 2, MOD) % MOD)


solve()
