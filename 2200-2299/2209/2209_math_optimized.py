def main():
    depth, position = map(int, input().split())
    path = position - 1
    leading_left = depth - 1 - path.bit_length()
    left = right = 1
    # Work back from the final mediant to its coefficients on the initial bounds.
    while path:
        if path & 1:
            right += left
        else:
            left += right
        path >>= 1
    print(right, left + leading_left * right)


if __name__ == "__main__":
    main()
