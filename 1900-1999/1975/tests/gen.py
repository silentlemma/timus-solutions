"""Independent fixture certification and maximal-input generator.

Usage: python gen.py SEED MODE
Modes: certify checks every stored expected answer independently; ring,
latitude and polar print regular 200-point rings; generic prints a seeded
200-point asymmetric sphere set with an identity-only certificate.
"""

import itertools
import math

EPS = 1e-6


def dot(a, b):
    return math.fsum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def length(p):
    return math.sqrt(dot(p, p))


def angle(a, b):
    return math.atan2(length(cross(a, b)), dot(a, b))


def det(a, b, c):
    return dot(a, cross(b, c))


def principal_quaternion(source, target):
    s = [
        [math.fsum(p[i] * q[j] for p, q in zip(source, target)) for j in range(3)]
        for i in range(3)
    ]
    xx, xy, xz = s[0]
    yx, yy, yz = s[1]
    zx, zy, zz = s[2]
    a = [
        [xx + yy + zz, yz - zy, zx - xz, xy - yx],
        [yz - zy, xx - yy - zz, xy + yx, xz + zx],
        [zx - xz, xy + yx, -xx + yy - zz, yz + zy],
        [xy - yx, xz + zx, yz + zy, -xx - yy + zz],
    ]
    vectors = [[float(i == j) for j in range(4)] for i in range(4)]
    for _ in range(80):
        p, q = max(
            itertools.combinations(range(4), 2), key=lambda ij: abs(a[ij[0]][ij[1]])
        )
        value = a[p][q]
        if abs(value) < 1e-30:
            break
        tau = (a[q][q] - a[p][p]) / (2 * value)
        t = math.copysign(1, tau) / (abs(tau) + math.hypot(1, tau))
        c = 1 / math.sqrt(1 + t * t)
        sine = t * c
        a[p][p] -= t * value
        a[q][q] += t * value
        a[p][q] = a[q][p] = 0.0
        for k in range(4):
            if k not in (p, q):
                oldp, oldq = a[k][p], a[k][q]
                a[k][p] = a[p][k] = c * oldp - sine * oldq
                a[k][q] = a[q][k] = sine * oldp + c * oldq
            oldp, oldq = vectors[k][p], vectors[k][q]
            vectors[k][p] = c * oldp - sine * oldq
            vectors[k][q] = sine * oldp + c * oldq
    column = max(range(4), key=lambda i: a[i][i])
    q = tuple(row[column] for row in vectors)
    magnitude = length(q)
    return tuple(x / magnitude for x in q)


def rotate(p, q):
    scalar = q[0]
    vector = q[1:]
    first = cross(vector, p)
    second = cross(vector, first)
    return tuple(a + 2 * scalar * b + 2 * c for a, b, c in zip(p, first, second))


def all_permutations(points, certified_mappings=()):
    n = len(points)
    assert n <= 8
    angles = [[angle(a, b) for b in points] for a in points]
    triples = list(itertools.combinations(range(n), 3))
    chosen = max(triples, key=lambda ids: abs(det(*(points[i] for i in ids))))
    orientation = det(*(points[i] for i in chosen))
    angular_tol = 4 * math.asin(EPS / (2 * min(map(length, points))))
    triple = [points[i] for i in chosen]
    volume_tol = EPS * sum(
        length(cross(triple[i], triple[j])) for i, j in ((0, 1), (0, 2), (1, 2))
    )
    volume_tol += EPS * EPS * sum(map(length, triple)) + EPS**3
    volume_tol = volume_tol * (1 + 1e-8) + 1e-20
    accepted = []
    unresolved = []
    angle_rejections = volume_rejections = 0
    pairs = list(itertools.combinations(range(n), 2))
    for permutation in itertools.permutations(range(n)):
        if any(
            abs(angles[i][j] - angles[permutation[i]][permutation[j]])
            > angular_tol + 1e-12
            for i, j in pairs
        ):
            angle_rejections += 1
            continue
        if (
            abs(orientation - det(*(points[permutation[i]] for i in chosen)))
            > volume_tol
        ):
            volume_rejections += 1
            continue
        if permutation in certified_mappings:
            accepted.append(permutation)
            continue
        target = [points[i] for i in permutation]
        quaternion = principal_quaternion(points, target)
        residuals = [
            length(tuple(x - y for x, y in zip(rotate(p, quaternion), q)))
            for p, q in zip(points, target)
        ]
        if max(residuals) <= EPS + 2e-15:
            accepted.append(permutation)
        else:
            unresolved.append(
                {"mapping": permutation, "max_l2_witness_error": max(residuals)}
            )
    return {
        "accepted": accepted,
        "unresolved": unresolved,
        "permutations": math.factorial(n),
        "angle_rejections": angle_rejections,
        "proper_orientation_rejections": volume_rejections,
    }


