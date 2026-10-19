import heapq
import math
import sys

DIMENSION = 3
MATCH_FACTOR = 5
WEIGHTED_ITERATIONS = 6
CELL_FACTOR = 10
FIT_ITERATIONS = 12
JACOBI_ITERATIONS = 24
EIGEN_ROUNDOFF_FACTOR = 256
ANGLE_ROUNDOFF = 1e-12
SINGULAR_LIMIT = 1e-30
STEP_LIMIT = 1e-15
MIN_WEIGHT = 1e-10
HALF = 0.5
WEIGHT_POWERS = (0, 1, 2, 4, 8, 16)
EPS = 1e-06
CELL = CELL_FACTOR * EPS
GATE = MATCH_FACTOR * EPS
INV_CELL = 1 / CELL


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def norm(a):
    return math.sqrt(dot(a, a))


def unit(a):
    length = norm(a)
    return tuple((x / length for x in a))


def frame(a, b):
    z = unit(a)
    y = unit(cross(z, unit(b)))
    x = cross(y, z)
    return (x, y, z)


def project(p, basis):
    return tuple((dot(p, axis) for axis in basis))


def unproject(p, basis):
    x, y, z = p
    ex, ey, ez = basis
    return (
        x * ex[0] + y * ey[0] + z * ez[0],
        x * ex[1] + y * ey[1] + z * ez[1],
        x * ex[2] + y * ey[2] + z * ez[2],
    )


