import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # every move adds two heaps, and the game ends when all heaps are ones
    moves = sum((int(a) - 1) // 2 for a in data[1:n + 1])
    print("Daenerys" if moves % 2 == 1 else "Stannis")


main()
