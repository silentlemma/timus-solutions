use std::f64::consts::PI;
use std::io::{self, Read};

const DIM: usize = 3;
const STEPS: usize = 60; // halvings in each bisection
const SPHERE: usize = 1500; // directions tried for the narrowest width

const GRID: usize = 80; // grid side of the fallback search
const STARTS: usize = 4; // best grid cells it zooms in around
const ZOOMS: usize = 14; // rounds of zooming, each one ZOOM times finer
const ZOOM: i32 = 5;

const TINY: f64 = 1e-13; // where the local search stops
const NEAR: f64 = 1e-10; // equal widths, relative to the diameter
const ROUNDS: usize = 400; // passes of a local search, which may creep on forever

const HELPER: f64 = 0.9; // a helper axis closer than this to n gives a poor cross product
const GOLDEN: f64 = 2.399963229728653; // the golden angle, spreading directions over the sphere
const FIRST_TURN: f64 = 0.7853981633974483; // pi / 4, the first turn of the polish

type Vec3 = [f64; DIM];
type Frame = [Vec3; DIM];
type Int3 = [i64; DIM];

fn dot(a: Vec3, b: Vec3) -> f64 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

fn cross(a: Vec3, b: Vec3) -> Vec3 {
    [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
}

/// s * a + t * b
fn comb(a: Vec3, s: f64, b: Vec3, t: f64) -> Vec3 {
    [s * a[0] + t * b[0], s * a[1] + t * b[1], s * a[2] + t * b[2]]
}

fn unit(a: Vec3) -> Vec3 {
    let n = dot(a, a).sqrt();
    [a[0] / n, a[1] / n, a[2] / n]
}

/// v turned by angle around the unit vector axis (Rodrigues).
fn turn(v: Vec3, axis: Vec3, angle: f64) -> Vec3 {
    let (c, s) = (angle.cos(), angle.sin());
    let k = dot(axis, v) * (1.0 - c);
    let w = cross(axis, v);
    [
        v[0] * c + w[0] * s + axis[0] * k,
        v[1] * c + w[1] * s + axis[1] * k,
        v[2] * c + w[2] * s + axis[2] * k,
    ]
}

/// Two unit vectors completing n to a right-handed frame.
fn across(n: Vec3) -> (Vec3, Vec3) {
    let helper = if n[0].abs() > HELPER { [0.0, 1.0, 0.0] } else { [1.0, 0.0, 0.0] };
    let a = unit(cross(n, helper));
    (a, cross(n, a))
}

struct Swarm {
    pts: Vec<Vec3>,
}

impl Swarm {
    fn width(&self, u: Vec3) -> f64 {
        let (mut lo, mut hi) = (f64::INFINITY, f64::NEG_INFINITY);
        for &p in &self.pts {
            let s = dot(p, u);
            lo = lo.min(s);
            hi = hi.max(s);
        }
        hi - lo
    }

    fn spread(&self, f: &Frame) -> f64 {
        let w = [self.width(f[0]), self.width(f[1]), self.width(f[2])];
        w[0].max(w[1]).max(w[2]) - w[0].min(w[1]).min(w[2])
    }

    fn cost(&self, f: &Frame) -> f64 {
        let w = [self.width(f[0]), self.width(f[1]), self.width(f[2])];
        (w[0] - w[1]).powi(2) + (w[1] - w[2]).powi(2) + (w[2] - w[0]).powi(2)
    }
}

fn show(f: &Frame) {
    for u in f {
        println!("{:.15} {:.15} {:.15}", u[0], u[1], u[2]);
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let count = v[0] as usize;
    let ints: Vec<Int3> = v[1..=DIM * count].chunks(DIM).map(|c| [c[0], c[1], c[2]]).collect();
    let sw = Swarm { pts: ints.iter().map(|p| [p[0] as f64, p[1] as f64, p[2] as f64]).collect() };
    // the shape of the swarm, decided exactly on the integers
    let diffs: Vec<Int3> =
        ints.iter().map(|p| [p[0] - ints[0][0], p[1] - ints[0][1], p[2] - ints[0][2]]).collect();
    let icross = |a: Int3, b: Int3| {
        [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
    };
    let first = *diffs.iter().find(|d| **d != [0, 0, 0]).unwrap();
    let normal = diffs.iter().map(|&d| icross(first, d)).find(|c| *c != [0, 0, 0]);
    let normal = match normal {
        Some(n) => n,
        None => {
            // all on a line of direction d: an axis at angle acos(1/sqrt 3) to
            // the line each, so the three widths are the length over sqrt 3
            let d = unit([first[0] as f64, first[1] as f64, first[2] as f64]);
            let (u, w) = across(d);
            let r3 = 1.0 / (DIM as f64).sqrt();
            let (r2, r6) = (1.0 / 2f64.sqrt(), 1.0 / (2.0 * DIM as f64).sqrt());
            show(&[
                comb(comb(d, r3, u, r2), 1.0, w, r6),
                comb(comb(d, r3, u, -r2), 1.0, w, r6),
                comb(d, r3, w, -2.0 * r6),
            ]);
            return;
        }
    };
    let flat = diffs.iter().all(|d| normal[0] * d[0] + normal[1] * d[1] + normal[2] * d[2] == 0);
    // widest direction: the diameter, where no other width can be larger
    let (mut best_length, mut n_max) = (-1i64, [0.0; DIM]);
    for p in &ints {
        for q in &ints {
            let d = [p[0] - q[0], p[1] - q[1], p[2] - q[2]];
            let l = d[0] * d[0] + d[1] * d[1] + d[2] * d[2];
            if l > best_length {
                best_length = l;
                n_max = [d[0] as f64, d[1] as f64, d[2] as f64];
            }
        }
    }
    let n_max = unit(n_max);
    // narrowest direction: the normal of a flat swarm, else a search
    let n_min = if flat {
        unit([normal[0] as f64, normal[1] as f64, normal[2] as f64])
    } else {
        let (mut w_min, mut n_min) = (f64::INFINITY, [0.0; DIM]);
        for i in 0..SPHERE {
            let z = 1.0 - (2 * i + 1) as f64 / (2 * SPHERE) as f64;
            let r = (1.0 - z * z).sqrt();
            let u = [r * (GOLDEN * i as f64).cos(), r * (GOLDEN * i as f64).sin(), z];
            let w = sw.width(u);
            if w < w_min {
                w_min = w;
                n_min = u;
            }
        }
        let mut step = 2.0 * PI / (SPHERE as f64).sqrt();
        for _ in 0..ROUNDS {
            if step <= TINY {
                break;
            }
            let (a, b) = across(n_min);
            let mut moved = false;
            for axis in [a, b, unit(comb(a, 1.0, b, 1.0)), unit(comb(a, 1.0, b, -1.0))] {
                for sign in [1.0, -1.0] {
                    let cand = unit(turn(n_min, axis, sign * step));
                    let w = sw.width(cand);
                    if w < w_min {
                        w_min = w;
                        n_min = cand;
                        moved = true;
                    }
                }
            }
            if !moved {
                step /= 2.0;
            }
        }
        n_min
    };
    // frames along the great circle from n_min to n_max: the third axis is
    // the turned n, the first two the turned a0, b0 rotated by phi
    let mut hinge = cross(n_min, n_max);
    if dot(hinge, hinge) < TINY {
        hinge = across(n_min).0;
    }
    let hinge = unit(hinge);
    let angle = dot(n_min, n_max).clamp(-1.0, 1.0).acos();
    let (a0, b0) = across(n_min);
    let frame = |t: f64, phi: f64| -> Frame {
        let n = turn(n_min, hinge, angle * t);
        let (a, b) = (turn(a0, hinge, angle * t), turn(b0, hinge, angle * t));
        let (c, s) = (phi.cos(), phi.sin());
        [comb(a, c, b, s), comb(a, -s, b, c), n]
    };
    // phi in [0, pi/2] with equal first two widths: the difference changes
    // sign over a quarter turn, as the axes swap places
    let balance = |t: f64| -> f64 {
        let gap_at = |phi: f64| {
            let f = frame(t, phi);
            sw.width(f[0]) - sw.width(f[1])
        };
        let (mut lo, mut hi) = (0.0, PI / 2.0);
        if gap_at(lo) > 0.0 {
            std::mem::swap(&mut lo, &mut hi);
        }
        for _ in 0..STEPS {
            let mid = (lo + hi) / 2.0;
            if gap_at(mid) > 0.0 {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        (lo + hi) / 2.0
    };
    // at n_min the third width is the smallest, at n_max the largest
    let (mut lo, mut hi) = (0.0, 1.0);
    for _ in 0..STEPS {
        let mid = (lo + hi) / 2.0;
        let f = frame(mid, balance(mid));
        if sw.width(f[2]) - sw.width(f[0]) < 0.0 {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    let t = (lo + hi) / 2.0;
    let mut result = frame(t, balance(t));
    let scale = sw.width(n_max).max(1.0);
    if sw.spread(&result) > NEAR * scale {
        // the chosen balance jumped. A solution still lies in the (t, phi)
        // square, as the third width is the smallest along t = 0 and the
        // largest along t = 1: scan it, then zoom in around the best cells
        let quarter = PI / 2.0;
        let last = (GRID - 1) as f64;
        let mut cells: Vec<(f64, f64, f64)> = Vec::new();
        for i in 0..GRID {
            for j in 0..GRID {
                let (ti, pj) = (i as f64 / last, quarter * j as f64 / last);
                cells.push((sw.cost(&frame(ti, pj)), ti, pj));
            }
        }
        cells.sort_by(|x, y| x.0.partial_cmp(&y.0).unwrap());
        for &start in cells.iter().take(STARTS) {
            let (mut dt, mut dp) = (1.0 / last, quarter / last);
            let mut here = start;
            for _ in 0..ZOOMS {
                let (tc, pc) = (here.1, here.2);
                for a in -ZOOM..=ZOOM {
                    let ta = (tc + a as f64 * dt / ZOOM as f64).clamp(0.0, 1.0);
                    for b in -ZOOM..=ZOOM {
                        let pb = pc + b as f64 * dp / ZOOM as f64;
                        let c = sw.cost(&frame(ta, pb));
                        if c < here.0 {
                            here = (c, ta, pb);
                        }
                    }
                }
                dt /= ZOOM as f64;
                dp /= ZOOM as f64;
            }
            result = frame(here.1, here.2);
            if sw.spread(&result) <= NEAR * scale {
                break;
            }
        }
    }
    // polish by small turns of the frame about its own axes
    let mut best = sw.cost(&result);
    let mut step = if sw.spread(&result) > NEAR * scale { FIRST_TURN } else { TINY * 2.0 };
    for _ in 0..ROUNDS {
        if step <= TINY {
            break;
        }
        let mut moved = false;
        for k in 0..DIM {
            for sign in [1.0, -1.0] {
                let mut cand = result;
                for i in 0..DIM {
                    if i != k {
                        cand[i] = turn(result[i], result[k], sign * step);
                    }
                }
                let c = sw.cost(&cand);
                if c < best {
                    best = c;
                    result = cand;
                    moved = true;
                }
            }
        }
        if !moved {
            step /= 2.0;
        }
    }
    show(&result);
}
