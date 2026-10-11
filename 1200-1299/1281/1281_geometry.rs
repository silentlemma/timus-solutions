use std::collections::HashMap;
use std::io::{self, Read};

type P = (f64, f64);

fn cross(o: P, a: P, b: P) -> f64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

// area of the convex hull, by the monotone chain and the shoelace
fn hull_area(mut pts: Vec<P>) -> f64 {
    pts.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mut h: Vec<P> = Vec::new();
    for &p in &pts {
        while h.len() >= 2 && cross(h[h.len() - 2], h[h.len() - 1], p) <= 0.0 {
            h.pop();
        }
        h.push(p);
    }
    let t = h.len() + 1;
    for &p in pts.iter().rev().skip(1) {
        while h.len() >= t && cross(h[h.len() - 2], h[h.len() - 1], p) <= 0.0 {
            h.pop();
        }
        h.push(p);
    }
    let area: f64 = h
        .windows(2)
        .map(|w| w[0].0 * w[1].1 - w[0].1 * w[1].0)
        .sum();
    area.abs() / 2.0
}

fn basin(i: usize, rivers: &[Vec<P>], tributaries: &[Vec<usize>], out: &mut Vec<P>) {
    out.extend_from_slice(&rivers[i]);
    for &t in &tributaries[i] {
        basin(t, rivers, tributaries, out);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut rivers: Vec<Vec<P>> = Vec::new();
    for _ in 0..n {
        let k: usize = words.next().unwrap().parse().unwrap();
        let r = (0..k)
            .map(|_| {
                (
                    words.next().unwrap().parse().unwrap(),
                    words.next().unwrap().parse().unwrap(),
                )
            })
            .collect();
        rivers.push(r);
    }
    // a river is a tributary of the one whose inner vertex is its mouth
    let key = |p: P| (p.0.to_bits(), p.1.to_bits());
    let mut owner = HashMap::new();
    for (i, r) in rivers.iter().enumerate() {
        for &p in r.iter().skip(1).take(r.len().saturating_sub(2)) {
            owner.insert(key(p), i);
        }
    }
    let mut tributaries = vec![Vec::new(); n];
    for (i, r) in rivers.iter().enumerate() {
        if let Some(&o) = owner.get(&key(r[r.len() - 1])) {
            if o != i {
                tributaries[o].push(i);
            }
        }
    }
    let mut best = 0.0f64;
    for i in 0..n {
        let mut pts = Vec::new();
        basin(i, &rivers, &tributaries, &mut pts);
        best = best.max(hull_area(pts));
    }
    println!("{:.2}", best);
}
