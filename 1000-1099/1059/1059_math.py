def main():
    n = int(input())
    # Horner's scheme: ((a0 * X + a1) * X + a2) ... in reverse Polish notation
    out = ["0"]
    for i in range(1, n + 1):
        out += ["X", "*", str(i), "+"]
    print("\n".join(out))


main()
