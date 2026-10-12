import sys

# the sides, in the order cars prefer to turn
SOUTH = 0
NORTH = 1
WEST = 2
EAST = 3


def main():
    lines = sys.stdin.read().split("\n")
    w, h = map(int, lines[0].split())
    width = w + 2
    # the plan with a frame of buildings, as one flat string
    rows = [line.rstrip("\r")[:w].ljust(w, ".") for line in lines[1 : 1 + h]]
    rows += ["." * w] * (h - len(rows))
    plan = "." * width + "".join("." + row + "." for row in rows) + "." * width
    road = [c in "#o" for c in plan]
    # control points numbered from the bottom row up, left to right
    points = [r * width + c + 1 for r in range(h, 0, -1) for c in range(w) if rows[r - 1][c] == "o"]
    steps = [width, -width, -1, 1]  # south, north, west, east
    words = " ".join(lines[1 + h :]).split()
    out = []
    for number, target in enumerate((int(x) for x in words[1 : 1 + int(words[0])]), 1):
        goal = points[target - 1]
        dist = [-1] * len(plan)
        dist[goal] = 0
        order = [goal]
        for cell in order:
            for step in steps:
                near = cell + step
                if road[near] and dist[near] < 0:
                    dist[near] = dist[cell] + 1
                    order.append(near)
        # every cell inherits the side its car arrives from from the cell it
        # moves to; cells one step away arrive straight from their own side
        side = [0] * len(plan)
        for cell in order[1:]:
            for k, step in enumerate(steps):
                near = cell + step
                if dist[near] == dist[cell] - 1 and road[near]:
                    # stepping in one direction onto the goal arrives from the opposite side
                    side[cell] = side[near] if near != goal else k ^ 1
                    break
        counts = [0] * (EAST + 1)
        for p in points:
            if p != goal and dist[p] > 0:
                counts[side[p]] += 1
        out.append(
            "Experiment #%d: North: %d, South: %d, East: %d, West: %d"
            % (number, counts[NORTH], counts[SOUTH], counts[EAST], counts[WEST])
        )
    print("\n".join(out))


main()
