use std::io::{self, Read};

const EPS: f64 = 1e-7;

type Pt = (f64, f64);

/// The common points of two circles.
fn circles(a: Pt, ra: f64, b: Pt, rb: f64, out: &mut Vec<Pt>) {
    let (dx, dy) = (b.0 - a.0, b.1 - a.1);
    let d2 = dx * dx + dy * dy;
    if d2 == 0.0 {
        return;
    }
    let along = (d2 + ra * ra - rb * rb) / (2.0 * d2);
    let h2 = ra * ra / d2 - along * along;
    if h2 < -EPS {
        return;
    }
    let h = h2.max(0.0).sqrt();
    let (x, y) = (a.0 + dx * along, a.1 + dy * along);
    out.push((x - dy * h, y + dx * h));
    out.push((x + dy * h, y - dx * h));
}

/// The common points of the line nx * x + ny * y = c (unit normal) and a
/// circle.
fn line_circle(nx: f64, ny: f64, c: f64, centre: Pt, radius: f64, out: &mut Vec<Pt>) {
    let off = nx * centre.0 + ny * centre.1 - c;
    let h2 = radius * radius - off * off;
    if h2 < -EPS {
        return;
    }
    let h = h2.max(0.0).sqrt();
    let (x, y) = (centre.0 - nx * off, centre.1 - ny * off);
    out.push((x - ny * h, y + nx * h));
    out.push((x + ny * h, y - nx * h));
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<f64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = v[0] as usize;
    let pts: Vec<Pt> = (0..n).map(|i| (v[1 + 2 * i], v[2 + 2 * i])).collect();
    let (small, big) = (v[1 + 2 * n], v[2 + 2 * n]);
    let turn: f64 = (0..n)
        .map(|i| {
            let (a, b) = (pts[(i + n - 1) % n], pts[i]);
            a.0 * b.1 - b.0 * a.1
        })
        .sum();
    let side = if turn > 0.0 { 1.0 } else { -1.0 };
    // per edge: start, direction, outward unit normal and its offset
    let edges: Vec<(Pt, Pt, Pt, f64)> = (0..n)
        .map(|i| {
            let (a, b) = (pts[(i + n - 1) % n], pts[i]);
            let (ex, ey) = (b.0 - a.0, b.1 - a.1);
            let length = ex.hypot(ey);
            let (nx, ny) = (side * ey / length, -side * ex / length);
            (a, (ex, ey), (nx, ny), nx * a.0 + ny * a.1)
        })
        .collect();
    let reach = (big + EPS) * (big + EPS);
    let keep = (small - EPS) * (small - EPS);
    let fits = |p: Pt| {
        if pts.iter().any(|q| (p.0 - q.0).powi(2) + (p.1 - q.1).powi(2) > reach) {
            return false;
        }
        let mut outside = false;
        for &(a, e, nrm, c) in &edges {
            if nrm.0 * p.0 + nrm.1 * p.1 > c {
                outside = true;
            }
            let t = ((p.0 - a.0) * e.0 + (p.1 - a.1) * e.1) / (e.0 * e.0 + e.1 * e.1);
            let t = t.max(0.0).min(1.0);
            if (p.0 - a.0 - t * e.0).powi(2) + (p.1 - a.1 - t * e.1).powi(2) < keep {
                return false;
            }
        }
        outside
    };
    // the goat's area is where the discs of radius R around the vertices meet,
    // and when any of it is far enough from the bed, so is one of its corners
    // or a crossing of its boundary with the boundary of the bed grown by r
    let mut found = Vec::new();
    for i in 0..n {
        for j in 0..n {
            found.clear();
            if i < j {
                circles(pts[i], big, pts[j], big, &mut found);
            }
            circles(pts[i], big, pts[j], small, &mut found);
            let (_, _, nrm, c) = edges[j];
            line_circle(nrm.0, nrm.1, c + small, pts[i], big, &mut found);
            for &p in &found {
                if fits(p) {
                    println!("{:.6} {:.6}", p.0, p.1);
                    return;
                }
            }
        }
    }
    println!("No solution");
}
