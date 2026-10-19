use std::io::{self, Read};
use std::str::SplitWhitespace;

const GRAVITY: i64 = 10;
const HALF_GRAVITY: i64 = GRAVITY / 2;
const QUADRATIC_FACTOR: i64 = 4;
const INPUT_FIELDS: usize = 8;
const MARGIN: f64 = 1e-6;

#[derive(Clone, Copy)]
struct Polynomial {
    a: i64,
    b: i64,
    c: i64,
}

fn roots(p: Polynomial) -> Option<(f64, f64)> {
    let delta = p.b * p.b + QUADRATIC_FACTOR * p.a * p.c;
    if delta < 0 {
        return None;
    }
    if delta == 0 {
        let value = p.b as f64 / (2 * p.a) as f64;
        return Some((value, value));
    }
    let q = (p.b as f64 + (delta as f64).sqrt().copysign(p.b as f64)) / 2.0;
    let (x, y) = (q / p.a as f64, -(p.c as f64) / q);
    Some((x.min(y), x.max(y)))
}

fn feasible(data: &[i64; INPUT_FIELDS]) -> Vec<(f64, f64)> {
    let [distance, height, thickness, diameter, vx, vy, ux, uy] = *data;
    let (mut lo, mut hi) = (
        0.0f64,
        (2.0 * vy as f64 / GRAVITY as f64).min(distance as f64 / vx as f64),
    );
    let face = |x, level| Polynomial {
        a: HALF_GRAVITY * (ux * ux + vx * vx),
        b: vy * ux * ux - uy * vx * ux + GRAVITY * x * vx,
        c: uy * x * ux - HALF_GRAVITY * x * x - level * ux * ux,
    };
    for x in [distance, distance + thickness] {
        let Some((a, b)) = roots(face(x, height)) else {
            return Vec::new();
        };
        lo = lo.max(a);
        hi = hi.min(b);
        if lo >= hi {
            return Vec::new();
        }
    }
    let ceiling = height + diameter;
    let before = (GRAVITY * distance - ux * uy) as f64 / (GRAVITY * vx) as f64;
    let after = (GRAVITY * (distance + thickness) - ux * uy) as f64 / (GRAVITY * vx) as f64;
    let pieces = [
        (lo, hi.min(before), face(distance, ceiling)),
        (
            lo.max(before),
            hi.min(after),
            Polynomial {
                a: GRAVITY * GRAVITY,
                b: 2 * GRAVITY * vy,
                c: uy * uy - 2 * GRAVITY * ceiling,
            },
        ),
        (lo.max(after), hi, face(distance + thickness, ceiling)),
    ];
    let (mut found, mut bad_lo, mut bad_hi) = (false, hi, lo);
    for (left, right, p) in pieces {
        if left > right {
            continue;
        }
        if let Some((a, b)) = roots(p) {
            let (a, b) = (left.max(a), right.min(b));
            if a <= b {
                found = true;
                bad_lo = bad_lo.min(a);
                bad_hi = bad_hi.max(b);
            }
        }
    }
    if !found {
        return vec![(lo, hi)];
    }
    let mut result = Vec::new();
    if lo < bad_lo {
        result.push((lo, bad_lo));
    }
    if bad_hi < hi {
        result.push((bad_hi, hi));
    }
    result
}

fn solve(data: &[i64; INPUT_FIELDS]) -> f64 {
    let (mut best_width, mut answer) = (2.0 * MARGIN, -1.0);
    for (lo, hi) in feasible(data) {
        if hi - lo > best_width {
            best_width = hi - lo;
            answer = (lo + hi) / 2.0;
        }
    }
    answer
}

fn run(tokens: &mut SplitWhitespace<'_>) -> String {
    let mut data = [0i64; INPUT_FIELDS];
    for value in &mut data {
        *value = tokens.next().unwrap().parse().unwrap();
    }
    format!("{}\n", solve(&data))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", run(&mut input.split_whitespace()));
}
