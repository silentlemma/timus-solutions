from operator import mul

SECONDS = 10
# once a whole line is done with this certainty the rest of the sum is lost
# in rounding
SURE = 1e-15


def main():
    n = int(input())
    m = n - 2
    # done[i]: the chance that i rockets between two launched ones are all
    # launched within the volleys counted so far; a stretch of i rockets
    # splits at a random one into stretches of l and i - 1 - l
    done = [1.0] + [0.0] * m
    volleys = 0.0
    for j in range(1, m + 1):
        volleys += 1 - done[m]
        before = done
        done = [1.0] * (m + 1)
        for i in range(j + 1, m + 1):
            done[i] = sum(map(mul, before[:i], before[i - 1::-1])) / i
        if 1 - done[m] < SURE:
            break
    print("%.11f" % (SECONDS * volleys))


main()
