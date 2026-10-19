import sys

HEALTHY = 3
TEAM_SIZE = 4
TRIPLE_SIZE = TEAM_SIZE - 1


def solve():
    source = sys.stdin.buffer
    count = int(source.readline())
    names = [source.readline().strip() for _ in range(count)]
    index = {name: player for player, name in enumerate(names)}
    health = [HEALTHY] * count
    parent = list(range(count))

    def find(player):
        while parent[player] != player:
            parent[player] = parent[parent[player]]
            player = parent[player]
        return player

    for _ in range(int(source.readline())):
        event = source.readline().split()
        actor = index[event[0]]
        action = event[1]
        if health[actor] < 2:
            return b"FAKE\n"
        if action == b"USES":
            health[actor] = HEALTHY
            continue
        target = index[event[2]]
        if action == b"HIT":
            damage = 2 if event[-1] == b"HEAD" else 1
            health[target] = max(0, health[target] - damage)
        else:
            if health[target] != 1:
                return b"FAKE\n"
            health[target] = 2
            first, second = find(actor), find(target)
            parent[max(first, second)] = min(first, second)

    groups = [[] for _ in range(count)]
    for player in range(count):
        groups[find(player)].append(player)
    buckets = [[] for _ in range(TEAM_SIZE + 1)]
    for group in groups:
        if len(group) > TEAM_SIZE:
            return b"FAKE\n"
        if group:
            buckets[len(group)].append(group)
    if len(buckets[1]) < len(buckets[TRIPLE_SIZE]):
        return b"FAKE\n"

    teams = buckets[TEAM_SIZE][:]
    single = 0
    for group in buckets[TRIPLE_SIZE]:
        teams.append(group + buckets[1][single])
        single += 1
    pair = 0
    while pair + 1 < len(buckets[2]):
        teams.append(buckets[2][pair] + buckets[2][pair + 1])
        pair += 2
    if pair < len(buckets[2]):
        teams.append(buckets[2][pair] + buckets[1][single] + buckets[1][single + 1])
        single += 2
    # The remaining singles fill whole teams because the player count is divisible by four.
    while single < len(buckets[1]):
        teams.append([group[0] for group in buckets[1][single : single + TEAM_SIZE]])
        single += TEAM_SIZE
    output = [b"CORRECT"]
    output.extend(b" ".join(names[player] for player in team) for team in teams)
    return b"\n".join(output) + b"\n"


if __name__ == "__main__":
    sys.stdout.buffer.write(solve())
