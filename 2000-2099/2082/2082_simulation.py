import sys


STREETS = ("preflop", "flop", "turn", "river")


class Game:
    def __init__(self, stacks, dealer, small, big, ante):
        self.stacks = [max(0, stack - ante) for stack in stacks]
        self.count = len(stacks)
        self.dealer = dealer
        self.bets = [0] * self.count
        self.folded = [False] * self.count
        small_seat = dealer if self.count == 2 else (dealer + 1) % self.count
        big_seat = (small_seat + 1) % self.count
        for seat, amount in ((small_seat, small), (big_seat, big)):
            paid = min(self.stacks[seat], amount)
            self.stacks[seat] -= paid
            self.bets[seat] = paid
        self.current = big
        self.street = 0
        self.cursor = (big_seat + 1) % self.count
        self.pending = [stack > 0 for stack in self.stacks]

    def deal(self):
        self.street += 1
        self.current = 0
        self.bets = [0] * self.count
        self.pending = [
            not self.folded[seat] and self.stacks[seat] > 0 for seat in range(self.count)
        ]
        self.cursor = (self.dealer + 1) % self.count

    def play(self, seat, action, paid):
        if action == "folds":
            self.folded[seat] = True
        else:
            self.stacks[seat] -= paid
            self.bets[seat] += paid
            if self.bets[seat] > self.current:
                self.current = self.bets[seat]
                self.pending = [
                    not self.folded[player] and self.stacks[player] > 0
                    for player in range(self.count)
                ]
        self.pending[seat] = False
        self.cursor = (seat + 1) % self.count


def main():
    lines = iter(sys.stdin.read().splitlines())
    small, big, ante = map(int, next(lines).split())
    count, dealer, bot = map(int, next(lines).split())
    dealer -= 1
    bot -= 1
    target = STREETS.index(next(lines).strip())
    names = []
    stacks = []
    for _ in range(count):
        name, stack = next(lines).split()
        names.append(name)
        stacks.append(int(stack))
    game = Game(stacks, dealer, small, big, ante)
    indices = {name: seat for seat, name in enumerate(names)}
    known = int(next(lines))
    for _ in range(known):
        words = next(lines).split()
        if words[0] == "dealing":
            game.deal()
            continue
        seat = indices[words[0]]
        action = words[1]
        paid = 0
        if action == "raises":
            paid = int(words[-1]) - game.bets[seat]
        elif action in ("calls", "bets"):
            paid = int(words[2])
        game.play(seat, action, paid)
    final = list(map(int, next(lines).split()))
    answer = []
    while True:
        if not any(game.pending):
            game.deal()
            answer.append("dealing " + STREETS[game.street])
        while not game.pending[game.cursor]:
            game.cursor = (game.cursor + 1) % count
        seat = game.cursor
        if seat == bot and game.street == target and game.stacks == final:
            break
        paid = game.stacks[seat] - final[seat]
        # A completed street cannot contain a raise after the bot's last action.
        if game.street < target and seat != bot:
            paid = min(paid, game.current - game.bets[seat])
        total = game.bets[seat] + paid
        if paid == 0:
            action = "checks" if total == game.current else "folds"
            text = action
        elif game.current == 0:
            action = "bets"
            text = f"bets {paid}"
        elif total > game.current:
            action = "raises"
            text = f"raises {total - game.current} to {total}"
        else:
            action = "calls"
            text = f"calls {paid}"
        answer.append(names[seat] + " " + text)
        game.play(seat, action, paid)
    sys.stdout.write(str(len(answer)) + "\n")
    if answer:
        sys.stdout.write("\n".join(answer) + "\n")


if __name__ == "__main__":
    main()
