use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap, HashSet};
use std::io::{self, Read};

const DIMENSION: usize = 3;
const QUATERNION_SIZE: usize = 4;
const FIT_ITERATIONS: usize = 12;
const WEIGHTED_ITERATIONS: usize = 6;
const JACOBI_ITERATIONS: usize = 24;
const EIGEN_ROUNDOFF_FACTOR: f64 = 256.0;
const EPS: f64 = 1e-6;
const CELL: f64 = 10.0 * EPS;
const GATE: f64 = 5.0 * EPS;
const ROUNDOFF_GUARD: f64 = 2e-15;
const NUMERIC_EPS: f64 = EPS + ROUNDOFF_GUARD;
const EPS2: f64 = NUMERIC_EPS * NUMERIC_EPS;
const ANGLE_ROUNDOFF: f64 = 1e-12;
const SEARCH_ROUNDOFF: f64 = 1e-16;
const CERTIFICATE_ROUNDOFF: f64 = 1e-20;
const SINGULAR_LIMIT: f64 = 1e-30;
const STEP_LIMIT: f64 = 1e-15;
const MIN_WEIGHT: f64 = 1e-10;
const WEIGHT_POWERS: [i32; WEIGHTED_ITERATIONS] = [0, 1, 2, 4, 8, 16];

type Point = [f64; DIMENSION];
type Matrix = [Point; DIMENSION];
type Pose = [f64; QUATERNION_SIZE];
type Key = [i32; DIMENSION];

