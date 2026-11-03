year, teams, remaining = map(int, input().split())
seen = set()
for _ in range(teams):
    team = input().strip()
    university = team.rsplit("#", 1)[0].rstrip().lower()
    if university in seen:
        continue
    if remaining == 0:
        print(team)
        break
    seen.add(university)
    remaining -= 1
