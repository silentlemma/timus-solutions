import math
import re
import sys

RADIUS = 6875 / 2
DANGER = 100
MINUTES = 60
SECONDS = 3600
HUNDREDTHS = 100
# degrees^minutes'seconds" followed by NL, SL, EL or WL
COORDINATE = re.compile(r"(\d+)\^(\d+)'(\d+)\" ([NSEW])L")


def main():
    angles = []
    for d, m, s, side in COORDINATE.findall(sys.stdin.read()):
        degrees = int(d) + int(m) / MINUTES + int(s) / SECONDS
        angles.append(math.radians(-degrees if side in "SW" else degrees))
    lat1, lon1, lat2, lon2 = angles
    # the haversine formula keeps its precision for small distances
    h = (
        math.sin((lat2 - lat1) / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    )
    distance = 2 * RADIUS * math.asin(min(1.0, math.sqrt(h)))
    print("The distance to the iceberg: %.2f miles." % distance)
    # the comparison uses the printed value: 99.996 is printed as 100.00
    if round(distance * HUNDREDTHS) < DANGER * HUNDREDTHS:
        print("DANGER!")


main()
