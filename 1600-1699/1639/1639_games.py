def main():
    m, n = map(int, input().split())
    # every break adds one piece, so the game always lasts m * n - 1 moves
    print("[:=[first]" if (m * n - 1) % 2 else "[second]=:]")


main()