def distance2(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    z = a[2] - b[2]
    return x * x + y * y + z * z


def candidates(points):
    n = len(points)
    normalized = list(map(unit, points))
    a = normalized[0]
    b = max(
        range(1, n), key=lambda j: dot(cross(a, normalized[j]), cross(a, normalized[j]))
    )
    sine = norm(cross(a, normalized[b]))
    cosine = dot(a, normalized[b])
    alpha = math.atan2(sine, cosine)
    assert sine > 0
    basis = frame(points[0], points[b])
    source = [project(p, basis) for p in points]
    xx = sum((p[0] * p[0] for p in source))
    yy = sum((p[1] * p[1] for p in source))
    zz = sum((p[2] * p[2] for p in source))
    xy = sum((p[0] * p[1] for p in source))
    xz = sum((p[0] * p[2] for p in source))
    yz = sum((p[1] * p[2] for p in source))
    normal = (
        (yy + zz, -xy, -xz / sine),
        (-xy, xx + zz, -yz / sine),
        (-xz / sine, -yz / sine, (xx + yy) / (sine * sine)),
    )
    minimum_norm = min(map(norm, points))
    e = EPS / minimum_norm
    angular = 2 * math.asin(e / 2)
    angle_cache = {}
    lookup = {}
    for i, p in enumerate(points):
        key = tuple((math.floor(x / CELL) for x in p))
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    lookup.setdefault(
                        (key[0] + dx, key[1] + dy, key[2] + dz), []
                    ).append(i)
    for p in range(n):
        for q in range(n):
            if p == q:
                continue
            target_sine = norm(cross(normalized[p], normalized[q]))
            target_cosine = dot(normalized[p], normalized[q])
            if (
                abs(target_sine - sine) > 2 * angular + ANGLE_ROUNDOFF
                or abs(target_cosine - cosine) > 2 * angular + ANGLE_ROUNDOFF
            ):
                continue
            beta = math.atan2(target_sine, target_cosine)
            if abs(alpha - beta) > 2 * angular + ANGLE_ROUNDOFF or target_sine == 0:
                continue
            target_basis = frame(points[p], points[q])
            mapping = []
            used = set()
            worst = 0.0
            for coordinate in source:
                rotated = unproject(coordinate, target_basis)
                key = (
                    math.floor(rotated[0] * INV_CELL),
                    math.floor(rotated[1] * INV_CELL),
                    math.floor(rotated[2] * INV_CELL),
                )
                best = GATE * GATE
                closest = -1
                for j in lookup.get(key, ()):
                    error = distance2(rotated, points[j])
                    if error < best:
                        best = error
                        closest = j
                if closest < 0 or closest in used:
                    break
                used.add(closest)
                mapping.append(closest)
                worst = max(worst, best)
            if len(mapping) != n:
                continue
            assert mapping[0] == p and mapping[b] == q
            targets = (
                [project(points[j], target_basis) for j in mapping]
                if worst > EPS * EPS
                else None
            )
            theta = 2 * math.asin(min(1.0, e / math.sqrt(sine * target_sine)))
            yield {
                "mapping": tuple(mapping),
                "canonical_error": math.sqrt(worst),
                "source": source,
                "targets": targets,
                "tilt_bound": math.tan(angular),
                "twist_bound": theta,
                "sine": sine,
                "normal": normal,
                "normalized": normalized,
                "angle_cache": angle_cache,
                "angle_tolerance": 2 * angular + ANGLE_ROUNDOFF,
            }


ROUNDOFF_GUARD = 2e-15
NUMERIC_EPS = EPS + ROUNDOFF_GUARD
EPS2 = NUMERIC_EPS * NUMERIC_EPS
MACHINE_EPS = 2.220446049250313e-16
CERTIFICATE_ROUNDOFF = 1e-20
SEARCH_ROUNDOFF = 1e-16


def solve3(matrix, rhs):
    a = [list(row) + [value] for row, value in zip(matrix, rhs)]
    for column in range(DIMENSION):
        pivot = max(range(column, DIMENSION), key=lambda i: abs(a[i][column]))
        if abs(a[pivot][column]) < SINGULAR_LIMIT:
            return None
        a[pivot], a[column] = (a[column], a[pivot])
        divisor = a[column][column]
        a[column] = [x / divisor for x in a[column]]
        for i in range(DIMENSION):
            if i == column:
                continue
            coefficient = a[i][column]
            a[i] = [x - coefficient * y for x, y in zip(a[i], a[column])]
    return [row[DIMENSION] for row in a]


def rotate_set(points, omega):
    angle = norm(omega)
    if angle == 0:
        return list(points)
    s = math.sin(angle) / angle
    v = HALF * (math.sin(angle / 2) / (angle / 2)) ** 2
    x, y, z = omega
    a, b, c = (1 - v * (y * y + z * z), v * x * y - s * z, v * x * z + s * y)
    d, e, f = (v * x * y + s * z, 1 - v * (x * x + z * z), v * y * z - s * x)
    g, h, i = (v * x * z - s * y, v * y * z + s * x, 1 - v * (x * x + y * y))
    return [
        (a * x + b * y + c * z, d * x + e * y + f * z, g * x + h * y + i * z)
        for x, y, z in points
    ]


def quaternion_step(omega, pose):
    angle = norm(omega)
    if angle == 0:
        return pose
    factor = math.sin(angle / 2) / angle
    a = math.cos(angle / 2)
    b, c, d = (value * factor for value in omega)
    w, x, y, z = pose
    result = (
        a * w - b * x - c * y - d * z,
        a * x + b * w + c * z - d * y,
        a * y - b * z + c * w + d * x,
        a * z + b * y - c * x + d * w,
    )
    length = math.sqrt(math.fsum((value * value for value in result)))
    return tuple((value / length for value in result))


def quaternion_apply(points, pose):
    w, x, y, z = pose
    a, b, c = (1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y))
    d, e, f = (2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x))
    g, h, i = (2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y))
    return [
        (a * x + b * y + c * z, d * x + e * y + f * z, g * x + h * y + i * z)
        for x, y, z in points
    ]


def quick_witness(candidate):
    gx = gy = gz = 0.0
    for p, q in zip(candidate["source"], candidate["targets"]):
        x, y, z = p
        ex = q[0] - x
        ey = q[1] - y
        ez = q[2] - z
        gx += y * ez - z * ey
        gy += z * ex - x * ez
        gz += x * ey - y * ex
    scale = candidate["sine"]
    omega = solve3(candidate["normal"], (gx, gy, gz / scale))
    if omega is None:
        return None
    omega[2] /= scale
    return rotate_set(candidate["source"], omega)


