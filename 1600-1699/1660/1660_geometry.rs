use std::f64::consts::PI;
use std::io::{self, Read};

const SLACK: f64 = 1e-9; // lets a chain that closes exactly keep its last circle

/// The image under inversion in the unit circle around the origin.
fn invert((x, y, r): (f64, f64, f64)) -> (f64, f64, f64) {
    let den = x * x + y * y - r * r;
    (x / den, y / den, r / den.abs())
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<f64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (big, small, d) = (v[0], v[1], v[2]);
    // the limit point inside the small circle (the common centre if d = 0):
    // inverting there makes both circles concentric
    let b = big * big + d * d - small * small;
    let twice = 2.0 * d * big;
    let p = twice * big / (b + (b * b - twice * twice).max(0.0).sqrt());
    let outer = invert((-p, 0.0, big));
    let inner = invert((d - p, 0.0, small));
    let centre = (outer.0 + inner.0) / 2.0;
    let mid = (outer.2 + inner.2) / 2.0;
    let half = (outer.2 - inner.2).abs() / 2.0;
    // there every chain circle has radius half and turns by step around the
    // centre; the chain stops once one more would overlap the first
    let step = 2.0 * (half / mid).asin();
    let count = (2.0 * PI / step + SLACK).floor();
    let span = (count - 1.0) * step;
    let gap = |theta: f64| {
        let a = invert((centre + mid * theta.cos(), mid * theta.sin(), half));
        let t = theta + span;
        let z = invert((centre + mid * t.cos(), mid * t.sin(), half));
        (a.0 - z.0).hypot(a.1 - z.1) - a.2 - z.2
    };
    // the best chain is symmetric about the line through the centres
    let best = gap(-span / 2.0).min(gap(PI - span / 2.0));
    println!("{:.10}", best.max(0.0));
}
