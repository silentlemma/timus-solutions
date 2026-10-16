import sys


def main():
    words = sys.stdin.read().split()
    groups, pots = int(words[0]), int(words[1])
    total = groups * pots
    # each team is an edge from its pot to its party; a colouring of the
    # edges with one colour per group, never repeated at a vertex, is an
    # answer
    pairs = words[2:2 + 2 * total]
    team = pairs[0::2]
    party_id = {}
    party = [party_id.setdefault(name, len(party_id)) for name in pairs[1::2]]
    pot = [e // groups for e in range(total)]
    size = [0] * len(party_id)
    for v in party:
        size[v] += 1
    if max(size) > groups:
        print("No")
        return
    # at_pot[u][c], at_party[v][c]: the edge of colour c; free_*: bit masks
    # of the colours not used yet
    at_pot = [[-1] * groups for _ in range(pots)]
    at_party = [[-1] * groups for _ in range(len(party_id))]
    everything = (1 << groups) - 1
    free_pot = [everything] * pots
    free_party = [everything] * len(party_id)
    colour = [-1] * total
    for e in range(total):
        u, v = pot[e], party[e]
        a = (free_pot[u] & -free_pot[u]).bit_length() - 1
        b = (free_party[v] & -free_party[v]).bit_length() - 1
        if a != b:
            # colour a is free at the pot and b at the party; swap a and b
            # along the path from the pot that alternates b and a, which
            # cannot reach the party, and b becomes free at both ends
            path = []
            at, want, on_pot = u, b, True
            while True:
                f = at_pot[at][want] if on_pot else at_party[at][want]
                if f < 0:
                    break
                path.append(f)
                at = party[f] if on_pot else pot[f]
                on_pot = not on_pot
                want = a + b - want
            swap = (1 << a) | (1 << b)
            for f in path:
                at_pot[pot[f]][colour[f]] = -1
                at_party[party[f]][colour[f]] = -1
            for f in path:
                c = a + b - colour[f]
                colour[f] = c
                at_pot[pot[f]][c] = f
                at_party[party[f]][c] = f
            # inside the path both colours stay used; at its far end they
            # trade places
            if path:
                last = path[-1]
                if len(path) % 2 == 1:
                    free_party[party[last]] ^= swap
                else:
                    free_pot[pot[last]] ^= swap
                free_pot[u] ^= swap
        colour[e] = b
        at_pot[u][b] = e
        at_party[v][b] = e
        free_pot[u] &= ~(1 << b)
        free_party[v] &= ~(1 << b)
    members = [[None] * pots for _ in range(groups)]
    for e in range(total):
        members[colour[e]][pot[e]] = team[e]
    out = ["Yes"]
    for group in members:
        out.append("")
        out.extend(group)
    print("\n".join(out))


main()
