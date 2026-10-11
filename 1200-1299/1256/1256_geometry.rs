use std::f64::consts::PI;
use std::io::{self, Read};

const STEPS: usize = 70; // golden-section steps: the bracket shrinks by 0.618 each
const SAMPLES: usize = 24; // first look along circle B, before refining
const GOLD: f64 = 0.618_033_988_749_894_9; // (sqrt 5 - 1) / 2

// the least value of a function with one minimum on [lo, hi]
fn golden<F: Fn(f64) -> f64>(f: F, mut lo: f64, mut hi: f64) -> f64 {
    let (mut a, mut b) = (hi - GOLD * (hi - lo), lo + GOLD * (hi - lo));
    let (mut fa, mut fb) = (f(a), f(b));
    for _ in 0..STEPS {
        if fa < fb {
            hi = b;
            b = a;
            fb = fa;
            a = hi - GOLD * (hi - lo);
            fa = f(a);
        } else {
            lo = a;
            a = b;
            fa = fb;
            b = lo + GOLD * (hi - lo);
            fb = f(b);
        }
    }
    fa.min(fb)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<f64>().unwrap());
    let mut next = || it.next().unwrap();
    let (r1, r2, r3, r) = (next(), next(), next(), next());
    // a dog is fed from the house itself: then the tour goes to the other
    // dog's circle and back, and nothing shorter exists
    if r1.min(r2) <= r {
        println!("{:.3}", 2.0 * (r1.max(r2) - r).max(0.0));
        return;
    }
    // posts at (0, 0) and (r3, 0), the house above them
    let hx = if r3 > 0.0 {
        (r1 * r1 - r2 * r2 + r3 * r3) / (2.0 * r3)
    } else {
        r1
    };
    let hy = (r1 * r1 - hx * hx).max(0.0).sqrt();
    let bx = r3;
    // the shortest way from P to the circle of dog B and on home
    let to_b = |px: f64, py: f64| -> f64 {
        let (dx, dy) = (hx - px, hy - py);
        let length = dx.hypot(dy);
        let t = if length > 0.0 {
            (((bx - px) * dx - py * dy) / (length * length)).clamp(0.0, 1.0)
        } else {
            0.0
        };
        if (px + t * dx - bx).hypot(py + t * dy) <= r {
            return length;
        }
        let via = |phi: f64| {
            let (qx, qy) = (bx + r * phi.cos(), r * phi.sin());
            (qx - px).hypot(qy - py) + (hx - qx).hypot(hy - qy)
        };
        let step = 2.0 * PI / SAMPLES as f64;
        let best = (1..SAMPLES).fold(0, |b, k| {
            if via(k as f64 * step) < via(b as f64 * step) {
                k
            } else {
                b
            }
        });
        golden(via, (best as f64 - 1.0) * step, (best as f64 + 1.0) * step)
    };
    // the tour length is convex in P inside dog A's circle, so a golden
    // search over x of golden searches over y finds its least value
    let column = |px: f64| {
        let half = (r * r - px * px).max(0.0).sqrt();
        golden(|py| (hx - px).hypot(hy - py) + to_b(px, py), -half, half)
    };
    println!("{:.3}", golden(column, -r, r));
}
