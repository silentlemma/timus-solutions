VOTE_SCALE = 20
MAX_VOTE = 10


def votes(current, target, count):
    total = min(MAX_VOTE * count, ((2 * current + 1) * count - 1) // VOTE_SCALE)
    if total < count or VOTE_SCALE * total < (2 * current - 1) * count:
        return "Impossible"

    bound = 2 * target + 1
    return max(0, (VOTE_SCALE * total - bound * count) // (bound - VOTE_SCALE) + 1)


def main():
    current, target, count = map(int, open(0, "rb").read().replace(b".", b"").split())
    print(votes(current, target, count))


if __name__ == "__main__":
    main()
