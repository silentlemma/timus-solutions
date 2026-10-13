def main():
    harry, larry = map(int, input().split())
    # the last can was shot by both, so each missed the other's count minus one
    print(larry - 1, harry - 1)


main()
