use std::io::{self, Read};

// the shot and the number of corners come before the corners
const HEADER: usize = 3;

fn segment_distance(p: (f64, f64), a: (f64, f64), b: (f64, f64)) -> f64 {
    let (dx, dy) = (b.0 - a.0, b.1 - a.1);
    let t = (p.0 - a.0) * dx + (p.1 - a.1) * dy;
    let length2 = dx * dx + dy * dy;
    if t <= 0.0 {
        (p.0 - a.0).hypot(p.1 - a.1)
    } else if t >= length2 {
        (p.0 - b.0).hypot(p.1 - b.1)
    } else {
        ((p.0 - a.0) * dy - (p.1 - a.1) * dx).abs() / length2.sqrt()
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (px, py, n) = (v[0], v[1], v[2] as usize);
    let pts: Vec<(i64, i64)> = v[HEADER..]
        .chunks(2)
        .take(n)
        .map(|c| (c[0], c[1]))
        .collect();
    let mut inside = true;
    let mut best = f64::INFINITY;
    for i in 0..n {
        let (a, b) = (pts[i], pts[(i + 1) % n]);
        // inside a counterclockwise polygon the point is left of every edge
        if (b.0 - a.0) * (py - a.1) - (b.1 - a.1) * (px - a.0) < 0 {
            inside = false;
        }
        let f = |q: (i64, i64)| (q.0 as f64, q.1 as f64);
        best = best.min(segment_distance(f((px, py)), f(a), f(b)));
    }
    println!("{:.3}", if inside { 0.0 } else { 2.0 * best });
}
