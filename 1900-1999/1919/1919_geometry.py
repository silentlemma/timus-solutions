import sys


def fits_orientation(first, second, height, circumference):
    if first > circumference:
        return False
    if second <= height:
        return True
    residual = height * circumference - first * second
    return residual >= 0 and residual * residual >= first * first * (
        circumference * circumference - first * first
    )


def can_block(width, height, cylinder_height, circumference):
    return fits_orientation(
        width, height, cylinder_height, circumference
    ) or fits_orientation(height, width, cylinder_height, circumference)


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    width, height = next(tokens), next(tokens)
    count = next(tokens)
    answer = []
    for _ in range(count):
        cylinder_height, circumference = next(tokens), next(tokens)
        answer.append(
            "Block the hole"
            if can_block(width, height, cylinder_height, circumference)
            else "Too small"
        )
    print("\n".join(answer))


if __name__ == "__main__":
    main()
