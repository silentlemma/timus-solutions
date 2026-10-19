import random
import sys

MAX_POSITION = 100000


def main():
    randomizer = random.Random(int(sys.argv[1]))
    mode = int(sys.argv[2])
    if mode in (1, 2):
        bound = 200 if mode == 1 else MAX_POSITION - 1
        speed = randomizer.randint(1, bound - 1)
        fire_speed = randomizer.randint(speed + 1, bound)
        length = randomizer.randint(1, 1000)
        width, gap, natural = [randomizer.randint(1, bound) for _ in range(3)]
        shield, braking = [randomizer.randint(0, 10000) for _ in range(2)]
        parameters = [speed, length, fire_speed, width, gap, natural, shield, braking]
        left = randomizer.randint(1, 2000)
        branches = []
        for _ in range(randomizer.randint(1, 5)):
            right = left + length + randomizer.randint(1, 3000)
            branches.append((left, right))
            left = right + randomizer.randint(1, 1000)
    elif mode == 3:
        parameters = [99998, 1, 99999, 99999, 99999, 1, 10000, 10000]
        branches = [(1 + 3 * index, 3 + 3 * index) for index in range(1000)]
    elif mode == 4:
        parameters = [99998, 1, 99999, 1, 1, 1, 10000, 10000]
        branches = [(1 + 99 * index, 99 + 99 * index) for index in range(1000)]
    elif mode == 5:
        parameters = [33334, 1, 99999, 1, 1, 66666, 0, 10000]
        branches = [(1, 3)]
    elif mode == 6:
        parameters = [3, 1, 5, 99999, 99999, 99999, 0, 10000]
        branches = [(10, 30)]
    elif mode == 7:
        parameters = [100, 10, 200, 100, 1, 1, 0, 0]
        branches = [(10, 120), (130, 240), (250, 360)]
    elif mode == 8:
        index = randomizer.randrange(3)
        entries, gaps = (2, 3, 4), (1, 2, 3)
        entry = entries[index]
        parameters = [3, 1, 5, 30, gaps[index], 1, 10000, 10000]
        branches = [(entry - 1, entry + 10)]
    elif mode == 9:
        parameters = [100, 10, 200, 100, 1, 1, 0, 10000]
        branches = [(10, 21), (30, 90), (100, 1110)]
    elif mode == 10:
        parameters = [100, 10, 200, 100, 1, 1, 0, 10000]
        branches = [(10, 21), (30, 1040), (1050, 1061)]
    elif mode == 11:
        parameters = [99998, 1, 99999, 10000, 1, 1, 10000, 10000]
        branches = [(1, 40002), (40003, 80004)]
    else:
        parameters = [100, 1, 200, 1, 1, 1, 10000, 0]
        branches = [(1 + 3 * index, 3 + 3 * index) for index in range(1000)]
    assert 1 <= len(branches) <= 1000
    assert all(0 < value < MAX_POSITION for value in parameters[:6])
    assert parameters[0] < parameters[2] and all(
        0 <= value <= 10000 for value in parameters[6:]
    )
    previous = 0
    for left, right in branches:
        assert previous < left and left + parameters[1] < right < MAX_POSITION
        previous = right
    print(*parameters)
    print(len(branches))
    for left, right in branches:
        print(left, right)


if __name__ == "__main__":
    main()