fn dot(a: Point, b: Point) -> f64 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}
fn cross(a: Point, b: Point) -> Point {
    [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]
}
fn norm(a: Point) -> f64 {
    dot(a, a).sqrt()
}
fn unit(mut a: Point) -> Point {
    let length = norm(a);
    for x in &mut a {
        *x /= length;
    }
    a
}
fn subtract(a: Point, b: Point) -> Point {
    [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
}
fn distance2(a: Point, b: Point) -> f64 {
    let d = subtract(a, b);
    dot(d, d)
}
fn frame(a: Point, b: Point) -> Matrix {
    let z = unit(a);
    let y = unit(cross(z, unit(b)));
    [cross(y, z), y, z]
}
fn project(a: Point, basis: Matrix) -> Point {
    [dot(a, basis[0]), dot(a, basis[1]), dot(a, basis[2])]
}
fn unproject(a: Point, basis: Matrix) -> Point {
    let mut result = [0.0; DIMENSION];
    for i in 0..DIMENSION {
        for j in 0..DIMENSION {
            result[i] += a[j] * basis[j][i];
        }
    }
    result
}
fn cell(p: Point) -> Key {
    [
        (p[0] / CELL).floor() as i32,
        (p[1] / CELL).floor() as i32,
        (p[2] / CELL).floor() as i32,
    ]
}
fn solve3(mut a: Matrix, mut rhs: Point) -> Option<Point> {
    for column in 0..DIMENSION {
        let mut pivot = column;
        for i in column + 1..DIMENSION {
            if a[i][column].abs() > a[pivot][column].abs() {
                pivot = i;
            }
        }
        if a[pivot][column].abs() < SINGULAR_LIMIT {
            return None;
        }
        a.swap(pivot, column);
        rhs.swap(pivot, column);
        let divisor = a[column][column];
        for j in 0..DIMENSION {
            a[column][j] /= divisor;
        }
        rhs[column] /= divisor;
        for i in 0..DIMENSION {
            if i == column {
                continue;
            }
            let factor = a[i][column];
            for j in 0..DIMENSION {
                a[i][j] -= factor * a[column][j];
            }
            rhs[i] -= factor * rhs[column];
        }
    }
    Some(rhs)
}
fn normal_matrix(points: &[Point], weights: &[f64], scale: f64) -> Matrix {
    let (mut xx, mut yy, mut zz, mut xy, mut xz, mut yz) = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
    for (p, &w) in points.iter().zip(weights) {
        xx += w * p[0] * p[0];
        yy += w * p[1] * p[1];
        zz += w * p[2] * p[2];
        xy += w * p[0] * p[1];
        xz += w * p[0] * p[2];
        yz += w * p[1] * p[2];
    }
    [
        [yy + zz, -xy, -xz / scale],
        [-xy, xx + zz, -yz / scale],
        [-xz / scale, -yz / scale, (xx + yy) / (scale * scale)],
    ]
}
fn gradient(points: &[Point], targets: &[Point], weights: &[f64]) -> Point {
    let mut result = [0.0; DIMENSION];
    for ((&p, &q), &w) in points.iter().zip(targets).zip(weights) {
        let g = cross(p, subtract(q, p));
        for j in 0..DIMENSION {
            result[j] += w * g[j];
        }
    }
    result
}
#[derive(Clone, Copy, Default)]
struct Sum {
    total: f64,
    correction: f64,
}
impl Sum {
    fn add(&mut self, x: f64) {
        let next = self.total + x;
        self.correction += if self.total.abs() >= x.abs() {
            (self.total - next) + x
        } else {
            (x - next) + self.total
        };
        self.total = next;
    }
    fn value(self) -> f64 {
        self.total + self.correction
    }
}
fn quaternion_step(omega: Point, pose: Pose) -> Pose {
    let angle = norm(omega);
    if angle == 0.0 {
        return pose;
    }
    let factor = (angle / 2.0).sin() / angle;
    let (a, b, c, d) = (
        (angle / 2.0).cos(),
        omega[0] * factor,
        omega[1] * factor,
        omega[2] * factor,
    );
    let (w, x, y, z) = (pose[0], pose[1], pose[2], pose[DIMENSION]);
    let mut result = [
        a * w - b * x - c * y - d * z,
        a * x + b * w + c * z - d * y,
        a * y - b * z + c * w + d * x,
        a * z + b * y - c * x + d * w,
    ];
    let mut squared = Sum::default();
    for &value in &result {
        squared.add(value * value);
    }
    let length = squared.value().sqrt();
    for value in &mut result {
        *value /= length;
    }
    result
}
fn quaternion_apply(points: &[Point], pose: Pose) -> Vec<Point> {
    let (w, x, y, z) = (pose[0], pose[1], pose[2], pose[DIMENSION]);
    let rows = [
        [
            1.0 - 2.0 * (y * y + z * z),
            2.0 * (x * y - w * z),
            2.0 * (x * z + w * y),
        ],
        [
            2.0 * (x * y + w * z),
            1.0 - 2.0 * (x * x + z * z),
            2.0 * (y * z - w * x),
        ],
        [
            2.0 * (x * z - w * y),
            2.0 * (y * z + w * x),
            1.0 - 2.0 * (x * x + y * y),
        ],
    ];
    points.iter().map(|&p| project(p, rows)).collect()
}
fn residuals(points: &[Point], targets: &[Point]) -> Vec<f64> {
    points
        .iter()
        .zip(targets)
        .map(|(&p, &q)| distance2(p, q))
        .collect()
}
fn maximum(values: &[f64]) -> f64 {
    values.iter().copied().fold(0.0, f64::max)
}
fn eigen_lower(mut a: Matrix) -> f64 {
    for _ in 0..JACOBI_ITERATIONS {
        let (mut p, mut q) = (0, 1);
        for i in 0..DIMENSION {
            for j in i + 1..DIMENSION {
                if a[i][j].abs() > a[p][q].abs() {
                    p = i;
                    q = j;
                }
            }
        }
        let value = a[p][q];
        if value.abs() < SINGULAR_LIMIT {
            break;
        }
        let tau = (a[q][q] - a[p][p]) / (2.0 * value);
        let t = 1.0_f64.copysign(tau) / (tau.abs() + 1.0_f64.hypot(tau));
        let c = 1.0 / (1.0 + t * t).sqrt();
        let s = t * c;
        a[p][p] -= t * value;
        a[q][q] += t * value;
        a[p][q] = 0.0;
        a[q][p] = 0.0;
        for k in 0..DIMENSION {
            if k == p || k == q {
                continue;
            }
            let (oldp, oldq) = (a[k][p], a[k][q]);
            a[k][p] = c * oldp - s * oldq;
            a[p][k] = a[k][p];
            a[k][q] = s * oldp + c * oldq;
            a[q][k] = a[k][q];
        }
    }
    let mut lower = f64::INFINITY;
    for i in 0..DIMENSION {
        let mut bound = a[i][i];
        for j in 0..DIMENSION {
            if i != j {
                bound -= a[i][j].abs();
            }
        }
        lower = lower.min(bound);
    }
    lower
}
fn lower_certificate(points: &[Point], targets: &[Point], weights: &[f64]) -> f64 {
    let mut error = Sum::default();
    let mut gradients = [Sum::default(); DIMENSION];
    let mut entries = [[Sum::default(); DIMENSION]; DIMENSION];
    for ((&p, &q), &w) in points.iter().zip(targets).zip(weights) {
        let e = subtract(q, p);
        let g = cross(p, e);
        error.add(w * dot(e, e));
        for i in 0..DIMENSION {
            gradients[i].add(w * g[i]);
            let mut diagonal = 0.0;
            for j in 0..DIMENSION {
                if i != j {
                    diagonal += p[j] * q[j];
                }
            }
            entries[i][i].add(w * diagonal);
            for j in 0..i {
                entries[i][j].add(-w / 2.0 * (p[i] * q[j] + p[j] * q[i]));
            }
        }
    }
    let mut h = [[0.0; DIMENSION]; DIMENSION];
    let mut g = [0.0; DIMENSION];
    for i in 0..DIMENSION {
        g[i] = gradients[i].value();
        for j in 0..=i {
            h[i][j] = entries[i][j].value();
            h[j][i] = h[i][j];
        }
    }
    let row_norm = h
        .iter()
        .map(|r| r[0].abs() + r[1].abs() + r[2].abs())
        .fold(0.0, f64::max);
    let eigen = eigen_lower(h) - EIGEN_ROUNDOFF_FACTOR * f64::EPSILON * row_norm;
    if eigen <= 0.0 {
        return f64::NEG_INFINITY;
    }
    error.value() - dot(g, g) / eigen
}
fn parameter_rotation(p: Point, center: Point) -> Point {
    let (u, v, theta) = (center[0], center[1], center[2]);
    let (sine, cosine) = (theta.sin(), theta.cos());
    let (x, y, z) = (
        cosine * p[0] - sine * p[1],
        sine * p[0] + cosine * p[1],
        p[2],
    );
    let c = 1.0 / (1.0 + u * u + v * v).sqrt();
    let value = u * x + v * y;
    let h = c * z - c * c * value / (1.0 + c);
    [x + u * h, y + v * h, c * (z - value)]
}
#[derive(Clone)]
struct Cell {
    lower: f64,
    serial: usize,
    center: Point,
    radii: Point,
}
impl PartialEq for Cell {
    fn eq(&self, other: &Self) -> bool {
        self.lower == other.lower && self.serial == other.serial
    }
}
impl Eq for Cell {}
impl PartialOrd for Cell {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}
impl Ord for Cell {
    fn cmp(&self, other: &Self) -> Ordering {
        other
            .lower
            .partial_cmp(&self.lower)
            .unwrap()
            .then_with(|| other.serial.cmp(&self.serial))
    }
}
struct Solver {
    points: Vec<Point>,
    normalized: Vec<Point>,
    source: Vec<Point>,
    targets: Vec<Point>,
    angles: Vec<Vec<f64>>,
    mapping: Vec<usize>,
    normal: Matrix,
    scale: f64,
    angular: f64,
    chord: f64,
}
impl Solver {
    fn new(points: Vec<Point>) -> Self {
        let n = points.len();
        Self {
            points,
            normalized: Vec::new(),
            source: Vec::new(),
            targets: Vec::new(),
            angles: vec![Vec::new(); n],
            mapping: Vec::new(),
            normal: [[0.0; DIMENSION]; DIMENSION],
            scale: 0.0,
            angular: 0.0,
            chord: 0.0,
        }
    }
    fn fill_angle_row(&mut self, index: usize) {
        if self.angles[index].is_empty() {
            let p = self.normalized[index];
            self.angles[index] = self
                .normalized
                .iter()
                .map(|&q| norm(cross(p, q)).atan2(dot(p, q)))
                .collect();
        }
    }
    fn angle_excluded(&mut self, index: usize) -> bool {
        self.fill_angle_row(index);
        self.fill_angle_row(self.mapping[index]);
        let a = &self.angles[index];
        let b = &self.angles[self.mapping[index]];
        self.mapping
            .iter()
            .enumerate()
            .any(|(i, &j)| (a[i] - b[j]).abs() > 2.0 * self.angular + ANGLE_ROUNDOFF)
    }
    fn fit(&self, weights: &[f64], iterations: usize, mut pose: Pose) -> (Vec<Point>, Pose) {
        let mut current = quaternion_apply(&self.source, pose);
        for _ in 0..iterations {
            let mut g = gradient(&current, &self.targets, weights);
            g[2] /= self.scale;
            let Some(mut omega) = solve3(normal_matrix(&current, weights, self.scale), g) else {
                break;
            };
            omega[2] /= self.scale;
            pose = quaternion_step(omega, pose);
            current = quaternion_apply(&self.source, pose);
            if maximum(&residuals(&current, &self.targets)) <= EPS2 || norm(omega) < STEP_LIMIT {
                break;
            }
        }
        (current, pose)
    }
    fn bounded(&self, twist: f64) -> bool {
        let norms: Vec<f64> = self.source.iter().copied().map(norm).collect();
        let rho: Vec<f64> = self.source.iter().map(|p| p[0].hypot(p[1])).collect();
        let mut heap = BinaryHeap::new();
        let mut serial = 0;
        let add = |center: Point, radii: Point, heap: &mut BinaryHeap<Cell>, serial: &mut usize| {
            let planar = 2.0 * radii[0].hypot(radii[1]);
            let (mut lower, mut worst) = (0.0_f64, 0.0_f64);
            for i in 0..self.source.len() {
                let d =
                    distance2(parameter_rotation(self.source[i], center), self.targets[i]).sqrt();
                let bound = norms[i] * planar + rho[i] * radii[2];
                if d > EPS + bound + SEARCH_ROUNDOFF {
                    return false;
                }
                worst = worst.max(d);
                lower = lower.max(d - bound);
            }
            if worst <= NUMERIC_EPS {
                return true;
            }
            *serial += 1;
            heap.push(Cell {
                lower,
                serial: *serial,
                center,
                radii,
            });
            false
        };
        if add(
            [0.0; DIMENSION],
            [self.angular.tan(), self.angular.tan(), twist],
            &mut heap,
            &mut serial,
        ) {
            return true;
        }
        while let Some(mut b) = heap.pop() {
            let mut axis = 0;
            let mut largest = b.radii[0];
            for i in 1..DIMENSION {
                let value = b.radii[i] * if i == 2 { self.scale } else { 1.0 };
                if value > largest {
                    largest = value;
                    axis = i;
                }
            }
            b.radii[axis] /= 2.0;
            for sign in [-1.0, 1.0] {
                let mut child = b.center;
                child[axis] += sign * b.radii[axis];
                if add(child, b.radii, &mut heap, &mut serial) {
                    return true;
                }
            }
        }
        false
    }
    fn feasible(&mut self, twist: f64) -> bool {
        let mut weights = vec![1.0; self.source.len()];
        let mut g = gradient(&self.source, &self.targets, &weights);
        g[2] /= self.scale;
        let mut quick = self.source.clone();
        if let Some(mut omega) = solve3(self.normal, g) {
            omega[2] /= self.scale;
            quick = quaternion_apply(&self.source, quaternion_step(omega, [1.0, 0.0, 0.0, 0.0]));
            if maximum(&residuals(&quick, &self.targets)) <= EPS2 {
                return true;
            }
        }
        let distances = residuals(&quick, &self.targets);
        let mut critical = 0;
        for i in 1..distances.len() {
            if distances[i] > distances[critical] {
                critical = i;
            }
        }
        if self.angle_excluded(critical) {
            return false;
        }
        let (mut current, mut pose) = self.fit(&weights, FIT_ITERATIONS, [1.0, 0.0, 0.0, 0.0]);
        for power in WEIGHT_POWERS {
            let distances = residuals(&current, &self.targets);
            let largest = maximum(&distances);
            if largest <= EPS2 {
                return true;
            }
            let mut total = Sum::default();
            for i in 0..weights.len() {
                weights[i] = if power == 0 {
                    1.0
                } else {
                    MIN_WEIGHT.max((distances[i] / largest).powi(power))
                };
                total.add(weights[i]);
            }
            if lower_certificate(&current, &self.targets, &weights)
                > (EPS2 + CERTIFICATE_ROUNDOFF) * total.value()
            {
                return false;
            }
            (current, pose) = self.fit(&weights, WEIGHTED_ITERATIONS, pose);
        }
        self.bounded(twist)
    }
    fn count(&mut self) -> usize {
        let n = self.points.len();
        let mut anchor = 1;
        let mut minimum_norm = f64::INFINITY;
        for &p in &self.points {
            self.normalized.push(unit(p));
            minimum_norm = minimum_norm.min(norm(p));
        }
        for i in 1..n {
            let candidate = norm(cross(self.normalized[0], self.normalized[i]));
            if candidate > self.scale {
                self.scale = candidate;
                anchor = i;
            }
        }
        let cosine = dot(self.normalized[0], self.normalized[anchor]);
        let alpha = self.scale.atan2(cosine);
        let basis = frame(self.points[0], self.points[anchor]);
        self.source = self.points.iter().map(|&p| project(p, basis)).collect();
        self.normal = normal_matrix(&self.source, &vec![1.0; n], self.scale);
        self.chord = EPS / minimum_norm;
        self.angular = 2.0 * (self.chord / 2.0).asin();
        let mut lookup: HashMap<Key, Vec<usize>> = HashMap::new();
        for (i, &p) in self.points.iter().enumerate() {
            let k = cell(p);
            for dx in -1..=1 {
                for dy in -1..=1 {
                    for dz in -1..=1 {
                        lookup
                            .entry([k[0] + dx, k[1] + dy, k[2] + dz])
                            .or_default()
                            .push(i);
                    }
                }
            }
        }
        let mut accepted = HashSet::new();
        for p in 0..n {
            for q in 0..n {
                if p == q {
                    continue;
                }
                let sine = norm(cross(self.normalized[p], self.normalized[q]));
                let target_cosine = dot(self.normalized[p], self.normalized[q]);
                let tolerance = 2.0 * self.angular + ANGLE_ROUNDOFF;
                if (sine - self.scale).abs() > tolerance
                    || (target_cosine - cosine).abs() > tolerance
                {
                    continue;
                }
                let beta = sine.atan2(target_cosine);
                if sine == 0.0 || (alpha - beta).abs() > tolerance {
                    continue;
                }
                let target_basis = frame(self.points[p], self.points[q]);
                self.mapping.clear();
                let mut used = vec![false; n];
                let mut worst = 0.0_f64;
                for &coordinate in &self.source {
                    let rotated = unproject(coordinate, target_basis);
                    let mut best = GATE * GATE;
                    let mut closest = None;
                    if let Some(bucket) = lookup.get(&cell(rotated)) {
                        for &j in bucket {
                            let error = distance2(rotated, self.points[j]);
                            if error < best {
                                best = error;
                                closest = Some(j);
                            }
                        }
                    }
                    let Some(j) = closest else {
                        break;
                    };
                    if used[j] {
                        break;
                    }
                    used[j] = true;
                    self.mapping.push(j);
                    worst = worst.max(best);
                }
                if self.mapping.len() != n {
                    continue;
                }
                if worst <= EPS2 {
                    accepted.insert(self.mapping.clone());
                    continue;
                }
                self.targets = self
                    .mapping
                    .iter()
                    .map(|&j| project(self.points[j], target_basis))
                    .collect();
                let twist = 2.0 * (self.chord / (self.scale * sine).sqrt()).min(1.0).asin();
                if self.feasible(twist) {
                    accepted.insert(self.mapping.clone());
                }
            }
        }
        accepted.len()
    }
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let Some(first) = tokens.next() else {
        return;
    };
    let n: usize = first.parse().unwrap();
    let points = (0..n)
        .map(|_| {
            let mut p = [0.0; DIMENSION];
            for value in &mut p {
                *value = tokens.next().unwrap().parse().unwrap();
            }
            p
        })
        .collect();
    println!("{}", Solver::new(points).count());
}
