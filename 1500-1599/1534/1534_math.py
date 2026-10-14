def main():
    scored, conceded, n = map(int, input().split())
    d = scored - conceded
    # with W wins and R losses the team has n + 2W - R points; the goals
    # split into a common part, scored and conceded alike, plus at least
    # one goal of margin per win and per loss
    if d >= 0:
        # no losses: the margin d covers up to d wins, the rest are draws
        best, worst = n + 2 * min(d, n), (n if d == 0 else n + 2)
    else:
        # no wins: up to -d losses, at least one
        best, worst = n - 1, n - min(-d, n)
    if scored >= 1 and conceded >= 1 and n >= 2:
        # wins and losses together: one goal each is enough, so one loss and
        # a win per goal scored, or one win and a loss per goal conceded
        best = max(best, n - 1 + 2 * min(scored, n - 1))
        worst = min(worst, n + 2 - min(conceded, n - 1))
    print(best, worst)


main()
