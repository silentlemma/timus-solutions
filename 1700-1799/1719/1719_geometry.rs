use std::io::{self, Read};

const BOSSES: usize = 4;
// the three ways to split the four bosses into two shots
const SPLITS: [[[usize; 2]; 2]; 3] = [[[0, 1], [2, 3]], [[0, 2], [1, 3]], [[0, 3], [1, 2]]];

// walk from the origin to a point P on the line a1 b1, shoot, then walk
// straight to the line a2 b2; along the first line P = a1 + t u and the
// length is sqrt((t - t0)^2 + h^2) + |k t + m|, convex in t
fn walk(p: &[(f64, f64)], a1: usize, b1: usize, a2: usize, b2: usize) -> f64 {
    let (lx, ly) = (p[b1].0 - p[a1].0, p[b1].1 - p[a1].1);
    let length = lx.hypot(ly);
    let (ux, uy) = (lx / length, ly / length);
    let t0 = -(p[a1].0 * ux + p[a1].1 * uy);
    let h = (p[a1].0 * uy - p[a1].1 * ux).abs();
    let (mx, my) = (p[b2].0 - p[a2].0, p[b2].1 - p[a2].1);
    let norm = mx.hypot(my);
    let (nx, ny) = (-my / norm, mx / norm);
    let k = nx * ux + ny * uy;
    let m = nx * (p[a1].0 - p[a2].0) + ny * (p[a1].1 - p[a2].1);
    // the minimum is at the foot of the origin, where the lines cross, or
    // where the slope of the first term cancels the slope k of the second
    let mut candidates = vec![t0];
    if k != 0.0 {
        candidates.push(-m / k);
    }
    if k.abs() < 1.0 {
        let shift = k * h / (1.0 - k * k).sqrt();
        candidates.push(t0 + shift);
        candidates.push(t0 - shift);
    }
    candidates
        .iter()
        .map(|&t| (t - t0).hypot(h) + (k * t + m).abs())
        .fold(f64::INFINITY, f64::min)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<f64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let p: Vec<(f64, f64)> = (0..BOSSES).map(|i| (v[2 * i], v[2 * i + 1])).collect();
    let mut best = f64::INFINITY;
    for &[first, second] in &SPLITS {
        best = best.min(walk(&p, first[0], first[1], second[0], second[1]));
        best = best.min(walk(&p, second[0], second[1], first[0], first[1]));
    }
    println!("{:.10}", best);
}
