use std::io::{self, Read};

const CORNERS: usize = 3;
const ROUNDS: usize = 200; // bisection steps, far beyond double precision

type Point = (f64, f64);

fn shoelace(poly: &[Point]) -> f64 {
    let n = poly.len();
    let twice: f64 = (0..n)
        .map(|i| {
            let (a, b) = (poly[(i + n - 1) % n], poly[i]);
            a.0 * b.1 - b.0 * a.1
        })
        .sum();
    twice.abs() / 2.0
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<f64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let pts: Vec<Point> = nums.chunks(2).map(|c| (c[0], c[1])).collect();
    let sides: Vec<f64> = (0..CORNERS)
        .map(|i| {
            let (a, b) = (pts[i], pts[(i + 1) % CORNERS]);
            (b.0 - a.0).hypot(b.1 - a.1)
        })
        .collect();
    let perimeter: f64 = sides.iter().sum();
    // arc positions of the corners along the coast, twice round
    let mut marks: Vec<(f64, Point)> = Vec::new();
    let mut pos = 0.0;
    for _ in 0..2 {
        for i in 0..CORNERS {
            marks.push((pos, pts[i]));
            pos += sides[i];
        }
    }
    // the coast point at arc length s from the first corner
    let at = |s: f64| -> Point {
        let mut s = s % perimeter;
        for i in 0..CORNERS {
            if s <= sides[i] || i == CORNERS - 1 {
                let t = (s / sides[i]).min(1.0);
                let (a, b) = (pts[i], pts[(i + 1) % CORNERS]);
                return (a.0 + (b.0 - a.0) * t, a.1 + (b.1 - a.1) * t);
            }
            s -= sides[i];
        }
        pts[0]
    };
    // area cut off by the coast from s to t (s < t) and the chord
    let area = |s: f64, t: f64| -> f64 {
        let mut poly = vec![at(s)];
        poly.extend(marks.iter().filter(|m| s < m.0 && m.0 < t).map(|m| m.1));
        poly.push(at(t));
        shoelace(&poly)
    };
    let half = perimeter / 2.0;
    let total = shoelace(&pts);
    let excess = |s: f64| area(s, s + half) - total / 2.0;
    // the excess changes sign over half a turn, as the other part is the
    // complement, so a chord splitting both evenly always exists
    let (mut lo, mut hi) = (0.0, half);
    let low = excess(lo) > 0.0;
    for _ in 0..ROUNDS {
        let mid = (lo + hi) / 2.0;
        if (excess(mid) > 0.0) == low {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    let s = (lo + hi) / 2.0;
    let (a, b) = (at(s), at(s + half));
    println!("YES\n{:.12} {:.12}\n{:.12} {:.12}", a.0, a.1, b.0, b.1);
}