def pair_angle_excluded(candidate, index):
    normalized = candidate["normalized"]
    cache = candidate["angle_cache"]
    mapping = candidate["mapping"]
    for anchor in (index, mapping[index]):
        if anchor not in cache:
            p = normalized[anchor]
            cache[anchor] = [
                math.atan2(norm(cross(p, q)), dot(p, q)) for q in normalized
            ]
    source = cache[index]
    target = cache[mapping[index]]
    tolerance = candidate["angle_tolerance"]
    return any((abs(source[i] - target[j]) > tolerance for i, j in enumerate(mapping)))


def residuals(source, targets):
    return [sum(((a - b) ** 2 for a, b in zip(p, q))) for p, q in zip(source, targets)]


def fit(
    source,
    targets,
    scale,
    weights=None,
    iterations=FIT_ITERATIONS,
    pose=(1.0, 0.0, 0.0, 0.0),
):
    current = quaternion_apply(source, pose)
    if weights is None:
        weights = [1.0] * len(source)
    for _ in range(iterations):
        xx = yy = zz = xy = xz = yz = gx = gy = gz = 0.0
        for p, q, weight in zip(current, targets, weights):
            x, y, z = p
            ex = q[0] - x
            ey = q[1] - y
            ez = q[2] - z
            gx += weight * (y * ez - z * ey)
            gy += weight * (z * ex - x * ez)
            gz += weight * (x * ey - y * ex)
            xx += weight * x * x
            yy += weight * y * y
            zz += weight * z * z
            xy += weight * x * y
            xz += weight * x * z
            yz += weight * y * z
        a = (
            (yy + zz, -xy, -xz / scale),
            (-xy, xx + zz, -yz / scale),
            (-xz / scale, -yz / scale, (xx + yy) / (scale * scale)),
        )
        g = (gx, gy, gz / scale)
        omega = solve3(a, g)
        if omega is None:
            break
        omega[2] /= scale
        pose = quaternion_step(omega, pose)
        current = quaternion_apply(source, pose)
        if max(residuals(current, targets)) <= EPS2:
            break
        if norm(omega) < STEP_LIMIT:
            break
    return (current, pose)


def smallest_eigen_lower(matrix):
    a = [list(row) for row in matrix]
    for _ in range(JACOBI_ITERATIONS):
        p, q = max(((0, 1), (0, 2), (1, 2)), key=lambda ij: abs(a[ij[0]][ij[1]]))
        value = a[p][q]
        if abs(value) < SINGULAR_LIMIT:
            break
        tau = (a[q][q] - a[p][p]) / (2 * value)
        t = math.copysign(1, tau) / (abs(tau) + math.hypot(1, tau))
        c = 1 / math.sqrt(1 + t * t)
        s = t * c
        a[p][p] -= t * value
        a[q][q] += t * value
        a[p][q] = a[q][p] = 0.0
        for k in range(DIMENSION):
            if k in (p, q):
                continue
            oldp, oldq = (a[k][p], a[k][q])
            a[k][p] = a[p][k] = c * oldp - s * oldq
            a[k][q] = a[q][k] = s * oldp + c * oldq
    return min(
        (
            a[i][i] - sum((abs(a[i][j]) for j in range(DIMENSION) if i != j))
            for i in range(DIMENSION)
        )
    )


def lower_certificate(source, targets, weights):
    terms = [tuple((b - a for a, b in zip(p, q))) for p, q in zip(source, targets)]
    error = math.fsum((w * dot(e, e) for w, e in zip(weights, terms)))
    gradients = [cross(p, e) for p, e in zip(source, terms)]
    g = [
        math.fsum((w * value[i] for w, value in zip(weights, gradients)))
        for i in range(DIMENSION)
    ]
    h = [[0.0] * DIMENSION for _ in range(DIMENSION)]
    for i in range(DIMENSION):
        h[i][i] = math.fsum(
            (
                w * sum((p[k] * q[k] for k in range(DIMENSION) if k != i))
                for p, q, w in zip(source, targets, weights)
            )
        )
        for j in range(i):
            h[i][j] = h[j][i] = -HALF * math.fsum(
                (
                    w * (p[i] * q[j] + p[j] * q[i])
                    for p, q, w in zip(source, targets, weights)
                )
            )
    eigen = smallest_eigen_lower(h) - EIGEN_ROUNDOFF_FACTOR * MACHINE_EPS * max(
        (sum(map(abs, row)) for row in h)
    )
    if eigen <= 0:
        return -math.inf
    return error - dot(g, g) / eigen


