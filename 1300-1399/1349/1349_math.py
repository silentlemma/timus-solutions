ANSWERS = {1: "1 2 3", 2: "3 4 5"}  # by Fermat's last theorem nothing else exists


def main():
    print(ANSWERS.get(int(input()), "-1"))


main()
