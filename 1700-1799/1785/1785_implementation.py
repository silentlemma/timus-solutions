import sys

# the smallest number for each word, from the largest down
FROM = [1000, 500, 250, 100, 50, 20, 10, 5, 1]
WORDS = ["legion", "zounds", "swarm", "throng", "horde", "lots", "pack", "several", "few"]


def main():
    n = int(sys.stdin.read())
    i = 0
    while n < FROM[i]:
        i += 1
    print(WORDS[i])


main()
