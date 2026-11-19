NAME = b"Sandro"
COINS = 5
CASE = ord("a") ^ ord("A")
ALPHABET = 1 << 8

text = open(0, "rb").read().strip()
windows = len(text) - len(NAME) + 1
costs = []
for offset, target in enumerate(NAME):
    table = bytes(
        COINS * (bool((letter ^ target) & CASE) + ((letter | CASE) != (target | CASE)))
        for letter in range(ALPHABET)
    )
    costs.append(text.translate(table)[offset : offset + windows])
print(min(map(sum, zip(*costs))))
