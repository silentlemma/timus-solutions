"""Usage: gen.py SEED MODE; modes: rare, self, chain, zeros, random, dense, single, long_names."""

import random


def render(recipes):
    return "".join(
        name + " : " + " ".join(f"{part} {percent}" for part, percent in sorted(row.items())) + "\n"
        for name, row in sorted(recipes.items())
    )


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == "rare":
        n = 10
        names = ["salad" + chr(97 + i) for i in range(n)]
        recipes = {}
        for i, name in enumerate(names):
            if i + 1 < n:
                recipes[name] = {names[0]: 99, names[i + 1]: 1}
            else:
                recipes[name] = {names[0]: 98, "basea": 1, "baseb": 1}
        return render(recipes)
    if mode == "self":
        return "salad : base 1 salad 99\n"
    if mode == "chain":
        names = ["salad" + chr(97 + i) for i in range(10)]
        return render(
            {
                name: {names[i + 1] if i + 1 < len(names) else "base": 100}
                for i, name in enumerate(names)
            }
        )
    if mode == "zeros":
        return render({"salada": {"basea": 100}, "saladb": {"baseb": 100}})
    assert mode in ("random", "dense", "single", "long_names")
    n = 10 if mode in ("dense", "long_names") else 1 if mode == "single" else rng.randint(1, 10)
    m = 10 if mode in ("dense", "long_names") else rng.randint(1, 10)
    names = ["s" + chr(97 + i) for i in range(n)]
    bases = ["b" + chr(97 + i) for i in range(m)]
    if mode == "long_names":
        names = ["saladname" + chr(97 + i) for i in range(n)]
        bases = ["basenames" + chr(97 + i) for i in range(m)]
    recipes = {}
    for name in names:
        row = {rng.choice(bases): 1}
        for _ in range(99):
            part = rng.choice(names + bases)
            row[part] = row.get(part, 0) + 1
        recipes[name] = row
    return render(recipes)


if __name__ == "__main__":
    import sys

    sys.stdout.write(generate(int(sys.argv[1]), sys.argv[2]))
