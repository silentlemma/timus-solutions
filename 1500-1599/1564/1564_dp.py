DECIMAL = 10
PLACES = 18


def floor_for(target):
    floor = prefix_ones = 0
    width = DECIMAL ** (PLACES - 1)
    for remaining in range(PLACES - 1, -1, -1):
        # Every free position contributes width / 10 ones in this block.
        fixed_cost = prefix_ones * width + remaining * (width // DECIMAL)
        for digit in range(DECIMAL):
            block = fixed_cost + (width if digit == 1 else 0)
            if target <= block:
                floor = DECIMAL * floor + digit
                prefix_ones += digit == 1
                break
            target -= block
        width //= DECIMAL
    return floor if target == prefix_ones else "Petr lies"


if __name__ == "__main__":
    print(floor_for(int(input())))
