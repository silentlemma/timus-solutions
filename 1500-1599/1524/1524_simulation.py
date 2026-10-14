import heapq
import math
import sys

EPS = 1e-9  # rounding to the closest minute must not suffer from 0.4999999
HALF = 0.5
MINUTES_IN_HOUR = 60
MINUTES_IN_DAY = 24 * MINUTES_IN_HOUR
TRAITS = 5  # accuracy, walking speed, intelligence, experience, driving skill
RUN = "run"
KILL = "kill"
FINDOUT = "findout"
TALK = "talk"
# message kinds in the order they are printed within one minute
BOUGHT = 1
BROKEN = 2
KILLED = 3
FINISHED = 4
TIRED = 5
JOINED = 6
STARTED = 7
WAITING, UNDER_WAY, DONE = "waiting", "under way", "done"
NONE = -1


def minutes(x):
    return int(math.floor(x + HALF + EPS))


class Agent:
    def __init__(self, name, traits, letter):
        self.name, self.letter = name, letter
        self.acc, self.walk, self.intel, self.exp, self.drive = traits
        self.busy, self.alive = False, True


class CarType:
    def __init__(self, need, limit, name):
        self.need, self.limit, self.name = need, limit, name


class Car:
    def __init__(self, kind, passed, ident, limit):
        self.kind, self.passed, self.id = kind, passed, ident
        self.busy, self.broken = False, passed >= limit


class Monster:
    def __init__(self, need_exp, need_int, evade, value, name):
        self.need_exp, self.need_int = need_exp, need_int
        self.evade, self.value, self.name = evade, value, name


class Quest:
    def __init__(self, kind, dist, monster=0, need=0.0, mint=0):
        self.kind, self.dist, self.monster = kind, dist, monster
        self.need, self.mint, self.state = need, mint, WAITING


class Stats:
    def __init__(self, walk, drive, acc, exp, intel):
        self.walk, self.drive, self.acc, self.exp, self.intel = walk, drive, acc, exp, intel


class Plan:
    """A team with its car (or none) and the moments of the quest counted
    from its start; NONE where there is no such moment."""

    def __init__(self, team, car, total, broke, kill, walked, drove):
        self.team, self.car, self.total = team, car, total
        self.broke, self.kill, self.walked, self.drove = broke, kill, walked, drove


class Outside:
    """An outside event: a new agent, a bought car or a received quest."""

    def __init__(self, time, word):
        self.time, self.word = time, word
        self.name = self.id = None
        self.traits, self.passed, self.quest = None, 0, None


