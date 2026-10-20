"""Generate a valid log: python gen.py MODE SEED.

Small randomized modes: random, powers, units, left-unit, right-unit, extremes.
The gap mode sends balanced messages with a luck ratio of exactly 1.0001.
Maximal modes: max-online, max-messages, max-cancel, max-joins, max-near,
max-closest. Each maximal mode has 86400 commands; max-near and max-closest
test close valid ratios after large cancellation with unrelated bases.
"""

import random
import sys


DAY_SECONDS = 86400
HOUR_SECONDS = 3600
MINUTE_SECONDS = 60
MAX_MESSAGE = 10
MAX_FACTOR = 10**9
SMALL_MIN = 32
SMALL_MAX = 512
SMALL_USERS = 32
NICK_DIGITS = 5
PAIR_CHOICES = (1, 2, 4, 8, 16, 256, 65536)
FACTOR_FOUR = 4
FACTOR_EIGHT = 8
TERNARY_FACTOR = 3
GAP_FACTOR = 10000
MAX_ONLINE = 30000
MAX_MESSAGE_USERS = 64
CANCEL_GROW = 30000
CANCEL_SHRINK = 20000
NEAR_GROW = 103124
NEAR_SHRINK = 65064
CLOSEST_FIRST = 5
CLOSEST_SECOND = 34
CLOSEST_GROW = 278086
CLOSEST_SHRINK = 126919
PERIOD = 7


def nickname(index):
    return f"aB{index:0{NICK_DIGITS}d}_"


class Log:
    def __init__(self, limit, message_limit, first_factor, second_factor):
        self.limit = limit
        self.message_limit = message_limit
        self.first_factor = first_factor
        self.second_factor = second_factor
        self.lines = []
        self.active = ["admin"]
        self.positions = {"admin": 0}

    def add(self, author, command):
        second = len(self.lines)
        hour, second = divmod(second, HOUR_SECONDS)
        minute, second = divmod(second, MINUTE_SECONDS)
        self.lines.append(f"[{hour:02}:{minute:02}:{second:02}] {author}: /{command}")

    def join(self, name, long_command):
        self.add(name, "join" if long_command else "j")
        if name not in self.positions:
            self.positions[name] = len(self.active)
            self.active.append(name)

    def quit(self, name, long_command):
        self.add(name, "quit" if long_command else "q")
        position = self.positions.pop(name)
        last = self.active.pop()
        if position < len(self.active):
            self.active[position] = last
            self.positions[last] = position

    def emit(self):
        assert len(self.lines) == self.limit
        print(self.limit, self.message_limit, self.first_factor, self.second_factor)
        sys.stdout.write("\n".join(self.lines) + "\n")


