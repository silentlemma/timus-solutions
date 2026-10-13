use std::collections::HashMap;
use std::io::{self, Read, Write};

type Point = (i64, i64);

fn gcd(a: i64, b: i64) -> i64 {
    let (mut a, mut b) = (a.abs(), b.abs());
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

fn cross(o: Point, a: Point, b: Point) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

/// Strict convex hull, counterclockwise, of sorted distinct points.
fn hull(pts: &[Point]) -> Vec<Point> {
    let mut h: Vec<Point> = Vec::with_capacity(2 * pts.len());
    for &p in pts {
        while h.len() >= 2 && cross(h[h.len() - 2], h[h.len() - 1], p) <= 0 {
            h.pop();
        }
        h.push(p);
    }
    let low = h.len() + 1;
    for &p in pts.iter().rev().skip(1) {
        while h.len() >= low && cross(h[h.len() - 2], h[h.len() - 1], p) <= 0 {
            h.pop();
        }
        h.push(p);
    }
    h.pop();
    h
}

/// Coordinates of the points in the frame o + s e1 + t e2 over their least
/// common denominator: the denominator first, then the pairs, sorted if asked.
fn in_frame(pts: &[Point], o: Point, e1: Point, e2: Point, sort_pairs: bool) -> Vec<i64> {
    let d = e1.0 * e2.1 - e1.1 * e2.0;
    let mut g = d;
    let mut pairs: Vec<(i64, i64)> = pts
        .iter()
        .map(|&(x, y)| {
            let (qx, qy) = (x - o.0, y - o.1);
            (qx * e2.1 - qy * e2.0, e1.0 * qy - e1.1 * qx)
        })
        .collect();
    for &(s, t) in &pairs {
        g = gcd(g, gcd(s, t));
    }
    if sort_pairs {
        pairs.sort_unstable();
    }
    let mut key = vec![d / g];
    for (s, t) in pairs {
        key.push(s / g);
        key.push(t / g);
    }
    key
}

/// The same for two point lists exactly when an affine map of positive
/// determinant takes one onto the other.
fn canonical(pts: &[Point]) -> Vec<i64> {
    let mut distinct = pts.to_vec();
    distinct.sort_unstable();
    distinct.dedup();
    if distinct.len() == 1 {
        return vec![0, pts.len() as i64];
    }
    let h = hull(&distinct);
    if h.len() == 2 {
        // on one line: positions from 0 to 1 between the ends, read either way
        let (dx, dy) = (h[1].0 - h[0].0, h[1].1 - h[0].1);
        let length = dx * dx + dy * dy;
        let mut forward: Vec<i64> = pts
            .iter()
            .map(|&(x, y)| (x - h[0].0) * dx + (y - h[0].1) * dy)
            .collect();
        let g = forward.iter().fold(length, |g, &t| gcd(g, t));
        let den = length / g;
        for t in forward.iter_mut() {
            *t /= g;
        }
        let mut backward: Vec<i64> = forward.iter().map(|t| den - t).collect();
        forward.sort_unstable();
        backward.sort_unstable();
        let mut key = vec![1, den];
        key.extend(forward.min(backward));
        return key;
    }
    // the frame at hull vertex i: it goes to 0, the next to (1, 0) and the
    // previous to (0, 1); a map of positive determinant keeps the order
    let k = h.len();
    let frame_key = |i: usize, points: &[Point], sort_pairs: bool| {
        let (o, nxt, prv) = (h[i], h[(i + 1) % k], h[(i + k - 1) % k]);
        in_frame(
            points,
            o,
            (nxt.0 - o.0, nxt.1 - o.1),
            (prv.0 - o.0, prv.1 - o.1),
            sort_pairs,
        )
    };
    let shapes: Vec<Vec<i64>> = (0..k)
        .map(|i| {
            let turned: Vec<Point> = h[i..].iter().chain(h[..i].iter()).cloned().collect();
            frame_key(i, &turned, false)
        })
        .collect();
    let best = shapes.iter().min().unwrap().clone();
    let chosen = (0..k)
        .filter(|&i| shapes[i] == best)
        .map(|i| frame_key(i, pts, true))
        .min()
        .unwrap();
    let mut key = vec![2, k as i64];
    key.extend(chosen);
    key
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut classes: HashMap<Vec<i64>, (usize, Vec<usize>)> = HashMap::new();
    for project in 1..=n {
        let m = it.next().unwrap() as usize;
        let pts: Vec<Point> = (0..m)
            .map(|_| (it.next().unwrap(), it.next().unwrap()))
            .collect();
        let entry = classes.entry(canonical(&pts)).or_insert((m, Vec::new()));
        entry.1.push(project);
    }
    // smaller projects first, then by the first project of the class
    let mut order: Vec<&(usize, Vec<usize>)> = classes.values().collect();
    order.sort_by_key(|c| (c.0, c.1[0]));
    let mut out = format!("{}\n", order.len());
    for (_, members) in order {
        for p in members {
            out.push_str(&format!("{} ", p));
        }
        out.push_str("0\n");
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
