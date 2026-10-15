use std::io::{self, Read};

const EPS: f64 = 1e-9;
const SIDES: usize = 4;
const POINTS: usize = SIDES + 1;

struct Scene {
    p: [(f64, f64); POINTS], // the mouse, then the corners of the book
    c: (f64, f64),
    r: f64,
}

impl Scene {
    // positive inside the book (the corners go counterclockwise)
    fn side(&self, i: usize, x: f64, y: f64) -> f64 {
        let (a, b) = (self.p[1 + i], self.p[1 + (i + 1) % SIDES]);
        (b.0 - a.0) * (y - a.1) - (b.1 - a.1) * (x - a.0)
    }

    fn outside(&self, x: f64, y: f64) -> bool {
        (0..SIDES).any(|i| self.side(i, x, y) < -EPS)
    }

    // whether the segment passes through the inside of the book
    fn blocks(&self, a: (f64, f64), b: (f64, f64)) -> bool {
        let (mut lo, mut hi) = (0.0f64, 1.0f64);
        for i in 0..SIDES {
            let (f0, f1) = (self.side(i, a.0, a.1), self.side(i, b.0, b.1));
            if f0 <= EPS && f1 <= EPS {
                return false;
            }
            if f0 < f1 && f0 <= EPS {
                lo = lo.max((EPS - f0) / (f1 - f0));
            }
            if f1 < f0 && f1 <= EPS {
                hi = hi.min((f0 - EPS) / (f0 - f1));
            }
        }
        hi - lo > EPS
    }

    // the closest point of the disk outside the book that s sees
    fn nearest(&self, s: (f64, f64)) -> f64 {
        let (c, r) = (self.c, self.r);
        let mut best = f64::INFINITY;
        let d = (s.0 - c.0).hypot(s.1 - c.1);
        if d > EPS {
            let q = (c.0 + (s.0 - c.0) * r / d, c.1 + (s.1 - c.1) * r / d);
            if self.outside(q.0, q.1) && !self.blocks(s, q) {
                best = (d - r).max(0.0);
            }
        }
        for i in 0..SIDES {
            if self.side(i, s.0, s.1) > EPS {
                continue;
            }
            // the part of side i inside the disk, as a parameter range on it
            let (a, b) = (self.p[1 + i], self.p[1 + (i + 1) % SIDES]);
            let (ex, ey) = (b.0 - a.0, b.1 - a.1);
            let qa = ex * ex + ey * ey;
            let qb = (a.0 - c.0) * ex + (a.1 - c.1) * ey;
            let qc = (a.0 - c.0).powi(2) + (a.1 - c.1).powi(2) - r * r;
            let disc = qb * qb - qa * qc;
            if disc <= 0.0 {
                continue;
            }
            let lo = ((-qb - disc.sqrt()) / qa).max(0.0);
            let hi = ((-qb + disc.sqrt()) / qa).min(1.0);
            if (hi - lo) * qa.sqrt() <= EPS {
                continue;
            }
            let t = (((s.0 - a.0) * ex + (s.1 - a.1) * ey) / qa).max(lo).min(hi);
            best = best.min((a.0 + t * ex - s.0).hypot(a.1 + t * ey - s.1));
        }
        best
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let mut it = v.into_iter();
    let mut next = || it.next().unwrap();
    let mut p = [(0.0, 0.0); POINTS];
    for corner in p.iter_mut().skip(1) {
        *corner = (next(), next());
    }
    let c = (next(), next());
    let r = next();
    p[0] = (next(), next());
    let scene = Scene { p, c, r };
    // the mouse goes straight or around corners of the book; Dijkstra over
    // the mouse and the corners gives each its shortest way from the start
    let mut dist = [f64::INFINITY; POINTS];
    let mut done = [false; POINTS];
    dist[0] = 0.0;
    for _ in 0..POINTS {
        let u = (0..POINTS)
            .filter(|&w| !done[w])
            .min_by(|&a, &b| dist[a].partial_cmp(&dist[b]).unwrap())
            .unwrap();
        done[u] = true;
        for w in 1..POINTS {
            let gap = (u + SIDES - w) % SIDES;
            let joined = if u == 0 {
                !scene.blocks(p[0], p[w])
            } else {
                gap == 1 || gap == SIDES - 1
            };
            if w != u && joined {
                let step = (p[w].0 - p[u].0).hypot(p[w].1 - p[u].1);
                dist[w] = dist[w].min(dist[u] + step);
            }
        }
    }
    let answer = (0..POINTS).map(|k| dist[k] + scene.nearest(p[k])).fold(f64::INFINITY, f64::min);
    println!("{:.5}", answer);
}
