"""Checker: "No solution." exactly when expected; otherwise an elbow at
distance a from the shoulder (the origin) and b from the claw, the
claw on the rail's axis with both segments across the axis, and the
bend angle at the elbow in [pi/2, pi], all within 1e-6."""

import math
import sys

EPS = 1e-6
DIM = 3
NONE = "No solution."


class Bad(Exception):
    pass


def check(source, expected, output):
    data = [int(w) for w in open(source).read().split()]
    a, b = data[0], data[1]
    p = data[2:2 + DIM]
    d = [data[2 + DIM + i] - p[i] for i in range(DIM)]
    want = open(expected).read().strip()
    got = open(output).read().strip()
    if want == NONE or got == NONE:
        if want != got:
            raise Bad("expected %r, got %r" % (want[:30], got[:30]))
        return
    values = [float(w) for w in got.split()]
    if len(values) != DIM + 1:
        raise Bad("expected the elbow and the angle")
    elbow, angle = values[:DIM], values[DIM]
    norm_d = math.sqrt(sum(x * x for x in d))
    unit = [x / norm_d for x in d]
    if abs(math.sqrt(sum(x * x for x in elbow)) - a) > EPS:
        raise Bad("the upper arm is not a long")
    if abs(sum(x * y for x, y in zip(elbow, unit))) > EPS:
        raise Bad("the upper arm is not across the rail")
    # the claw: the rail's point in the plane through the elbow across the rail
    t = sum((elbow[i] - p[i]) * unit[i] for i in range(DIM))
    claw = [p[i] + t * unit[i] for i in range(DIM)]
    fore = [claw[i] - elbow[i] for i in range(DIM)]
    if abs(math.sqrt(sum(x * x for x in fore)) - b) > EPS:
        raise Bad("the forearm does not reach the rail")
    cos_bend = -sum(x * y for x, y in zip(elbow, fore)) / (a * b)
    real = math.acos(max(-1.0, min(1.0, cos_bend)))
    if abs(real - angle) > EPS or not math.pi / 2 - EPS <= angle <= math.pi + EPS:
        raise Bad("the bend angle is %.9f, not %.9f" % (real, angle))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
