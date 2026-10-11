import sys

NEVER = 1 << 30
FIELDS = 7


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, hp_hero, mana, hp_monster, count, speed, heal = data[:FIELDS]
    bolt = [0] + data[FIELDS : FIELDS + n]
    top = count * hp_monster

    def land(p):
        return 1 if p - 1 < speed else p - speed

    def strike(h, p):
        return (h + hp_monster - 1) // hp_monster if p == 1 else 0

    # need[m][h][p] is the fewest hit points the hero needs at the start of
    # a turn with m mana against a pack of h hit points on square p; more
    # hit points never hurt, so this number decides every state
    need = [[[NEVER] * (n + 1) for _ in range(top + 1)] for _ in range(mana + 1)]

    def cost(m, h, p, spell):
        """Hit points a spell needs: 'L', 'H', or a teleport target."""
        cure = 0
        if spell == "L":
            if h <= bolt[p]:
                return 1
            h -= bolt[p]
        elif spell == "H":
            cure = heal
        else:
            p = spell
        q = land(p)
        rest = need[m - 1][h][q]
        if rest == NEVER:
            return NEVER
        req = strike(h, q) + rest
        if not cure:
            return req
        return NEVER if req > hp_hero else max(1, req - cure)

    spells = ["L", "H"] + list(range(1, n + 1))
    for m in range(1, mana + 1):
        for h in range(1, top + 1):
            row = need[m][h]
            for p in range(1, n + 1):
                row[p] = min(cost(m, h, p, s) for s in spells)
    hp, h, p = hp_hero, top, n
    if need[mana][h][p] > hp:
        print("DEFEATED")
        return
    out = ["VICTORIOUS"]
    # replay: any spell whose need the hero meets keeps the win in reach
    m = mana
    while h > 0:
        spell = next(s for s in spells if cost(m, h, p, s) <= hp)
        if spell == "L":
            h -= bolt[p]
        elif spell == "H":
            hp = min(hp_hero, hp + heal)
        else:
            p = spell
        out.append(spell if spell in ("L", "H") else "T %d" % spell)
        if h > 0:
            p = land(p)
            hp -= strike(h, p)
        m -= 1
    print("\n".join(out))


main()
