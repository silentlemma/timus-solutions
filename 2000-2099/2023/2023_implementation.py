import sys

# the three cabinets from left to right, with the names from the statement
CABINETS = [
    "Alice Ariel Aurora Phil Peter Olaf Phoebus Ralph Robin",
    "Bambi Belle Bolt Mulan Mowgli Mickey Silver Simba Stitch",
    "Dumbo Genie Jiminy Kuzko Kida Kenai Tarzan Tiana Winnie",
]

cabinet = {name: i for i, names in enumerate(CABINETS) for name in names.split()}
data = sys.stdin.read().split()
n = int(data[0])
position = steps = 0
for name in data[1 : n + 1]:
    steps += abs(cabinet[name] - position)
    position = cabinet[name]
print(steps)
