import argparse
import random
import sys
from dataclasses import dataclass


MIN_PLAYERS = 2
MAX_PLAYERS = 9
MIN_ALLIN_PLAYERS = 3
SMALL_GAME_PLAYERS = 5
MIN_SMALL_BLIND = 10
MAX_SMALL_BLIND = 500
MIN_BIG_BLIND = 20
MAX_BIG_BLIND = 1000
MAX_ANTE = 100
MAX_STACK = 20000
MAX_HISTORY = 1000
MAX_ATTEMPTS = 200
MAX_RANDOM_RAISES = 4
MAX_RAISE_BLINDS = 4
SHORT_STACK_BLINDS = 4
CHANCE_SCALE = 100
FOLD_CHANCE = 12
RAISE_CHANCE = 38
ALLIN_CHANCE = 60
LATE_RAISE_CHANCE = 18
LATE_MIN_STACK = 12000
LONG_MIN_STACK = 16000
LONG_MIN_RAISES = 500
LONG_MAX_RAISES = 900
MAX_SIM_ACTIONS = MAX_HISTORY + 2 * MAX_PLAYERS + 1
TURN = 2
STREETS = ("preflop", "flop", "turn", "river")
MODES = ("random", "first", "headsup", "full", "allin", "late", "long")


@dataclass
class Event:
    text: str
    player: int
    allin: bool = False


@dataclass
class Snapshot:
    count: int
    street: int
    stacks: tuple[int, ...]


