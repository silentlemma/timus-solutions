def main():
    n = int(input())
    # on sorted numbers every partition peels off just the first one
    print(" ".join(str(i) for i in range(1, n + 1)))


main()