def main():
    words = sys.stdin.read().split()
    pos = 0

    def take():
        nonlocal pos
        pos += 1
        return words[pos - 1]

    def traits():
        return [float(take()) for _ in range(TRAITS)]

    agents = []
    for _ in range(int(take())):
        name = take()
        agents.append(Agent(name, traits(), take()))
    types, type_of = [], {}
    for _ in range(int(take())):
        need, limit, name = float(take()), int(take()), take()
        type_of[name] = len(types)
        types.append(CarType(need, limit, name))
    cars = []
    for _ in range(int(take())):
        kind, passed, ident = type_of[take()], int(take()), take()
        cars.append(Car(kind, passed, ident, types[kind].limit))
    monsters, monster_of = [], {}
    for _ in range(int(take())):
        need_exp, need_int = float(take()), float(take())
        evade, value, name = int(take()), int(take()), take()
        monster_of[name] = len(monsters)
        monsters.append(Monster(need_exp, need_int, evade, value, name))
    max_walk, max_evade, max_value = int(take()), int(take()), int(take())
    retire = float(take())
    events = []
    for _ in range(int(take())):
        e = Outside(int(take()), take())
        if e.word == "newagent":
            e.name = take()
            e.traits = traits()
        elif e.word == "newcar":
            e.name, e.passed, e.id = take(), int(take()), take()
        else:
            kind = take()
            e.quest = Quest(kind, int(take()))
            if kind == KILL:
                e.quest.monster = monster_of[take()]
            elif kind != RUN:
                e.quest.need, e.quest.mint = float(take()), int(take())
        events.append(e)

    quests = []
    active = {}  # quest number -> plan
    timeline = []  # (moment, kind of event, quest number)
    log = []

    def letters(team):
        return "".join(agents[a].letter for a in team)

    def team_text(team):
        return " and agent ".join(
            "Agent " * (i == 0) + agents[a].letter for i, a in enumerate(team)
        )

    def team_stats(team):
        a = agents[team[0]]
        if len(team) == 1:
            return Stats(a.walk, a.drive, a.acc, a.exp, a.intel)
        b = agents[team[1]]
        return Stats(
            min(a.walk, b.walk),
            max(a.drive, b.drive),
            (a.acc + b.acc) / 2,
            1 - (1 - a.exp) * (1 - b.exp),
            1 - (1 - a.intel) * (1 - b.intel),
        )

    def action_time(q, st):
        """The time of the work at the place, or None when the team may not do it."""
        if q.kind == KILL:
            m = monsters[q.monster]
            feasible = st.exp >= m.need_exp and st.intel >= m.need_int
            return minutes(m.evade / st.acc) if feasible else None
        if q.kind == FINDOUT:
            return minutes(q.mint / st.intel) if st.intel >= q.need else None
        if q.kind == TALK:
            return minutes(q.mint / st.exp) if st.exp >= q.need else None
        return 0

    def with_car(team, q, action, st, c):
        car = cars[c]
        t = types[car.kind]
        rest, d = t.limit - car.passed, q.dist
        if rest <= 0 or st.drive < t.need:
            return None

        def by_car(x):
            return minutes(x / st.drive)

        def on_foot(x):
            return minutes(x / st.walk)

        broke = NONE
        if rest < d:  # breaks on the way there, the rest is walked
            there = by_car(rest) + on_foot(d - rest)
            back = on_foot(d)
            broke, walked, drove = by_car(rest), 2 * d - rest, rest
        elif rest == d:  # breaks on arrival
            there, back = by_car(d), on_foot(d)
            broke, walked, drove = there, d, d
        elif rest < 2 * d:  # breaks on the way back
            there = by_car(d)
            back = by_car(rest - d) + on_foot(2 * d - rest)
            broke, walked, drove = there + action + by_car(rest - d), 2 * d - rest, rest
        else:
            there = back = by_car(d)
            walked, drove = 0, 2 * d
            if rest == 2 * d:  # breaks on return
                broke = there + action + back
        kill = there + action if q.kind == KILL else NONE
        return Plan(team, c, there + action + back, broke, kill, walked, drove)

    def best_for_team(team, q, short_cars, long_cars):
        """short_cars may break on the trip; long_cars, sorted by id, will
        not, so they all take the same time and the first one the team may
        drive stands for them all."""
        st = team_stats(team)
        action = action_time(q, st)
        if action is None:
            return None
        there = minutes(q.dist / st.walk)
        kill = there + action if q.kind == KILL else NONE
        best = Plan(team, NONE, 2 * there + action, NONE, kill, 2 * q.dist, 0)
        first_long = next((c for c in long_cars if types[cars[c].kind].need <= st.drive), None)
        for c in short_cars + ([first_long] if first_long is not None else []):
            p = with_car(team, q, action, st, c)
            # a car only when strictly faster, then the smaller id
            if p and (
                p.total < best.total
                or (p.total == best.total and best.car != NONE and cars[c].id < cars[best.car].id)
            ):
                best = p
        return best

    def better(a, b):
        if b is None:
            return True
        return (a.total, len(a.team), letters(a.team)) < (b.total, len(b.team), letters(b.team))

    def best_plan(q):
        free = sorted(
            (i for i, a in enumerate(agents) if a.alive and not a.busy),
            key=lambda i: agents[i].letter,
        )
        free_cars = sorted(
            (
                i
                for i, c in enumerate(cars)
                if not c.broken and not c.busy and c.passed < types[c.kind].limit
            ),
            key=lambda i: cars[i].id,
        )
        teams = [[a] for a in free] + [[a, b] for i, a in enumerate(free) for b in free[i + 1 :]]
        longer = [types[cars[c].kind].limit - cars[c].passed > 2 * q.dist for c in free_cars]
        short_cars = [c for c, far in zip(free_cars, longer) if not far]
        long_cars = [c for c, far in zip(free_cars, longer) if far]
        best = None
        for team in teams:
            p = best_for_team(team, q, short_cars, long_cars)
            if p and better(p, best):
                best = p
        return best

    def start(num, q, p, now):
        q.state = UNDER_WAY
        active[num] = p
        if p.broke != NONE:
            heapq.heappush(timeline, (now + p.broke, BROKEN, num))
        if p.kill != NONE:
            heapq.heappush(timeline, (now + p.kill, KILLED, num))
        heapq.heappush(timeline, (now + p.total, FINISHED, num))
        for a in p.team:
            agents[a].busy = True
        text = "%s started quest %d" % (team_text(p.team), num)
        if p.car != NONE:
            cars[p.car].busy = True
            text += " using car %s" % cars[p.car].id
        log.append((STARTED, text + "."))

    def finish(num):
        p = active.pop(num)
        q = quests[num - 1]
        log.append((FINISHED, "%s finished quest %d." % (team_text(p.team), num)))
        if p.car != NONE:
            car = cars[p.car]
            if not car.broken:
                car.busy = False
                car.passed = min(car.passed + p.drove, types[car.kind].limit)
        tired = []
        for i in p.team:
            a = agents[i]
            a.busy = False
            acc, walk, intel, exp, drive = a.acc, a.walk, a.intel, a.exp, a.drive
            if p.walked > 0:
                a.walk = walk + (1 - walk) * p.walked / max_walk
            if p.car != NONE and p.drove > 0:
                a.drive = drive + (1 - drive) * p.drove / max_walk
            if q.kind == KILL:
                m = monsters[q.monster]
                a.exp = exp + (1 - exp) * m.value / max_value
                a.acc = acc + (1 - acc) * m.evade / max_evade
            elif q.kind == FINDOUT:
                a.exp = exp + (1 - exp) * intel / q.mint
                a.intel = intel + (1 - intel) * intel / q.mint
            elif q.kind == TALK:
                a.exp = exp + (1 - exp) * exp / q.mint
            if a.alive and a.exp >= retire:
                a.alive = False
                tired.append(a.letter)
        for letter in sorted(tired):
            log.append((TIRED, "Agent %s has tired." % letter))
        q.state = DONE

    def new_letter(name):
        used = {a.letter for a in agents if a.alive}
        target = ord(name[0].upper())
        free = [chr(c) for c in range(ord("A"), ord("Z") + 1) if chr(c) not in used]
        return min(free, key=lambda c: (abs(ord(c) - target), c))

    out = []
    nxt = 0
    while nxt < len(events) or timeline:
        now = min(
            events[nxt].time if nxt < len(events) else math.inf,
            timeline[0][0] if timeline else math.inf,
        )
        log = []
        while timeline and timeline[0][0] == now:
            _, kind, num = heapq.heappop(timeline)
            if num not in active:
                continue  # a moment that came after the quest had ended
            p = active[num]
            if kind == BROKEN:
                car = cars[p.car]
                if not car.broken:
                    car.broken, car.busy = True, False
                    car.passed = types[car.kind].limit
                    log.append((BROKEN, "Car %s was broken." % car.id))
            elif kind == KILLED:
                name = monsters[quests[num - 1].monster].name
                log.append((KILLED, "%s killed monster %s." % (team_text(p.team), name)))
            else:
                finish(num)
        if nxt < len(events) and events[nxt].time == now:
            e = events[nxt]
            nxt += 1
            if e.word == "newagent":
                letter = new_letter(e.name)
                agents.append(Agent(e.name, e.traits, letter))
                log.append((JOINED, "New agent %s got a letter %s." % (e.name, letter)))
            elif e.word == "newcar":
                kind = type_of[e.name]
                cars.append(Car(kind, e.passed, e.id, types[kind].limit))
                log.append((BOUGHT, "MIB bought a car of class %s." % e.name))
            else:
                quests.append(e.quest)
        # all quests that can start now, the earliest received first
        started = True
        while started:
            started = False
            for num, q in enumerate(quests, 1):
                if q.state == WAITING:
                    p = best_plan(q)
                    if p:
                        start(num, q, p, now)
                        started = True
                        break
        stamp = "%04d:%02d:%02d" % (
            now // MINUTES_IN_DAY,
            now % MINUTES_IN_DAY // MINUTES_IN_HOUR,
            now % MINUTES_IN_HOUR,
        )
        out += ["%s    %s\n" % (stamp, text) for _, text in sorted(log)]
    sys.stdout.write("".join(out))


main()
