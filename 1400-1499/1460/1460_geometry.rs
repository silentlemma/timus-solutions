use std::f64::consts::PI;
use std::io::{self, Read};

type Pt = (f64, f64);

const CORNERS: usize = 3;
const PINS: usize = 4;
const WIDE: f64 = 2.0 * PI / 3.0; // 120 degrees
const EPS: f64 = 1e-12;
// the pairs that share an extra point, each way round
const PAIRINGS: [[[usize; 2]; 2]; 6] = [
    [[0, 1], [2, 3]],
    [[0, 2], [1, 3]],
    [[0, 3], [1, 2]],
    [[2, 3], [0, 1]],
    [[1, 3], [0, 2]],
    [[1, 2], [0, 3]],
];
// sqrt(3) / 2, the height of a unit equilateral triangle
const ROOT3: f64 = 0.866_025_403_784_438_6;

fn dist(p: Pt, q: Pt) -> f64 {
    (p.0 - q.0).hypot(p.1 - q.1)
}

/// The point with the least total distance to three points (see 1451).
fn fermat(p: [Pt; CORNERS]) -> Pt {
    for i in 0..CORNERS {
        for j in i + 1..CORNERS {
            if dist(p[i], p[j]) < EPS {
                return p[i];
            }
        }
    }
    let mut angle = [0.0; CORNERS];
    let mut side = [0.0; CORNERS];
    for i in 0..CORNERS {
        let (a, b, c) = (p[i], p[(i + 1) % CORNERS], p[(i + 2) % CORNERS]);
        let (ux, uy, wx, wy) = (b.0 - a.0, b.1 - a.1, c.0 - a.0, c.1 - a.1);
        angle[i] = (ux * wy - uy * wx).abs().atan2(ux * wx + uy * wy);
        side[i] = dist(b, c);
    }
    for i in 0..CORNERS {
        if angle[i] >= WIDE {
            return p[i];
        }
    }
    let (mut total, mut x, mut y) = (0.0, 0.0, 0.0);
    for i in 0..CORNERS {
        let w = side[i] / (angle[i] + PI / CORNERS as f64).sin();
        total += w;
        x += w * p[i].0;
        y += w * p[i].1;
    }
    (x / total, y / total)
}

fn shortest(p: &[Pt; PINS]) -> f64 {
    // trees without extra points: the best spanning tree
    let mut edges = Vec::new();
    for i in 0..PINS {
        for j in i + 1..PINS {
            edges.push((dist(p[i], p[j]), i, j));
        }
    }
    edges.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
    let mut group: Vec<usize> = (0..PINS).collect();
    let mut best = 0.0;
    for (length, i, j) in edges {
        let (mut a, mut b) = (i, j);
        while group[a] != a {
            a = group[a];
        }
        while group[b] != b {
            b = group[b];
        }
        if a != b {
            group[a] = b;
            best += length;
        }
    }
    // one extra point joining three pins, the fourth wired to one of the four
    for rest in 0..PINS {
        let others: Vec<Pt> = (0..PINS).filter(|&i| i != rest).map(|i| p[i]).collect();
        let trio = [others[0], others[1], others[2]];
        let s = fermat(trio);
        let star: f64 = trio.iter().map(|&q| dist(s, q)).sum();
        let link = trio
            .iter()
            .map(|&q| dist(p[rest], q))
            .fold(dist(p[rest], s), f64::min);
        best = f64::min(best, star + link);
    }
    // two extra points, {a, b} on one and {c, d} on the other: the Melzak
    // construction gives both, and the real length of that tree is a candidate
    for pr in PAIRINGS.iter() {
        let (a, b, c, d) = (p[pr[0][0]], p[pr[0][1]], p[pr[1][0]], p[pr[1][1]]);
        let (mx, my) = ((a.0 + b.0) / 2.0, (a.1 + b.1) / 2.0);
        let (dx, dy) = (b.0 - a.0, b.1 - a.1);
        for side in [1.0, -1.0] {
            let e = (mx - side * dy * ROOT3, my + side * dx * ROOT3);
            let s2 = fermat([e, c, d]);
            let s1 = fermat([a, b, s2]);
            let tree = dist(s1, a) + dist(s1, b) + dist(s1, s2) + dist(s2, c) + dist(s2, d);
            best = f64::min(best, tree);
        }
    }
    best
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let tests = v[0] as usize;
    let mut out = String::new();
    for t in 0..tests {
        let mut p = [(0.0, 0.0); PINS];
        for (i, q) in p.iter_mut().enumerate() {
            let k = 1 + 2 * (PINS * t + i);
            *q = (v[k], v[k + 1]);
        }
        out.push_str(&format!("{:.6}\n", shortest(&p)));
    }
    print!("{}", out);
}
