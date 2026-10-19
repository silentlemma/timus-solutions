"""Usage: gen.py SEED MODE; exact small traces and maximum resource families."""

import itertools
import random
import sys

MAXIMUM = 100000
MAX_MODES = (
    "all_yes",
    "all_no",
    "updates",
    "mixed",
    "mixed_yes",
    "whole_yes",
    "varied_yes",
    "late_no",
    "nonuniform",
    "symmetric_ranges",
)


def render(word, operations):
    return word + "\n" + str(len(operations)) + "\n" + "\n".join(operations) + "\n"


def literal_answers(word, operations):
    letters = list(word)
    answers = []
    for operation in operations:
        kind, left, right = operation.split()
        if kind == "change":
            letters[int(left) - 1] = right
        else:
            first, last = int(left) - 1, int(right) - 1
            while first < last and letters[first] == letters[last]:
                first += 1
                last -= 1
            answers.append("Yes" if first >= last else "No")
    return answers


def generate(seed, mode):
    rng = random.Random(seed)
    if mode.startswith("exhaustive") or mode == "ternary":
        size = 5 if mode == "ternary" else int(mode[len("exhaustive") :])
        if not 5 <= size <= 8:
            raise ValueError("exhaustive size must be between 5 and 8")
        alphabet = "abc" if mode == "ternary" else "ab"
        word = "a" * size
        operations = []
        for target in itertools.product(alphabet, repeat=size):
            for position, value in enumerate(target, 1):
                operations.append(f"change {position} {value}")
                operations.extend(
                    f"palindrome? {left} {right}"
                    for left in range(1, size + 1)
                    for right in range(left, size + 1)
                )
        return word, operations, literal_answers(word, operations)
    if mode in ("random", "planted", "boundaries"):
        size = rng.randint(5, 100)
        word = "".join(rng.choice("abcz") for _ in range(size))
        operations = []
        for _ in range(400):
            if mode == "planted" and rng.randrange(5) == 0:
                first = rng.randint(1, size)
                end = rng.randint(first, size)
                half = [rng.choice("az") for _ in range((end - first + 2) // 2)]
                target = (
                    (half + half[::-1])[: end - first + 1]
                    if (end - first + 1) % 2 == 0
                    else half + half[-2::-1]
                )
                for position, value in enumerate(target, first):
                    operations.append(f"change {position} {value}")
                operations.append(f"palindrome? {first} {end}")
            elif rng.randrange(3) == 0:
                position = rng.choice((1, size)) if mode == "boundaries" else rng.randint(1, size)
                operations.append(f"change {position} {rng.choice('abcz')}")
            else:
                first = rng.randint(1, size)
                end = rng.randint(first, size)
                if mode == "boundaries":
                    first, end = rng.choice(
                        ((1, size), (1, 1), (size, size), (1, size - 1), (2, size))
                    )
                operations.append(f"palindrome? {first} {end}")
        return word, operations, literal_answers(word, operations)
    assert mode in MAX_MODES
    size = count = MAXIMUM
    word = "ab" * (size // 2) if mode == "all_no" else "a" * size
    operations, answers = [], []
    if mode in ("whole_yes", "varied_yes", "late_no", "nonuniform", "symmetric_ranges"):
        if mode == "late_no":
            word = word[: size // 2 - 1] + "b" + word[size // 2 :]
        if mode in ("nonuniform", "symmetric_ranges"):
            half = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(size // 2))
            word = half + half[::-1]
        for i in range(count):
            left, end = 1, size
            if mode == "varied_yes":
                left, end = 1 + i % 128, size - (i // 128) % 128
            elif mode == "symmetric_ranges":
                left, end = 1 + i % 128, size - i % 128
            operations.append(f"palindrome? {left} {end}")
        answers = ["No" if mode == "late_no" else "Yes"] * count
    elif mode in ("all_yes", "all_no"):
        operations = ["palindrome? 32768 65535"] * count
        answers = ["Yes" if mode == "all_yes" else "No"] * count
    elif mode == "updates":
        operations = [f"change 1 {'b' if i % 2 == 0 else 'a'}" for i in range(count)]
    elif mode == "mixed":
        for i in range(count // 2):
            operations.extend((f"change 1 {'b' if i % 2 == 0 else 'a'}", "palindrome? 1 65535"))
            answers.append("No" if i % 2 == 0 else "Yes")
    else:
        for i in range(count // 3):
            value = "b" if i % 2 == 0 else "a"
            operations.extend(
                (f"change 1 {value}", f"change {size} {value}", f"palindrome? 1 {size}")
            )
            answers.append("Yes")
        while len(operations) < count:
            operations.append(f"palindrome? 1 {size}")
            answers.append("Yes")
    return word, operations, answers


if __name__ == "__main__":
    initial, commands, _ = generate(int(sys.argv[1]), sys.argv[2])
    sys.stdout.write(render(initial, commands))
