import sys


def can_crash(length, height, gate_height, speed, gate_speed, deceleration):
    stopping_bound = gate_speed * (speed * speed + 2 * deceleration * length)
    passing_bound = 2 * deceleration * speed * (gate_height - height)
    return stopping_bound >= passing_bound


if __name__ == "__main__":
    values = map(int, sys.stdin.buffer.read().split())
    print("Crash" if can_crash(*values) else "Safe")
