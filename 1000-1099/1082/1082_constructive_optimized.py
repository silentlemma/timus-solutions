BATCH = 128


def main():
    n = int(input())
    output = open(1, "w")
    # On sorted numbers every first-element partition peels off one element.
    for first in range(1, n + 1, BATCH):
        if first != 1:
            output.write(" ")
        output.write(" ".join(map(str, range(first, min(first + BATCH, n + 1)))))
    output.write("\n")


main()