def signed_axis_witnesses(baseline, points):
    from fractions import Fraction

    exact = [tuple(Fraction(f"{v:.9f}") for v in p) for p in points]
    accepted = set()
    for axes in itertools.permutations(range(3)):
        parity = (-1) ** sum(
            axes[i] > axes[j] for i in range(3) for j in range(i + 1, 3)
        )
        for signs in itertools.product((-1, 1), repeat=3):
            if parity * math.prod(signs) != 1:
                continue
            mapping = []
            for p in baseline:
                rotated = tuple(sign * p[axis] for sign, axis in zip(signs, axes))
                distances = [
                    sum((a - b) ** 2 for a, b in zip(rotated, q)) for q in baseline
                ]
                target = min(range(len(baseline)), key=lambda j: distances[j])
                if distances[target] > 1e-20:
                    break
                mapping.append(target)
            if len(mapping) != len(points):
                continue
            assert len(set(mapping)) == len(points)
            for i, j in enumerate(mapping):
                rotated = tuple(
                    sign * exact[i][axis] for sign, axis in zip(signs, axes)
                )
                assert sum((a - b) ** 2 for a, b in zip(rotated, exact[j])) <= Fraction(
                    1, 10**12
                )
            accepted.add(tuple(mapping))
    return accepted


def planar_ring_witnesses(points):
    n = len(points)
    assert n % 2 == 1 and all(p[2] == 0 for p in points)
    angles = [math.atan2(p[1], p[0]) for p in points]
    radii = list(map(length, points))
    accepted = set()
    for direction in (-1, 1):
        for shift in range(n):
            mapping = tuple((shift + direction * i) % n for i in range(n))
            center = angles[mapping[0]] - direction * angles[0]
            lower = -math.inf
            upper = math.inf
            for i, j in enumerate(mapping):
                difference = angles[j] - direction * angles[i]
                difference = (
                    center + (difference - center + math.pi) % (2 * math.pi) - math.pi
                )
                radial = abs(radii[i] - radii[j])
                if radial > EPS:
                    lower = math.inf
                    break
                chord = math.sqrt((EPS * EPS - radial * radial) / (radii[i] * radii[j]))
                tolerance = 2 * math.asin(chord / 2)
                lower = max(lower, difference - tolerance)
                upper = min(upper, difference + tolerance)
            if lower > upper:
                continue
            phi = (lower + upper) / 2
            c = math.cos(phi)
            s = math.sin(phi)
            for i, j in enumerate(mapping):
                x, y, z = points[i]
                rotated = (
                    c * x - direction * s * y,
                    s * x + direction * c * y,
                    direction * z,
                )
                assert (
                    length(tuple(a - b for a, b in zip(rotated, points[j])))
                    <= EPS + 2e-15
                )
            accepted.add(mapping)
    return accepted


def unique_fingerprint_certificate(points):
    table = [[angle(p, q) for q in points] for p in points]
    fingerprints = list(map(sorted, table))
    angular = 4 * math.asin(EPS / (2 * min(map(length, points)))) + 1e-12
    minimum = math.inf
    ambiguous = []
    for i, j in itertools.combinations(range(len(points)), 2):
        gap = max(abs(a - b) for a, b in zip(fingerprints[i], fingerprints[j]))
        minimum = min(minimum, gap)
        if gap <= angular:
            ambiguous.append((i, j))
    allowed = [{i} for i in range(len(points))]
    for i, j in ambiguous:
        allowed[i].add(j)
        allowed[j].add(i)
    rejected = []
    changed = True
    while changed:
        changed = False
        fixed = [i for i, row in enumerate(allowed) if len(row) == 1]
        for i, row in enumerate(allowed):
            for target in list(row):
                if target == i:
                    continue
                for anchor in fixed:
                    if (
                        target == anchor
                        or abs(table[i][anchor] - table[target][anchor]) > angular
                    ):
                        row.remove(target)
                        rejected.append((i, target, anchor))
                        changed = True
                        break
    return {
        "all_fingerprints_unique": not ambiguous,
        "minimum_worst_gap": minimum,
        "necessary_tolerance": angular,
        "pairs_checked": len(points) * (len(points) - 1) // 2,
        "ambiguous_pairs": ambiguous,
        "refined_all_points_fixed": all(row == {i} for i, row in enumerate(allowed)),
        "fixed_anchor_refinement_rejections": rejected,
    }


def read_points(path):
    data = iter(path.read_text().split())
    n = int(next(data))
    return [tuple(float(next(data)) for _ in range(3)) for _ in range(n)]


