import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    taken = [int(x) for x in data[1 : n + 1]]
    # the pocket is a stack: roll the balls in order, and whenever the top
    # one is the next ball the inspector took out, take it out
    pocket = []
    nxt = 0
    for ball in range(1, n + 1):
        pocket.append(ball)
        while pocket and nxt < n and pocket[-1] == taken[nxt]:
            pocket.pop()
            nxt += 1
    print("Not a proof" if nxt == n else "Cheater")


main()
