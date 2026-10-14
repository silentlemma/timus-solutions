HUNDRED = 100  # times are kept in hundredths of a second, exactly
STAND = 15 * HUNDRED  # the lift stands this long on the first floor
BOARD = 5 * HUNDRED  # getting into the lift


def hundredths(word):
    """A number with at most two decimals, as an exact integer of hundredths."""
    whole, _, frac = word.partition(".")
    return int(whole) * HUNDRED + int((frac + "00")[:2])


def main():
    n_word, k_word, u_word, v_word = input().split()
    n, k = int(n_word), int(k_word)
    u, v = hundredths(u_word), hundredths(v_word)
    # walking all the way down needs no lift
    best_floor, best_time = 1, (n - 1) * u
    ready = (k - 1) * v + STAND  # the lift may leave the first floor from then on
    for f in range(2, n + 1):
        # Petya calls the lift on reaching floor f; it comes up, waits for
        # the boarding and goes down again
        start = max(ready, (n - f) * u)
        total = start + (f - 1) * v + BOARD + (f - 1) * v
        # a later floor means less walking, so ties go to it
        if total <= best_time:
            best_floor, best_time = f, total
    print(best_floor)


main()