def ring_certificate(points, expected):
    n = len(points)
    lengths = [
        [length(tuple(a - b for a, b in zip(p, q))) for q in points] for p in points
    ]
    largest_edge = max(lengths[i][(i + 1) % n] for i in range(n))
    smallest_nonedge = min(
        lengths[i][j]
        for i in range(n)
        for j in range(n)
        if (i - j) % n not in (0, 1, n - 1)
    )
    # A rotation preserves all cycle edges: no nonedge is within its allowed error.
    assert largest_edge + 2 * EPS < smallest_nonedge
    chosen = (0, n // 3, 2 * n // 3)
    triple = [points[i] for i in chosen]
    original_volume = det(*triple)
    volume_bound = EPS * sum(
        length(cross(triple[i], triple[j])) for i, j in ((0, 1), (0, 2), (1, 2))
    )
    volume_bound += EPS * EPS * sum(map(length, triple)) + EPS**3
    witnessed = excluded = 0
    for direction in (-1, 1):
        for shift in range(n):
            phi = 2 * math.pi * shift / n
            c, s = math.cos(phi), math.sin(phi)
            mapping = [(shift + direction * i) % n for i in range(n)]
            errors = []
            for (x, y, z), j in zip(points, mapping):
                rotated = (
                    c * x - direction * s * y,
                    s * x + direction * c * y,
                    direction * z,
                )
                errors.append(length(tuple(a - b for a, b in zip(rotated, points[j]))))
            if max(errors) <= EPS + 2e-15:
                witnessed += 1
            else:
                target_volume = det(*(points[mapping[i]] for i in chosen))
                assert (
                    abs(original_volume - target_volume)
                    > volume_bound * (1 + 1e-8) + 1e-20
                )
                excluded += 1
    assert witnessed == expected and witnessed + excluded == 2 * n
    return {
        "cycle_automorphisms_checked": 2 * n,
        "explicit_witnesses": witnessed,
        "proper_volume_exclusions": excluded,
    }


def certify():
    from pathlib import Path
    import json

    directory = Path(__file__).resolve().parent
    cases = json.loads((directory / "tests.json").read_text())["cases"]
    points_by_note = {
        case["note"]: read_points(directory / (case["name"] + ".in")) for case in cases
    }
    examined = 0
    for case in cases:
        note = case["note"]
        points = points_by_note[note]
        expected = int((directory / (case["name"] + ".out")).read_text())
        assert 3 <= len(points) <= 200
        assert (
            min(
                length(tuple(a - b for a, b in zip(p, q)))
                for i, p in enumerate(points)
                for q in points[i + 1 :]
            )
            >= 1e-5
        )
        if len(points) <= 8:
            certificates = set()
            if note.startswith("angular_perturbation_"):
                certificates = planar_ring_witnesses(points)
            if note.startswith("perturbed_"):
                certificates = signed_axis_witnesses(
                    points_by_note[note[len("perturbed_") :]], points
                )
            result = all_permutations(points, certificates)
            assert not result["unresolved"], (note, result["unresolved"])
            assert len(result["accepted"]) == expected, note
            examined += result["permutations"]
        elif "irregular" in note or "fingerprints" in note:
            result = unique_fingerprint_certificate(points)
            assert result["refined_all_points_fixed"] and expected == 1, note
        else:
            ring_certificate(points, expected)
    print(
        json.dumps(
            {
                "all_passed": True,
                "fixtures": len(cases),
                "tiny_permutations_examined": examined,
                "unresolved": 0,
            }
        )
    )


def main():
    import random
    import sys

    seed, mode = int(sys.argv[1]), sys.argv[2]
    if mode == "certify":
        certify()
        return
    rng = random.Random(seed)
    n = 200
    if mode in ("ring", "latitude", "polar"):
        radius = (
            0.0004
            if mode == "polar"
            else math.sqrt(1 - 0.3**2)
            if mode == "latitude"
            else 1.0
        )
        height = (
            math.sqrt(1 - radius**2)
            if mode == "polar"
            else 0.3
            if mode == "latitude"
            else 0.0
        )
        offset = rng.random() * 2 * math.pi
        points = [
            (
                radius * math.cos(offset + 2 * math.pi * i / n),
                radius * math.sin(offset + 2 * math.pi * i / n),
                height,
            )
            for i in range(n)
        ]
    elif mode == "generic":
        while True:
            points = []
            for _ in range(n):
                z = rng.uniform(-1, 1)
                phi = rng.random() * 2 * math.pi
                radius = math.sqrt(1 - z * z)
                points.append((radius * math.cos(phi), radius * math.sin(phi), z))
            points = [tuple(float(f"{v:.9f}") for v in p) for p in points]
            separated = (
                min(
                    length(tuple(a - b for a, b in zip(p, q)))
                    for i, p in enumerate(points)
                    for q in points[i + 1 :]
                )
                >= 1e-5
            )
            if (
                separated
                and unique_fingerprint_certificate(points)["refined_all_points_fixed"]
            ):
                break
    else:
        raise SystemExit("unknown mode: " + mode)
    print(n)
    for p in points:
        print(" ".join(f"{v:.9f}" for v in p))


if __name__ == "__main__":
    main()
