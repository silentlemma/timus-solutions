import os
import sys

CANS = 3


def reachable(cap):
    a, b, c = cap
    aa, bb, cc = a + 1, b + 1, c + 1
    plane_x = bb * cc
    plane_y = aa * cc
    plane_z = aa * bb
    seen = bytearray(2 * (plane_x + plane_y + plane_z))
    queue = []

    # a state (x, y, z) as one number; every move leaves some can empty or full
    def push(x, y, z):
        if x == 0:
            slot = y * cc + z
        elif x == a:
            slot = plane_x + y * cc + z
        elif y == 0:
            slot = 2 * plane_x + x * cc + z
        elif y == b:
            slot = 2 * plane_x + plane_y + x * cc + z
        elif z == 0:
            slot = 2 * (plane_x + plane_y) + x * bb + y
        else:
            slot = 2 * (plane_x + plane_y) + plane_z + x * bb + y
        if not seen[slot]:
            seen[slot] = 1
            queue.append((x * bb + y) * cc + z)

    volumes = bytearray(a + b + c + 1)
    push(0, 0, 0)
    head = 0
    while head < len(queue):
        state = queue[head]
        head += 1
        xy, z = divmod(state, cc)
        x, y = divmod(xy, bb)
        volumes[x] = volumes[y] = volumes[z] = volumes[x + y] = volumes[x + z] = volumes[
            y + z
        ] = volumes[x + y + z] = 1
        # fill can i from the pump up to the brim
        if x < a:
            push(a, y, z)
        if y < b:
            push(x, b, z)
        if z < c:
            push(x, y, c)
        # pour i into j
        if x and y < b:
            amount = min(x, b - y)
            push(x - amount, y + amount, z)
        if x and z < c:
            amount = min(x, c - z)
            push(x - amount, y, z + amount)
        if y and x < a:
            amount = min(y, a - x)
            push(x + amount, y - amount, z)
        if y and z < c:
            amount = min(y, c - z)
            push(x, y - amount, z + amount)
        if z and x < a:
            amount = min(z, a - x)
            push(x + amount, y, z - amount)
        if z and y < b:
            amount = min(z, b - y)
            push(x, y + amount, z - amount)
    return sum(volumes) - 1


def main():
    print(reachable(list(map(int, sys.stdin.read().split()))))


main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
