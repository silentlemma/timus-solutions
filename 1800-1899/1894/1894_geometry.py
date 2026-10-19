import math
import sys

SNAPSHOT_AGE = 60


def rotate(points):
    start = min(range(len(points)), key=lambda i: (points[i][1], points[i][0]))
    return points[start:] + points[:start]


def main():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    airport = rotate([tuple(map(int, read().split())) for _ in range(n)])
    cloud = []
    for _ in range(m):
        x, y = map(int, read().split())
        cloud.append((-x, -y))
    cloud = rotate(cloud)
    airport.append(airport[0])
    cloud.append(cloud[0])
    x, y = airport[0][0] + cloud[0][0], airport[0][1] + cloud[0][1]
    i = j = 0
    distance = math.inf
    while i < n or j < m:
        ax = airport[i + 1][0] - airport[i][0] if i < n else 0
        ay = airport[i + 1][1] - airport[i][1] if i < n else 0
        bx = cloud[j + 1][0] - cloud[j][0] if j < m else 0
        by = cloud[j + 1][1] - cloud[j][1] if j < m else 0
        turn = ax * by - ay * bx
        take_airport = i < n and (j == m or turn >= 0)
        take_cloud = j < m and (i == n or turn <= 0)
        dx = ax * take_airport + bx * take_cloud
        dy = ay * take_airport + by * take_cloud
        # The origin is inside the sum, so its nearest supporting line is sufficient.
        distance = min(distance, (x * dy - y * dx) / math.hypot(dx, dy))
        x += dx
        y += dy
        i += take_airport
        j += take_cloud
    print(f"{max(0.0, distance - SNAPSHOT_AGE):.10f}")


main()
