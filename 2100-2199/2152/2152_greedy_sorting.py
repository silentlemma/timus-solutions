import sys
from array import array
from bisect import bisect_right

BASE = 10
CENTS = BASE * BASE
ZERO_CODE = ord("0")
NINE_CODE = ord("9")
SPACE_CODE = ord(" ")
HEADER_SIZE = 6
MAX_DIGIT = BASE - 1
MAX_VALUE = BASE**MAX_DIGIT
MAX_PRICE_GAIN = (BASE - 2) * MAX_VALUE * CENTS
POWERS = [BASE**exponent for exponent in range(BASE)]


def main():
    header = sys.stdin.buffer.read().split(None, HEADER_SIZE)
    data = bytearray(header.pop())
    n, k, weight_limit, price_limit, weight_rate, price_rate = map(int, header)
    weight_rate *= CENTS
    large_gain = MAX_PRICE_GAIN // weight_rate
    gains = [0] * n
    choices = array("i", [0]) * n
    weight_total = price_total = 0
    cursor = 0
    length = len(data)
    for index in range(n):
        while data[cursor] <= SPACE_CODE:
            cursor += 1
        weight = 0
        position = cursor
        while cursor < length and data[cursor] > SPACE_CODE:
            digit = data[cursor]
            weight = weight * BASE + digit - ZERO_CODE
            if digit == NINE_CODE and position == cursor:
                position += 1
            cursor += 1
        weight_position = position
        weight_delta = 0
        if position < cursor:
            weight_delta = (NINE_CODE - data[position]) * POWERS[cursor - position - 1]
        while data[cursor] <= SPACE_CODE:
            cursor += 1
        price = 0
        position = cursor
        while cursor < length and data[cursor] > SPACE_CODE:
            digit = data[cursor]
            price = price * BASE + digit - ZERO_CODE
            if digit == NINE_CODE and position == cursor:
                position += 1
            cursor += 1
        price_delta = 0
        if position < cursor:
            price_delta = (NINE_CODE - data[position]) * POWERS[cursor - position - 1]
        weight_excess = weight - weight_limit
        if weight_excess > 0:
            weight_total += weight_excess
        else:
            weight_excess = 0
        price_excess = price - price_limit
        if price_excess > 0:
            price_total += price_excess
        else:
            price_excess = 0
        weight_gain = weight + weight_delta - weight_limit - weight_excess
        if weight_gain < 0:
            weight_gain = 0
        # Above the price bound, only the unscaled weight gain determines the order.
        if weight_gain > large_gain:
            weight_gain += MAX_PRICE_GAIN
        else:
            weight_gain *= weight_rate
        price_gain = price + price_delta - price_limit - price_excess
        if price_gain < 0:
            price_gain = 0
        price_gain *= price_rate
        if weight_gain >= price_gain:
            gains[index] = weight_gain
            choices[index] = weight_position
        else:
            gains[index] = price_gain
            choices[index] = position
    small_total = 0
    if k:
        ordered = sorted(gains)
        cutoff = ordered[n - k]
        # Spend equal gains in input order, preserving the original tie rule.
        ties = bisect_right(ordered, cutoff) - (n - k)
        del ordered
        for index, gain in enumerate(gains):
            if not gain or gain < cutoff:
                continue
            if gain == cutoff:
                if not ties:
                    continue
                ties -= 1
            if gain > MAX_PRICE_GAIN:
                weight_total += gain - MAX_PRICE_GAIN
            else:
                small_total += gain
            data[choices[index]] = NINE_CODE
    total = weight_total * weight_rate + price_total * price_rate + small_total
    sys.stdout.buffer.write(f"{total // CENTS}.{total % CENTS:02d}\n".encode() + data)


if __name__ == "__main__":
    main()
