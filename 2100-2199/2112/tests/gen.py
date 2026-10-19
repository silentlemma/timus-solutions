"""Generate deterministic logs; every accepted log has a unique team partition."""

import random
import string
import sys

TEAM_SIZE = 4
HEALTHY = 3
WOUNDED = 2
DYING = 1
MAX_PLAYERS = 1000
MAX_EVENTS = 10000
MAX_NAME = 20
NAME_DIGITS = 3
SMALL_TEAMS = 6
SMALL_EVENTS = 100
RANDOM_EVENTS = 1000
MODE_SMALL = 1
MODE_RANDOM = 2
MODE_MAXIMUM = 3
MODE_BAD_ACTOR = 4
MODE_BAD_REVIVE = 5
MODE_OVERSIZE = 6
MODE_PACKING = 7
MODE_SHAPES = 8
MODE_DEAD_TARGET = 9
MODE_MAXIMUM_BAD = 10


class Log:
    def __init__(self, count, rng, long_names=False):
        self.rng = rng
        self.names = []
        alphabet = string.ascii_letters
        for index in range(count):
            suffix = ""
            value = index
            for _ in range(NAME_DIGITS):
                suffix += alphabet[value % len(alphabet)]
                value //= len(alphabet)
            length = MAX_NAME if long_names else rng.randint(TEAM_SIZE, MAX_NAME)
            padding = "".join(rng.choice(alphabet) for _ in range(length - len(suffix)))
            self.names.append(suffix + padding)
        self.order = list(range(count))
        rng.shuffle(self.order)
        self.members = list(range(count))
        rng.shuffle(self.members)
        self.teams = [self.members[i : i + TEAM_SIZE] for i in range(0, count, TEAM_SIZE)]
        self.team_of = [0] * count
        for index, team in enumerate(self.teams):
            for member in team:
                self.team_of[member] = index
        self.health = [HEALTHY] * count
        self.events = []
        self.anchor = self.members[0]

    def hit(self, actor, target, damage):
        part = "BODY" if damage == 1 else "HEAD"
        self.events.append(f"{self.names[actor]} HIT {self.names[target]} IN {part}")
        self.health[target] = max(0, self.health[target] - damage)

    def medkit(self, actor):
        self.events.append(f"{self.names[actor]} USES MEDKIT")
        self.health[actor] = HEALTHY

    def revive(self, actor, target):
        self.events.append(f"{self.names[actor]} REVIVE {self.names[target]}")
        self.health[target] = WOUNDED

    def connect(self, group, chain=False):
        actor = group[0]
        for target in group[1:]:
            self.hit(actor, target, 2)
            self.revive(actor, target)
            if chain:
                actor = target

    def force_teams(self, partial=False):
        for index, team in enumerate(self.teams):
            if not partial or index != len(self.teams) - 1:
                self.connect(team, self.rng.choice((False, True)))
                continue
            shapes = ((HEALTHY, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1))
            shape = self.rng.choice(shapes)
            start = 0
            for size in shape:
                self.connect(team[start : start + size])
                start += size

    def random_events(self, target_count):
        targets = [player for player in self.members if player != self.anchor]
        while len(self.events) < target_count:
            active = [player for player in self.members if self.health[player] >= WOUNDED]
            actor = self.rng.choice(active)
            action = self.rng.randrange(TEAM_SIZE)
            if action == 0:
                self.medkit(actor)
            elif action < HEALTHY:
                target = self.rng.choice(targets)
                self.hit(actor, target, action)
            else:
                team = self.teams[self.team_of[actor]]
                dying = [player for player in team if self.health[player] == DYING]
                if dying:
                    self.revive(actor, self.rng.choice(dying))
                else:
                    self.medkit(actor)

    def emit(self):
        print(len(self.names))
        print("\n".join(self.names[player] for player in self.order))
        print(len(self.events))
        if self.events:
            print("\n".join(self.events))


def main():
    mode, seed = map(int, sys.argv[1:HEALTHY])
    rng = random.Random(seed)
    if mode in (MODE_SMALL, MODE_RANDOM, MODE_MAXIMUM, MODE_SHAPES, MODE_MAXIMUM_BAD):
        if mode in (MODE_MAXIMUM, MODE_MAXIMUM_BAD):
            count = MAX_PLAYERS
        else:
            maximum = SMALL_TEAMS if mode == MODE_SMALL else MAX_PLAYERS // TEAM_SIZE
            count = TEAM_SIZE * rng.randint(1, maximum)
        log = Log(count, rng, mode in (MODE_MAXIMUM, MODE_MAXIMUM_BAD))
        log.force_teams(mode == MODE_SHAPES)
        maximum = SMALL_EVENTS if mode == MODE_SMALL else RANDOM_EVENTS
        minimum = len(log.events)
        target = rng.randint(minimum, max(minimum, maximum))
        if mode in (MODE_MAXIMUM, MODE_MAXIMUM_BAD):
            target = MAX_EVENTS - (HEALTHY if mode == MODE_MAXIMUM_BAD else 0)
        log.random_events(target)
        if mode == MODE_MAXIMUM_BAD:
            victim = log.members[1]
            while log.health[victim] >= WOUNDED:
                log.hit(log.anchor, victim, 2)
            log.medkit(victim)
            while len(log.events) < MAX_EVENTS:
                log.medkit(log.anchor)
    elif mode == MODE_BAD_ACTOR:
        log = Log(TEAM_SIZE, rng)
        actor, target = log.members[:2]
        log.hit(target, actor, 2)
        if rng.choice((False, True)):
            log.hit(target, actor, 2)
        action = rng.randrange(HEALTHY)
        if action == 0:
            log.medkit(actor)
        elif action == 1:
            log.hit(actor, target, 1)
        else:
            log.revive(actor, target)
    elif mode in (MODE_BAD_REVIVE, MODE_DEAD_TARGET):
        log = Log(TEAM_SIZE, rng)
        actor, target = log.members[:2]
        if mode == MODE_DEAD_TARGET:
            log.hit(actor, target, 2)
            log.hit(actor, target, 2)
        elif rng.choice((False, True)):
            log.hit(actor, target, 1)
        log.revive(actor, target)
    elif mode == MODE_OVERSIZE:
        log = Log(2 * TEAM_SIZE, rng)
        log.connect(log.members[: TEAM_SIZE + 1], rng.choice((False, True)))
    elif mode == MODE_PACKING:
        count = rng.choice((2, HEALTHY)) * TEAM_SIZE
        log = Log(count, rng)
        position = 0
        while position + HEALTHY <= count:
            log.connect(log.members[position : position + HEALTHY])
            position += HEALTHY
        if position < count:
            log.connect(log.members[position:])
    else:
        raise SystemExit("unknown mode")
    log.emit()


if __name__ == "__main__":
    main()
