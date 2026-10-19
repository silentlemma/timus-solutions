"""Usage: gen.py SEED MODE; length30,ascii,missing,priority,duplicates,sessions,keywords,random."""

import random
import sys

LIMIT = 100
MAX_LENGTH = 30
FIRST_ASCII = 33
AFTER_ASCII = 127


def generate(seed, mode):
    alphabet = "".join(chr(i) for i in range(FIRST_ASCII, AFTER_ASCII))
    if mode == "length30":
        return [
            (
                "register",
                "N" + str(i).zfill(MAX_LENGTH - 1),
                "!" * (MAX_LENGTH - 1) + alphabet[i % len(alphabet)],
            )
            for i in range(LIMIT)
        ]
    if mode == "ascii":
        commands = [("register", ch, alphabet[-i - 1]) for i, ch in enumerate(alphabet)]
        commands += [("login", alphabet[i], alphabet[-i - 1]) for i in range(LIMIT - len(commands))]
        return commands
    if mode == "missing":
        return [("logout", str(i)) if i % 2 else ("login", str(i), "p") for i in range(LIMIT)]
    if mode == "duplicates":
        return (
            [("register", "u", "p"), ("login", "u", "p")]
            + [("register", "u", "q")] * (LIMIT - 4)
            + [("login", "u", "q"), ("login", "u", "p")]
        )
    if mode == "priority":
        cycle = [
            ("register", "u", "p"),
            ("login", "u", "p"),
            ("login", "u", "q"),
            ("login", "u", "p"),
            ("logout", "u"),
            ("logout", "u"),
        ]
        return [cycle[i % len(cycle)] for i in range(LIMIT)]
    if mode == "sessions":
        return [("register", "u", "p")] + [
            ("login", "u", "p") if i % 2 else ("logout", "u") for i in range(LIMIT - 1)
        ]
    rng = random.Random(seed)
    names = ["register", "login", "logout", "None", "null", "a", "A"]
    if mode == "keywords":
        commands = [("register", name, names[-i - 1]) for i, name in enumerate(names)]
        while len(commands) < LIMIT:
            i = len(commands) % len(names)
            commands.append(("login", names[i], names[-i - 1]))
        return commands
    commands = []
    for _ in range(LIMIT):
        action = rng.choice(("register", "login", "logout"))
        name = rng.choice(names)
        password = "".join(rng.choice(alphabet) for _ in range(MAX_LENGTH))
        commands.append((action, name) if action == "logout" else (action, name, password))
    return commands


if __name__ == "__main__":
    commands = generate(int(sys.argv[1]), sys.argv[2])
    print(len(commands))
    for command in commands:
        print(*command)
