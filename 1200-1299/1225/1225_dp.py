def main():
    n = int(input())
    # a row ends in white or red; it comes from a row one shorter ending in
    # the other of the two, or from one two shorter followed by blue
    prev, cur = 2, 2
    for _ in range(n - 2):
        prev, cur = cur, prev + cur
    print(cur)


main()
