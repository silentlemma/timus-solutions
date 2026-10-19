HEIGHT = 6
WIDTH = 11
GRID = (
    ">?v........",
    ".>>.......v",
    "..@A+AB+B-<",
    "..B........",
    "..-........",
    ".^@A!#.....",
)


def main():
    print(HEIGHT, WIDTH)
    print(*GRID, sep="\n")


if __name__ == "__main__":
    main()
