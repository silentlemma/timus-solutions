from sys import stdin


scored, conceded, games = map(int, stdin.buffer.readline().split())
margin = scored - conceded
if margin < 0:
    best = games - 1
    worst = max(0, games + margin)
else:
    best = games + 2 * min(margin, games)
    worst = games + 2 * bool(margin)
if scored and conceded and games >= 2:
    # Reserve a match for the opposite outcome in each extreme.
    best = max(best, games - 1 + 2 * min(scored, games - 1))
    worst = min(worst, games + 2 - min(conceded, games - 1))
print(best, worst)
