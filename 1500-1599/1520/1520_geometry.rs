use std::io::{self, Read};

const BOX: f64 = 2.0; // the starting cell is a square of half-side BOX * R around the disk
const SPAN: f64 = 4.0; // a site cuts a cell only within twice its reach: squared, 4 times
const EPS: f64 = 1e-9;

type Pt = (f64, f64);

// the part of the convex polygon with (p - m) . d <= 0
fn clip(poly: &[Pt], m: Pt, d: Pt) -> Vec<Pt> {
    let n = poly.len();
    let mut out = Vec::with_capacity(n + 1);
    for k in 0..n {
        let (p, q) = (poly[k], poly[(k + 1) % n]);
        let sp = (p.0 - m.0) * d.0 + (p.1 - m.1) * d.1;
        let sq = (q.0 - m.0) * d.0 + (q.1 - m.1) * d.1;
        if sp <= 0.0 {
            out.push(p);
        }
        if (sp < 0.0 && sq > 0.0) || (sq < 0.0 && sp > 0.0) {
            let t = sp / (sp - sq);
            out.push((p.0 + t * (q.0 - p.0), p.1 + t * (q.1 - p.1)));
        }
    }
    out
}

// whether the point lies in the convex polygon, counterclockwise
fn inside(poly: &[Pt], a: Pt) -> bool {
    let n = poly.len();
    (0..n).all(|k| {
        let (p, q) = (poly[k], poly[(k + 1) % n]);
        (q.0 - p.0) * (a.1 - p.1) - (q.1 - p.1) * (a.0 - p.0) >= -EPS
    })
}

// the largest distance from c to a point of the polygon inside the disk of
// radius r around the origin
fn farthest(poly: &[Pt], c: Pt, r: f64) -> f64 {
    let mut best: f64 = 0.0;
    let n = poly.len();
    for k in 0..n {
        let (p, q) = (poly[k], poly[(k + 1) % n]);
        if p.0 * p.0 + p.1 * p.1 <= r * r {
            best = best.max((p.0 - c.0).hypot(p.1 - c.1));
        }
        // where the edge crosses the circle: |p + t (q - p)| = r
        let (ux, uy) = (q.0 - p.0, q.1 - p.1);
        let (a, b, cc) = (
            ux * ux + uy * uy,
            p.0 * ux + p.1 * uy,
            p.0 * p.0 + p.1 * p.1 - r * r,
        );
        let disc = b * b - a * cc;
        if a > 0.0 && disc >= 0.0 {
            for t in [(-b - disc.sqrt()) / a, (-b + disc.sqrt()) / a] {
                if (0.0..=1.0).contains(&t) {
                    best = best.max((p.0 + t * ux - c.0).hypot(p.1 + t * uy - c.1));
                }
            }
        }
    }
    // on an arc inside the cell the distance peaks at the circle point
    // opposite the site, if that point is in the cell
    let norm = c.0.hypot(c.1);
    let o = if norm > 0.0 {
        (-r * c.0 / norm, -r * c.1 / norm)
    } else {
        (r, 0.0)
    };
    if inside(poly, o) {
        best = best.max((o.0 - c.0).hypot(o.1 - c.1));
    }
    best
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, r) = (v[0] as usize, v[1]);
    let sites: Vec<Pt> = v[2..2 + 2 * n].chunks(2).map(|p| (p[0], p[1])).collect();
    let sq = |a: Pt, b: Pt| (a.0 - b.0).powi(2) + (a.1 - b.1).powi(2);
    let side = BOX * r;
    let mut answer: f64 = 0.0;
    for &c in &sites {
        let mut poly = vec![(-side, -side), (side, -side), (side, side), (-side, side)];
        let mut order: Vec<usize> = (0..n).collect();
        order.sort_by(|&a, &b| sq(sites[a], c).partial_cmp(&sq(sites[b], c)).unwrap());
        for j in order {
            let d = sq(sites[j], c);
            if d == 0.0 {
                continue; // the site itself, or another one at the same point
            }
            let reach = poly.iter().map(|&p| sq(p, c)).fold(0.0, f64::max);
            if d > SPAN * reach {
                break;
            }
            let o = sites[j];
            poly = clip(
                &poly,
                ((o.0 + c.0) / 2.0, (o.1 + c.1) / 2.0),
                (o.0 - c.0, o.1 - c.1),
            );
        }
        answer = answer.max(farthest(&poly, c, r));
    }
    println!("{:.8}", answer);
}
