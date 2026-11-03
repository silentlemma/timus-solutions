import sys

LONGEST = 100
TOP = 9
MAX_SUM = LONGEST * TOP
INCREMENTS = TOP - 1


def main():
    reach = [[1]]
    lower = [[0]]
    triangular = [d * (d - 1) // 2 for d in range(1, TOP + 1)]
    # For exactly k nonzero digits, index by extra=sum-k and b=(squares-sum)/2.
    # Shift each bitset by its balanced-digit minimum, leaving no leading zeros.
    for size in range(1, LONGEST + 1):
        lows = []
        for extra in range(INCREMENTS * size + 1):
            q, r = divmod(extra, size)
            lows.append(size * q * (q + 1) // 2 + r * (q + 1))
        previous = reach[-1]
        previous_low = lower[-1]
        row = []
        for extra, least in enumerate(lows):
            bits = 0
            for digit_extra in range(max(0, extra - len(previous) + 1), min(INCREMENTS, extra) + 1):
                old = extra - digit_extra
                shift = previous_low[old] + triangular[digit_extra] - least
                bits |= previous[old] << shift
            row.append(bits)
        reach.append(row)
        lower.append(lows)

    digits_text = [str(digit) for digit in range(1, TOP + 1)]
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    answers = []
    cache = {}
    for _ in range(next(tokens)):
        total, squares = next(tokens), next(tokens)
        key = total, squares
        if key in cache:
            answers.append(cache[key])
            continue
        answer = "No solution"
        if 0 < total <= MAX_SUM and total <= squares <= TOP * total and (squares - total) % 2 == 0:
            b = (squares - total) // 2
            # k>=sum/9 and k>=sum²/squares by Cauchy, before any bitset lookup.
            first = max((total + TOP - 1) // TOP, (total * total + squares - 1) // squares)
            found = 0
            for size in range(first, min(LONGEST, total) + 1):
                extra = total - size
                if 0 <= extra < len(reach[size]):
                    bit = b - lower[size][extra]
                    if bit >= 0 and (reach[size][extra] >> bit) & 1:
                        found = size
                        break
            if found:
                digits = []
                digit = 1
                for left in range(found - 1, -1, -1):
                    row, lows = reach[left], lower[left]
                    while True:
                        extra = total - digit - left
                        if 0 <= extra < len(row):
                            bit = b - triangular[digit - 1] - lows[extra]
                            if bit >= 0 and (row[extra] >> bit) & 1:
                                break
                        digit += 1
                    digits.append(digits_text[digit - 1])
                    total -= digit
                    b -= triangular[digit - 1]
                answer = "".join(digits)
        cache[key] = answer
        answers.append(answer)
    print("\n".join(answers))


main()
