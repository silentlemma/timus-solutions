import sys

LEVELS = ("Easy", "Medium", "Hard")  # Diff 1, 2, 3: periods of 1000, 500, 250 ms
SLOWEST = 1000
BASE_SCORE = 10**6
NAMES = ("Perfect", "Great", "Good", "Boo", "Miss")
PERFECT, GREAT, GOOD, BOO, MISS = range(len(NAMES))
SCORE = (10, 5, 0, 0, 0)  # p
COMBO = (55, 33, 0, 0, 0)  # q
DANCE = (2, 1, 0, -4, -5)  # dance points
PERCENT = 100
TENTHS = 10
PERFECT_TENTHS = 4  # under 40 % of the period
GREAT_TENTHS = 7  # under 70 %
# level bonuses: share of the most dance points needed, in percent
SHARES = ((80, 100000), (64, 10000), (50, 1000))
ALL_PERFECT = 10**7
ALL_GREAT = 10**6
LOW = 100
SEPARATOR = "--------------------"


def main():
    lines = sys.stdin.read().split("\n")
    level = LEVELS.index(lines[0].split()[1])
    beats = lines[1].strip()
    log = sorted((int(t), a) for t, a in (line.split() for line in lines[2:] if line.strip()))
    diff, period = level + 1, SLOWEST >> level
    steps = sum(1 for b in beats if b != "N")
    unit = diff * BASE_SCORE // (steps * (steps + 1) // 2)  # B div S
    counts = [0] * len(NAMES)
    stage = combo_bonus = combo = points = 0
    went_negative = False
    n = 0
    k = 0  # the first logged press not before the current beat
    for i, beat in enumerate(beats):
        start, end = i * period, (i + 1) * period
        while k < len(log) and log[k][0] < start:
            k += 1
        if beat == "N":
            continue
        n += 1
        # only the first press within the beat counts
        if k == len(log) or log[k][0] >= end:
            mark = BOO
        elif log[k][1] != beat:
            mark = MISS
        else:
            elapsed = log[k][0] - start
            if TENTHS * elapsed < PERFECT_TENTHS * period:
                mark = PERFECT
            elif TENTHS * elapsed < GREAT_TENTHS * period:
                mark = GREAT
            else:
                mark = GOOD
        counts[mark] += 1
        stage += SCORE[mark] * n * unit
        combo = combo + 1 if mark <= GOOD else 0
        combo_bonus += COMBO[mark] * combo
        points += DANCE[mark]
        went_negative = went_negative or points < 0
    most = DANCE[PERFECT] * steps
    if went_negative:
        bonus = 0
    elif counts[PERFECT] == steps:
        bonus = ALL_PERFECT
    elif counts[PERFECT] + counts[GREAT] == steps:
        bonus = ALL_GREAT
    else:
        bonus = next((b for share, b in SHARES if PERCENT * points >= share * most), LOW)
    out = ["%s: %d" % (name, c) for name, c in zip(NAMES, counts)]
    out.append(SEPARATOR)
    out.append("Stage Score: %d" % stage)
    out.append("Combo Bonus: %d" % combo_bonus)
    out.append("Dance Level Bonus: %d" % bonus)
    out.append("Total Score: %d" % (stage + combo_bonus + bonus))
    print("\n".join(out))


main()
