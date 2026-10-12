use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const MOST: f64 = 4.0; // the longest squared chord, between opposite points

// the point on the unit sphere
fn unit(latitude: f64, longitude: f64) -> (f64, f64, f64) {
    let (a, b) = (latitude.to_radians(), longitude.to_radians());
    (a.cos() * b.cos(), a.cos() * b.sin(), a.sin())
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<f64>().unwrap());
    let mut next = || it.next().unwrap();
    let (n, m, r) = (next() as usize, next() as usize, next());
    let pads: Vec<(f64, f64, f64)> = (0..m)
        .map(|_| {
            let w = next();
            unit(w, next())
        })
        .collect();
    let mut out = String::new();
    for _ in 0..n {
        let w = next();
        let q = unit(w, next());
        // the nearest pad has the shortest chord through the planet
        let best = pads
            .iter()
            .map(|p| {
                let (dx, dy, dz) = (q.0 - p.0, q.1 - p.1, q.2 - p.2);
                dx * dx + dy * dy + dz * dz
            })
            .fold(MOST, f64::min);
        let half = (best.sqrt() / 2.0).min(1.0);
        writeln!(out, "{:.2}", 2.0 * r * half.asin()).unwrap();
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
