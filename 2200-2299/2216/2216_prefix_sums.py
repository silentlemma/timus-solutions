import sys


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    floors, elevators = next(values), next(values)
    difference = [0] * (floors + 1)
    for left, right in zip(values, values):
        difference[left] += 1
        difference[right] -= 1
    if floors == 1:
        print(-1)
        return

    crossing = 0
    answer = elevators
    # Every route crosses each gap; cover all elevators crossing the cheapest gap.
    for floor in range(1, floors):
        crossing += difference[floor]
        if crossing < answer:
            answer = crossing
    print(answer)


if __name__ == "__main__":
    main()
