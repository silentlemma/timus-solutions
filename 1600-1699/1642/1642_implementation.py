def main():
    data = list(map(int, open(0).read().split()))
    x, walls = data[1], data[2:]
    # the nearest obstacles on both sides; walking away from the exit is
    # promised to meet one, so the one needed below always exists
    left = max((w for w in walls if w < 0), default=None)
    right = min((w for w in walls if w > 0), default=None)
    if (left is not None and x < left) or (right is not None and x > right):
        print("Impossible")  # an obstacle stands between the start and the exit
    elif x > 0:
        print(x, -2 * left + x)
    else:
        print(2 * right - x, -x)


main()
