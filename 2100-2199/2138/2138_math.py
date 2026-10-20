DIGITS = 4


def main():
    input()
    v = int(input())
    # Both directions reverse the four base-256 digits, so the type does not matter.
    print(int.from_bytes(v.to_bytes(DIGITS, "big"), "little"))


main()
