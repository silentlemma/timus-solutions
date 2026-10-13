use std::io::{self, Read};

const SHORTEST: f64 = 1.0; // the allowed rope lengths
const LONGEST: f64 = 50.0;
const EPS: f64 = 1e-9;

/// The largest a^2 + b^2 with 1 <= a <= top_a, 1 <= b <= top_b, a + b <= d, or -1.
fn best_pair(top_a: f64, top_b: f64, d: f64) -> f64 {
    if top_a < SHORTEST - EPS || top_b < SHORTEST - EPS || d < 2.0 * SHORTEST - EPS {
        return -1.0;
    }
    // a convex function is largest at a corner of the region
    let corners = [
        (top_a, top_b),
        (top_a, SHORTEST),
        (SHORTEST, top_b),
        (top_a, d - top_a),
        (d - top_b, top_b),
        (d - SHORTEST, SHORTEST),
        (SHORTEST, d - SHORTEST),
    ];
    corners
        .iter()
        .filter(|&&(a, b)| {
            a >= SHORTEST - EPS
                && a <= top_a + EPS
                && b >= SHORTEST - EPS
                && b <= top_b + EPS
                && a + b <= d + EPS
        })
        .map(|&(a, b)| a * a + b * b)
        .fold(-1.0, f64::max)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let pts: Vec<(f64, f64)> = (0..n)
        .map(|_| {
            let x: f64 = it.next().unwrap().parse().unwrap();
            let y: f64 = it.next().unwrap().parse().unwrap();
            (x, y)
        })
        .collect();
    let dist = |i: usize, j: usize| (pts[i].0 - pts[j].0).hypot(pts[i].1 - pts[j].1);
    // the longest rope at each tree: up to the nearest other tree and 50 meters
    let top: Vec<f64> = (0..n)
        .map(|i| {
            (0..n)
                .filter(|&j| j != i)
                .map(|j| dist(i, j))
                .fold(LONGEST, f64::min)
        })
        .collect();
    let mut best = 0.0f64;
    for i in 0..n {
        for j in i + 1..n {
            best = best.max(best_pair(top[i], top[j], dist(i, j)));
        }
    }
    println!("{:.4}", std::f64::consts::PI * best);
}
