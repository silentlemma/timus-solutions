# the counts for N = 1 and N = 2; from N = 3 on, 1575 and N - 3 zeros
SMALL = ["", "14", "155"]
SHORT = 3
BASE = "1575"


def main():
    n = int(input())
    print(SMALL[n] if n < SHORT else BASE + "0" * (n - SHORT))


main()
