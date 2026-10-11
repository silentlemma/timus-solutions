# Roman digits needed for each decimal digit: -, I, II, III, IV, V, VI,
# VII, VIII, IX
LENGTHS = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2]


def main():
    print(sum(LENGTHS[int(c)] for c in input().strip()))


main()
