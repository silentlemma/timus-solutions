"""A random agency from a seed and a mode. Mode 1 is small, mode 2 has 26
agents, 50 cars and 2000 events, mostly deliveries, mode 3 has cars that break on the way,
mode 4 has agents that tire soon and newcomers taking their letters, mode
5 has demanding quests that need a pair of agents. At most 26 agents and
50 cars ever appear, and the quests are spread out in time."""

import random
import string
import sys

LETTERS = string.ascii_uppercase
MOST_AGENTS = 26
MOST_CARS = 50
USED = 50  # the largest distance a car has passed when it is listed
FAR = 800  # the farthest quest
EVADE = 500  # the largest evasiveness
VALUE = 500  # the largest experience value of a monster
QUESTS = ["run", "kill", "findout", "talk"]
RUNS = 0.85  # the share of deliveries in the big agency


def char(rng, low=1, high=99):
    return "%.2f" % (rng.randint(low, high) / 100)


def name(rng):
    first = rng.choice(string.ascii_letters + string.digits)
    return first + "".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(0, 6)))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    big = mode == 2
    start_agents = MOST_AGENTS if big else rng.randint(1, 6)
    later_agents = 0 if big else rng.randint(0, MOST_AGENTS - start_agents)
    types = rng.randint(1, 8)
    start_cars = MOST_CARS if big else rng.randint(0, 6)
    later_cars = 0 if big else rng.randint(0, 6)
    kinds = rng.randint(1, 6)
    events = 2000 if big else rng.randint(1, 60)
    low_skill = 60 if mode == 5 else 1
    names = set()

    def fresh():
        while True:
            n = name(rng)
            if n not in names:
                names.add(n)
                return n

    lines = [str(start_agents)]
    for letter in rng.sample(LETTERS, start_agents):
        stats = " ".join(char(rng, 1, low_skill if mode == 5 else 99) for _ in range(5))
        lines.append("%s %s %s" % (fresh(), stats, letter))
    type_names = [fresh() for _ in range(types)]
    limit = 300 if mode == 3 else 5000
    lines.append(str(types))
    distance = {}
    for t in type_names:
        distance[t] = rng.randint(1, limit)
        lines.append("%s %d %s" % (char(rng, 0, 60), distance[t], t))

    def car():
        # a type, the distance already passed (at most the type's), an id
        t = rng.choice(type_names)
        return "%s %d %s" % (t, rng.randint(0, min(USED, distance[t])), fresh())

    lines.append(str(start_cars))
    lines += [car() for _ in range(start_cars)]
    monster_names = [fresh() for _ in range(kinds)]
    lines.append(str(kinds))
    hard = 70 if mode == 5 else 30
    for m in monster_names:
        lines.append(
            "%s %s %d %d %s"
            % (
                char(rng, 0, hard),
                char(rng, 0, hard),
                rng.randint(1, EVADE),
                rng.randint(1, VALUE),
                m,
            )
        )
    retire = "0.50" if mode == 4 else "0.99"
    # the walking limit covers a quest there and back, the others every monster
    lines.append(
        "%d %d %d %s"
        % (rng.randint(2 * FAR, 3 * FAR), EVADE, rng.randint(VALUE, 6 * VALUE), retire)
    )
    lines.append(str(events + later_agents + later_cars))
    kinds_of_event = ["quest"] * events + ["newagent"] * later_agents + ["newcar"] * later_cars
    rng.shuffle(kinds_of_event)
    time = 0
    for kind in kinds_of_event:
        time += rng.randint(1, 400)
        if kind == "newagent":
            lines.append(
                "%d newagent %s %s" % (time, fresh(), " ".join(char(rng) for _ in range(5)))
            )
        elif kind == "newcar":
            lines.append("%d newcar %s" % (time, car()))
        else:
            dist = rng.randint(1, FAR)
            # in the big agency most quests are deliveries, which give no
            # experience, so that the agents do not all tire
            quest = "run" if big and rng.random() < RUNS else rng.choice(QUESTS)
            if quest == "run":
                lines.append("%d quest run %d" % (time, dist))
            elif quest == "kill":
                lines.append("%d quest kill %d %s" % (time, dist, rng.choice(monster_names)))
            else:
                need = char(rng, 0, hard)
                lines.append(
                    "%d quest %s %d %s %d" % (time, quest, dist, need, rng.randint(1, 300))
                )
    print("\n".join(lines))


main()
