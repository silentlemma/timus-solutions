"""Checker: the first word must match the reference. After VICTORIOUS the
hero's spells are played turn by turn against the monsters' rule; the
pack must die from the last spell, with the hero alive and with mana
left for every spell, and no spells may follow its death."""

import sys


def fail(message):
    print(message)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    data = list(map(int, open(inp).read().split()))
    n, hp_hero, mana, hp_monster, count, speed, heal = data[:7]
    bolt = [0] + data[7 : 7 + n]
    want = open(ans).read().split()[0]
    lines = [line.split() for line in open(output).read().splitlines() if line.strip()]
    if not lines or lines[0] != [lines[0][0]] or lines[0][0] not in ("VICTORIOUS", "DEFEATED"):
        fail("the first line must be VICTORIOUS or DEFEATED")
    if lines[0][0] != want:
        fail("answered %s, expected %s" % (lines[0][0], want))
    if want == "DEFEATED":
        if len(lines) != 1:
            fail("extra lines after DEFEATED")
        return
    hp, pack, pos = hp_hero, count * hp_monster, n
    for turn, spell in enumerate(lines[1:], 1):
        if pack <= 0:
            fail("spell %d comes after the monsters are dead" % turn)
        if mana == 0:
            fail("no mana left for spell %d" % turn)
        mana -= 1
        if spell == ["L"]:
            pack -= bolt[pos]
        elif spell == ["H"]:
            hp = min(hp_hero, hp + heal)
        elif len(spell) == 2 and spell[0] == "T" and spell[1].isdigit() and 1 <= int(spell[1]) <= n:
            pos = int(spell[1])
        else:
            fail("bad spell %r" % " ".join(spell))
        if pack <= 0:
            continue
        pos -= min(speed, pos - 1)
        if pos == 1:
            hp -= (pack + hp_monster - 1) // hp_monster
        if hp <= 0:
            fail("the hero falls after spell %d" % turn)
    if pack > 0:
        fail("the monsters survive")


if __name__ == "__main__":
    main()