def parameter_rotation(p, u, v, theta):
    sine, cosine = (math.sin(theta), math.cos(theta))
    x = cosine * p[0] - sine * p[1]
    y = sine * p[0] + cosine * p[1]
    z = p[2]
    c = 1 / math.sqrt(1 + u * u + v * v)
    value = u * x + v * y
    h = c * z - c * c * value / (1 + c)
    return (x + u * h, y + v * h, c * (z - value))


def feasible(candidate):
    if candidate["canonical_error"] <= NUMERIC_EPS:
        return True
    source, targets = (candidate["source"], candidate["targets"])
    scale = candidate["sine"]
    if max(residuals(source, targets)) <= EPS2:
        return True
    current = quick_witness(candidate)
    if current is not None and max(residuals(current, targets)) <= EPS2:
        return True
    distances = residuals(current if current is not None else source, targets)
    critical = max(range(len(source)), key=distances.__getitem__)
    if pair_angle_excluded(candidate, critical):
        return False
    current, pose = fit(source, targets, scale)
    for power in WEIGHT_POWERS:
        distances = residuals(current, targets)
        if max(distances) <= EPS2:
            return True
        weights = (
            [1.0] * len(source)
            if power == 0
            else [max(MIN_WEIGHT, (d / max(distances)) ** power) for d in distances]
        )
        lower = lower_certificate(current, targets, weights)
        if lower > (EPS2 + CERTIFICATE_ROUNDOFF) * math.fsum(weights):
            return False
        current, pose = fit(source, targets, scale, weights, WEIGHTED_ITERATIONS, pose)
    radii = (candidate["tilt_bound"], candidate["tilt_bound"], candidate["twist_bound"])
    norms = [norm(p) for p in source]
    rho = [math.hypot(p[0], p[1]) for p in source]
    heap = []
    serial = 0

    def add(center, radii):
        nonlocal serial
        planar = 2 * math.hypot(radii[0], radii[1])
        lower = 0.0
        worst = 0.0
        for p, q, r, radial in zip(source, targets, norms, rho):
            moved = parameter_rotation(p, *center)
            d = math.sqrt(sum(((a - b) ** 2 for a, b in zip(moved, q))))
            bound = r * planar + radial * radii[2]
            if d > EPS + bound + SEARCH_ROUNDOFF:
                return False
            worst = max(worst, d)
            lower = max(lower, d - bound)
        if worst <= NUMERIC_EPS:
            return True
        serial += 1
        heapq.heappush(heap, (lower, serial, center, radii))
        return False

    if add((0.0, 0.0, 0.0), radii):
        return True
    while heap:
        _, _, center, radii = heapq.heappop(heap)
        axis = max(range(DIMENSION), key=lambda i: radii[i] * (scale if i == 2 else 1))
        following = list(radii)
        following[axis] /= 2
        for sign in (-1, 1):
            child = list(center)
            child[axis] += sign * following[axis]
            if add(tuple(child), tuple(following)):
                return True
    return False


def rotation_count(points):
    accepted = set()
    for candidate in candidates(points):
        answer = feasible(candidate)
        if answer:
            accepted.add(candidate["mapping"])
    return len(accepted)


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    count = int(next(tokens))
    points = [
        (float(next(tokens)), float(next(tokens)), float(next(tokens)))
        for _ in range(count)
    ]
    print(rotation_count(points))


if __name__ == "__main__":
    main()