class Game:
    def __init__(self, rng, mode):
        self.rng = rng
        self.mode = mode
        if mode == "headsup":
            self.size = MIN_PLAYERS
        elif mode in ("full", "long"):
            self.size = MAX_PLAYERS
        elif mode == "allin":
            self.size = rng.randint(MIN_ALLIN_PLAYERS, MAX_PLAYERS)
        else:
            self.size = rng.randint(MIN_PLAYERS, SMALL_GAME_PLAYERS)
        self.dealer = rng.randrange(self.size)
        self.bot = rng.randrange(self.size)
        self.anchor = (self.bot + 1) % self.size
        self.small = rng.randint(MIN_SMALL_BLIND, MAX_SMALL_BLIND)
        low_big = max(MIN_BIG_BLIND, self.small + 1)
        self.big = rng.randint(low_big, min(MAX_BIG_BLIND, 2 * self.small))
        self.ante = rng.randint(0, MAX_ANTE)
        self.initial = []
        for player in range(self.size):
            minimum = self.ante + 2 * self.big
            maximum = MAX_STACK
            if mode == "long":
                minimum = LONG_MIN_STACK
            elif mode == "late":
                minimum = LATE_MIN_STACK
            elif mode == "allin" and player not in (self.bot, self.anchor):
                maximum = self.ante + SHORT_STACK_BLINDS * self.big
            self.initial.append(rng.randint(minimum, maximum))
        prefix = "MixedCasePlayerName" if mode == "long" else "Player"
        self.names = [prefix + str(player + 1) for player in range(self.size)]
        self.stacks = [stack - self.ante for stack in self.initial]
        self.live = [True] * self.size
        self.bets = [0] * self.size
        small_player = self.dealer
        if self.size != MIN_PLAYERS:
            small_player = (small_player + 1) % self.size
        big_player = (small_player + 1) % self.size
        for player, blind in ((small_player, self.small), (big_player, self.big)):
            paid = min(self.stacks[player], blind)
            self.stacks[player] -= paid
            self.bets[player] += paid
        self.cap = self.big
        self.pending = set(range(self.size))
        self.next_player = (big_player + 1) % self.size
        self.street = 0
        self.raises = 0
        self.long_raises = rng.randint(LONG_MIN_RAISES, LONG_MAX_RAISES)
        self.history = []
        self.snapshots = []

    def active(self):
        return [player for player in range(self.size) if self.live[player] and self.stacks[player]]

    def actor(self):
        for distance in range(self.size):
            player = (self.next_player + distance) % self.size
            if player in self.pending:
                return player
        return -1

    def choose(self, player):
        owed = max(0, self.cap - self.bets[player])
        stack = self.stacks[player]
        if self.mode == "long":
            if self.street == 0 and self.raises < self.long_raises:
                return "pay", owed + self.rng.randint(1, 2)
            return ("pay", min(owed, stack)) if owed else ("check", 0)
        protected = player in (self.bot, self.anchor)
        can_fold = owed and not protected and self.mode != "late"
        if can_fold and self.rng.randrange(CHANCE_SCALE) < FOLD_CHANCE:
            return "fold", 0
        can_raise = stack > owed and self.raises < MAX_RANDOM_RAISES
        chance = LATE_RAISE_CHANCE if self.mode == "late" else RAISE_CHANCE
        if can_raise and self.rng.randrange(CHANCE_SCALE) < chance:
            maximum = min(stack - owed, self.big * MAX_RAISE_BLINDS)
            raise_by = self.rng.randint(1, maximum)
            if self.mode == "allin" and not protected:
                if self.rng.randrange(CHANCE_SCALE) < ALLIN_CHANCE:
                    raise_by = stack - owed
            return "pay", owed + raise_by
        return ("pay", min(owed, stack)) if owed else ("check", 0)

    def apply(self, player, kind, paid):
        assert player == self.actor()
        assert self.live[player] and self.stacks[player] > 0
        owed = max(0, self.cap - self.bets[player])
        name = self.names[player]
        allin = False
        self.pending.remove(player)
        if kind == "fold":
            assert owed > 0 and paid == 0
            self.live[player] = False
            text = f"{name} folds"
        elif kind == "check":
            assert owed == 0 and paid == 0
            text = f"{name} checks"
        else:
            assert 0 < paid <= self.stacks[player]
            total = self.bets[player] + paid
            allin = paid == self.stacks[player]
            assert total >= self.cap or allin
            if total > self.cap:
                if self.cap == 0:
                    text = f"{name} bets {paid}"
                else:
                    text = f"{name} raises {total - self.cap} to {total}"
                self.cap = total
                self.raises += 1
                self.pending = set(self.active()) - {player}
            else:
                assert owed > 0
                text = f"{name} calls {paid}"
            self.stacks[player] -= paid
            self.bets[player] = total
        self.pending.intersection_update(self.active())
        self.next_player = (player + 1) % self.size
        self.history.append(Event(text, player, allin))
        assert all(stack >= 0 for stack in self.stacks)

    def simulate(self):
        while len(self.history) <= MAX_SIM_ACTIONS:
            if sum(self.live) < MIN_PLAYERS:
                break
            player = self.actor()
            if player == -1:
                if self.street + 1 == len(STREETS) or len(self.active()) < MIN_PLAYERS:
                    break
                self.street += 1
                self.bets = [0] * self.size
                self.cap = 0
                self.raises = 0
                self.pending = set(self.active())
                self.next_player = (self.dealer + 1) % self.size
                text = f"dealing {STREETS[self.street]}"
                self.history.append(Event(text, -1))
                continue
            if player == self.bot and len(self.active()) >= MIN_PLAYERS:
                snapshot = Snapshot(len(self.history), self.street, tuple(self.stacks))
                self.snapshots.append(snapshot)
            kind, paid = self.choose(player)
            self.apply(player, kind, paid)

    def candidates(self):
        result = []
        # Consecutive bot turns leave at most one deal to recover.
        for index, snapshot in enumerate(self.snapshots):
            known = self.snapshots[index - 1].count if index else 0
            if known > MAX_HISTORY:
                continue
            missing = self.history[known : snapshot.count]
            if self.mode == "first" and index:
                continue
            if self.mode == "late" and snapshot.street < TURN:
                continue
            if self.mode == "long" and known < LONG_MIN_RAISES:
                continue
            if self.mode == "allin" and not any(event.allin for event in missing):
                continue
            bot_actions = sum(event.player == self.bot for event in missing)
            deals = sum(event.player == -1 for event in missing)
            assert bot_actions == (1 if index else 0)
            assert deals <= 1
            result.append((known, snapshot))
        return result

    def render(self, known, snapshot):
        lines = [
            f"{self.small} {self.big} {self.ante}",
            f"{self.size} {self.dealer + 1} {self.bot + 1}",
            STREETS[snapshot.street],
        ]
        lines.extend(f"{name} {stack}" for name, stack in zip(self.names, self.initial))
        lines.append(str(known))
        lines.extend(event.text for event in self.history[:known])
        lines.append(" ".join(map(str, snapshot.stacks)))
        missing = [event.text for event in self.history[known : snapshot.count]]
        answer = [str(len(missing)), *missing]
        return "\n".join(lines) + "\n", "\n".join(answer) + "\n"


def generate_case(mode, seed):
    rng = random.Random(seed)
    for _ in range(MAX_ATTEMPTS):
        game = Game(rng, mode)
        game.simulate()
        candidates = game.candidates()
        if candidates:
            known, snapshot = rng.choice(candidates)
            return game.render(known, snapshot)
    raise RuntimeError("could not generate a suitable bot turn")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=MODES)
    parser.add_argument("seed", type=int)
    arguments = parser.parse_args()
    text, _ = generate_case(arguments.mode, arguments.seed)
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
