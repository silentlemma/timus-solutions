PER_ATTEMPT = 20  # minutes for each rejected attempt


def main():
    t1, t2, *attempts = map(int, open(0).read().split())
    # without the rejected attempts ZZZ wins only with strictly less time
    clean = t2 - PER_ATTEMPT * sum(attempts)
    print("Dirty debug :(" if clean < t1 else "No chance.")


main()
