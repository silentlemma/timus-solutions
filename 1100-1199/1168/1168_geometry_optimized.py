from math import isqrt
import sys

EPS = 1e-6
SKY = 10**6
RADIUS_INDEX = 3
SQUARED_CROSS_TERM = 4


def remove_containing_spheres(stations):
    if not stations:
        return stations
    stations.sort(key=lambda station: station[RADIUS_INDEX])
    ai, aj, az, radius_squared = stations[0]
    essential = [stations[0]]
    for station in stations[1:]:
        i, j, z, reach = station
        separation = (i - ai) ** 2 + (j - aj) ** 2 + (z - az) ** 2
        # reach >= (sqrt(radius_squared) + sqrt(separation)) ** 2.
        margin = reach - radius_squared - separation
        if margin < 0 or margin * margin < SQUARED_CROSS_TERM * radius_squared * separation:
            essential.append(station)
    return essential


def placements(rows, columns, heights, stations):
    occupied = {i * columns + j for i, j, _, _ in stations}
    stations = remove_containing_spheres(stations)
    square = [d * d for d in range(max(rows, columns))]
    total = 0
    for i in range(rows):
        # One subtraction per station and row, shared by every column.
        bands = [(j, z, reach - square[abs(i - si)]) for si, j, z, reach in stations]
        for j in range(columns):
            cell = i * columns + j
            if cell in occupied:
                continue
            low, high = heights[cell], SKY
            for sj, z, reach in bands:
                rest = reach - square[abs(j - sj)]
                if rest < 0:
                    break
                farthest = high - z
                if z - low > farthest:
                    farthest = z - low
                if farthest * farthest <= rest:
                    continue
                extent = isqrt(rest)
                lower, upper = z - extent, z + extent
                if lower > low:
                    low = lower
                if upper < high:
                    high = upper
                if low > high:
                    break
            else:
                total += high - low + 1
    return total


def main():
    fields = iter(sys.stdin.buffer.read().split())
    rows, columns, count = int(next(fields)), int(next(fields)), int(next(fields))
    heights = [int(next(fields)) for _ in range(rows * columns)]
    stations = []
    for _ in range(count):
        i, j, radius = int(next(fields)) - 1, int(next(fields)) - 1, float(next(fields))
        stations.append((i, j, heights[i * columns + j], int(radius * radius + EPS)))
    print(placements(rows, columns, heights, stations))


if __name__ == "__main__":
    main()
