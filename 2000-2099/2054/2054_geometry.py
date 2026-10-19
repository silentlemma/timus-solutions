import math
import sys

MONTHS = (
    b"jan",
    b"feb",
    b"mar",
    b"apr",
    b"may",
    b"jun",
    b"jul",
    b"aug",
    b"sep",
    b"oct",
    b"nov",
    b"dec",
)
LENGTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
SOLSTICE_DAY = 171
HOURS_PER_DAY = 24
HOURS_PER_YEAR = 8760
NOON = 12
TILT_DEGREES = 23.439281


def main():
    fields = iter(sys.stdin.buffer.read().split())
    latitude = math.radians(float(next(fields)))
    count = int(next(fields))
    prefix = {}
    days = 0
    for month, length in zip(MONTHS, LENGTHS):
        prefix[month] = days
        days += length
    tilt = math.radians(TILT_DEGREES)
    equatorial = math.cos(latitude) * math.cos(tilt)
    transverse = math.cos(latitude)
    axial = math.sin(latitude) * math.sin(tilt)
    output = []
    for _ in range(count):
        day, month, hour = int(next(fields)), next(fields), int(next(fields))
        elapsed = (prefix[month] + day - 1 - SOLSTICE_DAY) * HOURS_PER_DAY + hour - NOON
        orbit = math.tau * elapsed / HOURS_PER_YEAR
        spin = orbit + math.tau * (hour - NOON) / HOURS_PER_DAY
        sine = (
            equatorial * math.cos(spin) * math.cos(orbit)
            + transverse * math.sin(spin) * math.sin(orbit)
            + axial * math.cos(orbit)
        )
        angle = math.degrees(math.asin(max(0.0, min(1.0, sine))))
        output.append(f"{angle:.10f}")
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
