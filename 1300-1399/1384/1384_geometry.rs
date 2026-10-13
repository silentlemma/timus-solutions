use std::io::{self, Read};

const EPS: f64 = 1e-9;

/// Distance from an inner point to the fence, or -1 outside.
fn distance_to_fence(pts: &[(f64, f64)], px: f64, py: f64) -> f64 {
    let n = pts.len();
    let mut inside = false;
    let mut best = f64::INFINITY;
    for i in 0..n {
        let (ax, ay) = pts[i];
        let (bx, by) = pts[(i + 1) % n];
        if (ay > py) != (by > py) && px < ax + (py - ay) * (bx - ax) / (by - ay) {
            inside = !inside;
        }
        let (dx, dy) = (bx - ax, by - ay);
        let t = (((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)).clamp(0.0, 1.0);
        best = best.min((px - ax - t * dx).hypot(py - ay - t * dy));
    }
    if inside {
        best
    } else {
        -1.0
    }
}

/// Points o + t u whose distance to v equals base + slope t.
fn on_circle(
    o: (f64, f64),
    u: (f64, f64),
    base: f64,
    slope: f64,
    v: (f64, f64),
    out: &mut Vec<(f64, f64)>,
) {
    // |o + t u - v|^2 = (base + slope t)^2, or qa t^2 + 2 hb t + qc = 0
    let (wx, wy) = (o.0 - v.0, o.1 - v.1);
    let qa = u.0 * u.0 + u.1 * u.1 - slope * slope;
    let hb = wx * u.0 + wy * u.1 - base * slope;
    let qc = wx * wx + wy * wy - base * base;
    let disc = hb * hb - qa * qc;
    if disc < -EPS * (hb * hb + (qa * qc).abs()) {
        return;
    }
    // the stable form of the roots, also when qa is next to zero
    let q = -(hb + disc.max(0.0).sqrt().copysign(hb));
    if qa.abs() > EPS {
        out.push((o.0 + q / qa * u.0, o.1 + q / qa * u.1));
    }
    if q.abs() > EPS {
        out.push((o.0 + qc / q * u.0, o.1 + qc / q * u.1));
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let data: Vec<f64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = data[0] as usize;
    let pts: Vec<(f64, f64)> = (0..n).map(|i| (data[1 + 2 * i], data[2 + 2 * i])).collect();
    // each edge as a line a x + b y + c, positive inside
    let lines: Vec<(f64, f64, f64)> = (0..n)
        .map(|i| {
            let (ax, ay) = pts[i];
            let (bx, by) = pts[(i + 1) % n];
            let length = (bx - ax).hypot(by - ay);
            let (a, b) = (-(by - ay) / length, (bx - ax) / length);
            (a, b, -(a * ax + b * ay))
        })
        .collect();
    // only reflex vertices can be the nearest point of the fence from inside
    let reflex: Vec<(f64, f64)> = (0..n)
        .filter(|&i| {
            let (p, q, r) = (pts[(i + n - 1) % n], pts[i], pts[(i + 1) % n]);
            (q.0 - p.0) * (r.1 - q.1) - (q.1 - p.1) * (r.0 - q.0) < 0.0
        })
        .map(|i| pts[i])
        .collect();
    let k = reflex.len();
    let mut cand: Vec<(f64, f64)> = Vec::new();
    // three lines: a_i x + b_i y + c_i = r for all three, by Cramer's rule
    for i in 0..n {
        for j in i + 1..n {
            for l in j + 1..n {
                let (p, q, s) = (lines[i], lines[j], lines[l]);
                let det = p.0 * (q.1 - s.1) - p.1 * (q.0 - s.0) + (q.0 * s.1 - s.0 * q.1);
                if det.abs() < EPS {
                    continue;
                }
                let rx = -p.2 * (q.1 - s.1) - p.1 * (s.2 - q.2) + (s.2 * q.1 - q.2 * s.1);
                let ry = p.0 * (s.2 - q.2) + p.2 * (q.0 - s.0) + (s.0 * q.2 - q.0 * s.2);
                cand.push((rx / det, ry / det));
            }
        }
    }
    // two lines and a reflex vertex: on the bisector, as far from the vertex
    for i in 0..n {
        for j in i + 1..n {
            let (p, q) = (lines[i], lines[j]);
            let (da, db, dc) = (p.0 - q.0, p.1 - q.1, p.2 - q.2);
            let norm = da * da + db * db;
            if norm < EPS {
                continue;
            }
            let o = (-dc * da / norm, -dc * db / norm);
            let u = (-db, da);
            for &v in &reflex {
                let base = p.0 * o.0 + p.1 * o.1 + p.2;
                on_circle(o, u, base, p.0 * u.0 + p.1 * u.1, v, &mut cand);
            }
        }
    }
    // a line and two reflex vertices: on their perpendicular bisector
    for i in 0..k {
        for j in i + 1..k {
            let (v, w) = (reflex[i], reflex[j]);
            let o = ((v.0 + w.0) / 2.0, (v.1 + w.1) / 2.0);
            let u = (-(w.1 - v.1), w.0 - v.0);
            for p in &lines {
                let base = p.0 * o.0 + p.1 * o.1 + p.2;
                on_circle(o, u, base, p.0 * u.0 + p.1 * u.1, v, &mut cand);
            }
        }
    }
    // three reflex vertices: the centre of their circle
    for i in 0..k {
        for j in i + 1..k {
            for l in j + 1..k {
                let (p, q, r) = (reflex[i], reflex[j], reflex[l]);
                let d = 2.0 * (p.0 * (q.1 - r.1) + q.0 * (r.1 - p.1) + r.0 * (p.1 - q.1));
                if d.abs() < EPS {
                    continue;
                }
                let s1 = p.0 * p.0 + p.1 * p.1;
                let s2 = q.0 * q.0 + q.1 * q.1;
                let s3 = r.0 * r.0 + r.1 * r.1;
                cand.push((
                    (s1 * (q.1 - r.1) + s2 * (r.1 - p.1) + s3 * (p.1 - q.1)) / d,
                    (s1 * (r.0 - q.0) + s2 * (p.0 - r.0) + s3 * (q.0 - p.0)) / d,
                ));
            }
        }
    }
    let best = cand
        .iter()
        .map(|&(x, y)| distance_to_fence(&pts, x, y))
        .fold(0.0, f64::max);
    println!("{:.2}", best);
}
