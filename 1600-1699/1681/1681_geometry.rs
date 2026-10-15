use std::io::{self, Read};

type P = (f64, f64);

fn cross(a: P, b: P, c: P) -> f64 {
    (b.0 - a.0) * (c.1 - a.1) - (b.1 - a.1) * (c.0 - a.0)
}

// the part of a convex polygon on the given side (sign of the cross
// product) of the line through a and b
fn clip(poly: &[P], a: P, b: P, sign: f64) -> Vec<P> {
    let mut out = Vec::new();
    for i in 0..poly.len() {
        let (p, q) = (poly[i], poly[(i + 1) % poly.len()]);
        let (sp, sq) = (cross(a, b, p) * sign, cross(a, b, q) * sign);
        if sp >= 0.0 {
            out.push(p);
        }
        if (sp > 0.0 && sq < 0.0) || (sp < 0.0 && sq > 0.0) {
            let t = sp / (sp - sq);
            out.push((p.0 + (q.0 - p.0) * t, p.1 + (q.1 - p.1) * t));
        }
    }
    out
}

fn area(poly: &[P]) -> f64 {
    let m = poly.len();
    (0..m)
        .map(|i| {
            let (a, b) = (poly[(i + m - 1) % m], poly[i]);
            a.0 * b.1 - b.0 * a.1
        })
        .sum::<f64>()
        / 2.0
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = v[0];
    let k = v[1].min(n - v[1]);
    let pts: Vec<P> = (0..n as usize)
        .map(|i| (v[2 + 2 * i] as f64, v[2 + 2 * i + 1] as f64))
        .collect();
    if k == 1 {
        // every rope lies along the fence: the rabbit cannot get in at all
        println!("{:.9}", 1.0);
        return;
    }
    let at = |j: i64| pts[j.rem_euclid(n) as usize];
    let whole = area(&pts);
    let mut reachable = 0.0;
    for i in 0..n {
        // the face next to side i is on the side's side of every rope; only
        // the ropes from vertices i + 1 - k, ..., i pass over that side
        let (p, q) = (at(i), at(i + 1));
        let mid = ((p.0 + q.0) / 2.0, (p.1 + q.1) / 2.0);
        let mut ropes = vec![i + 1 - k, i];
        ropes.extend(i + 2 - k..i);
        let mut face = pts.clone();
        for j in ropes {
            let (a, b) = (at(j), at(j + k));
            let sign = if cross(a, b, mid) > 0.0 { 1.0 } else { -1.0 };
            face = clip(&face, a, b, sign);
            if face.is_empty() {
                break;
            }
        }
        reachable += area(&face);
    }
    println!("{:.9}", (whole - reachable) / whole);
}
