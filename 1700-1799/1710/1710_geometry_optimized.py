def main():
    with open(0, "rb") as source:
        ax, ay, bx, by, cx, cy = map(int, source.read().split())
    dx, dy = cx - ax, cy - ay
    squared = dx * dx + dy * dy
    # Reflect C about the projection of B onto the line AC.
    other = 2 * ((bx - ax) * dx + (by - ay) * dy) - squared
    if other <= 0 or other == squared:
        print("YES")
    else:
        x = ax + dx * other / squared
        y = ay + dy * other / squared
        print(f"NO\n{ax} {ay}\n{bx} {by}\n{x:.12f} {y:.12f}")


if __name__ == "__main__":
    main()
