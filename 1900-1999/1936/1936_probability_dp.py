import sys

GESTURE_COUNT = 3
OUTPUT_DIGITS = 12


def expected_rounds(count):
    expected = [0.0] * (count + 1)
    power_three = 1.0
    power_two = 2.0
    for players in range(2, count + 1):
        power_three *= GESTURE_COUNT
        power_two *= 2
        weighted_successors = 0.0
        combination = 1.0
        for survivors in range(1, players):
            combination = combination * (players - survivors + 1) / survivors
            weighted_successors += combination * expected[survivors]
        expected[players] = (power_three + weighted_successors) / (power_two - 2)
    return expected[count]


def main():
    count = int(sys.stdin.buffer.read())
    print(f"{expected_rounds(count):.{OUTPUT_DIGITS}f}")


if __name__ == "__main__":
    main()