def message(rng, limit, balanced=False):
    if balanced:
        return "glhf" * rng.randint(1, limit // FACTOR_FOUR)
    return "".join(rng.choice(("gl", "hf")) for _ in range(rng.randint(1, limit // 2)))


def random_log(mode, rng):
    limit = rng.randint(SMALL_MIN, SMALL_MAX)
    message_limit = rng.randint(1, MAX_MESSAGE // 2) * 2
    first = rng.choice(PAIR_CHOICES)
    second = rng.choice(PAIR_CHOICES)
    if mode == "units":
        first = second = 1
    elif mode == "left-unit":
        first = 1
    elif mode == "right-unit":
        second = 1
    elif mode == "powers":
        first, second = rng.choice(((2, FACTOR_FOUR), (FACTOR_FOUR, FACTOR_EIGHT)))
    elif mode == "extremes":
        first = second = MAX_FACTOR
    elif mode == "gap":
        first, second = GAP_FACTOR + 1, GAP_FACTOR
        message_limit = FACTOR_EIGHT
    log = Log(limit, message_limit, first, second)
    names = [nickname(index) for index in range(SMALL_USERS)]
    names.extend(("Admin", "write", "compare", "w", "c", "Z_9aB_0x"))
    actions = ("join", "quit", "online", "say", "write", "compare")
    for _ in range(limit):
        action = rng.choice(actions)
        author = rng.choice(log.active)
        long_command = rng.choice((False, True))
        if action == "join":
            log.join(rng.choice(names + ["admin"]), long_command)
        elif action == "quit" and author != "admin":
            log.quit(author, long_command)
        elif action == "online" or action == "quit":
            log.add(author, "online" if long_command else "o")
        elif action == "say":
            text = message(rng, message_limit, mode == "gap")
            log.add(author, ("say " if long_command else "s ") + text)
        elif action == "write":
            recipient = rng.choice(names + ["admin", "Never_0"])
            if recipient == author:
                recipient = "Never_1"
            text = message(rng, message_limit, mode == "gap")
            command = "write" if long_command else "w"
            log.add(author, f"{command}<{recipient}> {text}")
        else:
            author = rng.choice(("admin", author))
            first_name = rng.choice(names + ["admin", "Never_0"])
            command = "compare" if long_command else "c"
            argument = f"<{first_name}>"
            if rng.choice((False, True)):
                second_name = rng.choice(names + ["admin", "Never_1"])
                argument += f"-<{second_name}>"
            log.add(author, command + argument)
    return log


def maximal_online(rng):
    log = Log(DAY_SECONDS, MAX_MESSAGE, 2, FACTOR_FOUR)
    for index in range(MAX_ONLINE):
        log.join(nickname(index), bool(index % 2))
    while len(log.lines) < log.limit:
        index = len(log.lines)
        author = rng.choice(log.active)
        if index % PERIOD == 0:
            log.add("admin", f"compare<{author}>-<admin>")
        else:
            log.add(author, "say " + "glhfglhfgl")
    return log


def maximal_messages(rng):
    log = Log(DAY_SECONDS, MAX_MESSAGE, MAX_FACTOR, MAX_FACTOR)
    for index in range(MAX_MESSAGE_USERS):
        log.join(nickname(index), bool(index % 2))
    while len(log.lines) < log.limit:
        index = len(log.lines)
        author = rng.choice(log.active)
        recipient = rng.choice(log.active)
        if index % PERIOD == 0:
            log.add("admin", f"c<{author}>-<{recipient}>")
        elif index % 2 == 0 or author == recipient:
            log.add(author, "s " + rng.choice(("glglglglgl", "hfhfhfhfhf")))
        else:
            text = rng.choice(("glglglhfhf", "hfhfglhfgl"))
            log.add(author, f"write<{recipient}> {text}")
    return log


def maximal_cancel(rng):
    log = Log(DAY_SECONDS, MAX_MESSAGE, FACTOR_FOUR, FACTOR_EIGHT)
    first, second = nickname(0), nickname(1)
    log.join(first, False)
    log.join(second, True)
    for _ in range(CANCEL_GROW):
        log.add("admin", f"write<{first}> glglglglgl")
    for _ in range(CANCEL_SHRINK):
        log.add("admin", f"w<{first}> hfhfhfhfhf")
    log.add("admin", f"compare<{first}>")
    while len(log.lines) < log.limit:
        if len(log.lines) % PERIOD == 0:
            log.add("admin", f"c<{first}>-<{second}>")
        else:
            author = rng.choice(log.active)
            log.add(author, "say glglglhfhf")
    return log


def maximal_joins(rng):
    log = Log(DAY_SECONDS, MAX_MESSAGE, 2, FACTOR_FOUR)
    for index in range(DAY_SECONDS):
        log.join(nickname(index), rng.choice((False, True)))
    return log


def maximal_near(rng):
    return close_ratio(rng, 2, TERNARY_FACTOR, NEAR_GROW, NEAR_SHRINK)


def maximal_closest(rng):
    return close_ratio(rng, CLOSEST_FIRST, CLOSEST_SECOND, CLOSEST_GROW, CLOSEST_SHRINK)


def close_ratio(rng, first_factor, second_factor, grow, shrink):
    log = Log(DAY_SECONDS, MAX_MESSAGE, first_factor, second_factor)
    recipient = nickname(0)
    log.join(recipient, True)
    for count, pair in ((grow, "gl"), (shrink, "hf")):
        full_messages, remainder = divmod(count, MAX_MESSAGE // 2)
        for _ in range(full_messages):
            command = rng.choice(("write", "w"))
            log.add("admin", f"{command}<{recipient}> {pair * (MAX_MESSAGE // 2)}")
        if remainder:
            log.add("admin", f"w<{recipient}> {pair * remainder}")
    arguments = (
        f"<{recipient}>",
        f"<{recipient}>-<admin>",
        f"<admin>-<{recipient}>",
        f"<{recipient}>-<{recipient}>",
        "<admin>",
    )
    while len(log.lines) < log.limit:
        command = rng.choice(("compare", "c"))
        log.add("admin", command + rng.choice(arguments))
    return log


def main():
    mode = sys.argv[1]
    rng = random.Random(int(sys.argv[2]))
    maximal_modes = {
        "max-online": maximal_online,
        "max-messages": maximal_messages,
        "max-cancel": maximal_cancel,
        "max-joins": maximal_joins,
        "max-near": maximal_near,
        "max-closest": maximal_closest,
    }
    if mode in maximal_modes:
        log = maximal_modes[mode](rng)
    else:
        small_modes = {"random", "powers", "units", "left-unit", "right-unit", "extremes", "gap"}
        if mode not in small_modes:
            raise ValueError("unknown mode")
        log = random_log(mode, rng)
    log.emit()


if __name__ == "__main__":
    main()
