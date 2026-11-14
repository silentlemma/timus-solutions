SQRT_EXPONENT = 0.5


def main():
    with open(0, "rb", closefd=False) as stream:
        count, height = stream.read().split()
    last = int(count) - 1
    first = float(height)

    # A/k + k is minimized at one of the two integers around sqrt(A).
    k = int(first**SQRT_EXPONENT)
    if k >= last:
        print("0.00")
        return
    if first > k * (k + 1):
        k += 1

    # Subtract the height at the binding lamp, whose height is zero.
    print(f"{(last - k) * (last - first / k):.2f}")


main()
