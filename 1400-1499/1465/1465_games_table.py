"""Regenerate the winning-position bit mask used by the optimized solver."""

LIMIT = 200
TAKE = 3


def main():
    grundy = [0] * (LIMIT + 1)
    for size in range(1, LIMIT + 1):
        reachable = {0} if size == 1 else set()
        if size >= 2:
            reachable.add(grundy[size - 2])
        reachable.update(
            grundy[left] ^ grundy[size - TAKE - left] for left in range(size - TAKE + 1)
        )
        while grundy[size] in reachable:
            grundy[size] += 1
    print(hex(sum(1 << index for index, value in enumerate(grundy) if value)))


if __name__ == "__main__":
    main()
