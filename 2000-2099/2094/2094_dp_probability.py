import sys

PERCENT = 100
OUTPUT_SCALE = 1_000_000_000
OUTPUT_DIGITS = 9
MIN_DECIMALS = 3
HALF = 0.5


def main():
    data = sys.stdin.buffer.read().split()
    vacancy_percent = int(data[1])
    row = data[2]
    seat = row.index(b"2")
    occupied = row[:seat].count(b"1")
    left = row[:seat].count(b"0")
    right = row[seat + 1 :].count(b"0")
    total = left + right
    step = [0.0] * (total + 1)
    expected = [0.0] * (total + 1)
    another = 0.0
    future = 0.0

    # Condition the binomial arrival count on the prefix already observed.
    for remaining in range(1, total + 1):
        weight = float(remaining * (PERCENT - vacancy_percent))
        absent = float((total - remaining + 1) * vacancy_percent)
        another = weight / (weight + absent * (1.0 - another))
        future = another * (1.0 + future)
        step[remaining] = another / remaining
        expected[remaining] = future / remaining

    dp = [0.0] * (right + 1)
    for empty_left in range(1, left + 1):
        for empty_right in range(1, right + 1):
            remaining = empty_left + empty_right
            take_seat = empty_right * expected[remaining]
            wait = step[remaining] * (
                empty_left * (1.0 + dp[empty_right]) + empty_right * dp[empty_right - 1]
            )
            dp[empty_right] = min(take_seat, wait)

    rounded = int((occupied + dp[right]) * OUTPUT_SCALE + HALF)
    whole, fraction = divmod(rounded, OUTPUT_SCALE)
    digits = f"{fraction:0{OUTPUT_DIGITS}d}"
    while len(digits) > MIN_DECIMALS and digits.endswith("0"):
        digits = digits[:-1]
    print(f"{whole}.{digits}")


if __name__ == "__main__":
    main()
