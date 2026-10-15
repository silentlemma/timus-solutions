def main():
    pages, cover, start, stop = map(int, input().split())
    # on a shelf a volume's first page faces its right neighbour and its
    # last page faces the left one
    whole = pages + 2 * cover
    if start == stop:
        length = pages
    elif start < stop:
        length = 2 * cover + (stop - start - 1) * whole
    else:
        length = 2 * pages + 2 * cover + (start - stop - 1) * whole
    print(length)


main()
