use std::io::{self, Read};

const EPS: f64 = 1e-9;
const BOX: f64 = 2.0; // the starting cell is a square of half-side BOX * R around the table
const SPAN: f64 = 4.0; // a piece cuts a cell only within twice its reach: squared, 4 times

type Pt = (f64, f64);

fn norm2(p: Pt) -> f64 {
    p.0 * p.0 + p.1 * p.1
}

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

// a point of the table edge where piece i is the nearest: the Voronoi cell
// of the piece is convex and reaches the edge exactly when its farthest
// vertex from the centre is at least R away
fn seat(pieces: &[Pt], i: usize, r: f64) -> Option<Pt> {
    let c = pieces[i];
    let (side, limit) = (BOX * r, r * r - EPS);
    let mut poly = vec![(-side, -side), (side, -side), (side, side), (-side, side)];
    let dist: Vec<f64> = pieces
        .iter()
        .map(|p| norm2((p.0 - c.0, p.1 - c.1)))
        .collect();
    let mut order: Vec<usize> = (0..pieces.len()).collect();
    order.sort_by(|&a, &b| dist[a].partial_cmp(&dist[b]).unwrap());
    for &j in &order {
        if j == i {
            continue;
        }
        let reach = poly
            .iter()
            .map(|v| norm2((v.0 - c.0, v.1 - c.1)))
            .fold(0.0, f64::max);
        if dist[j] > SPAN * reach {
            break; // farther than twice the cell's reach: cannot cut it
        }
        let o = pieces[j];
        poly = clip(
            &poly,
            ((o.0 + c.0) / 2.0, (o.1 + c.1) / 2.0),
            (o.0 - c.0, o.1 - c.1),
        );
        if poly.iter().map(|&v| norm2(v)).fold(0.0, f64::max) < limit {
            return None;
        }
    }
    let v = poly
        .iter()
        .copied()
        .fold((0.0, 0.0), |a, b| if norm2(b) > norm2(a) { b } else { a });
    // the segment from the piece to that vertex lies in the cell and crosses
    // the edge: solve |c + t (v - c)| = R
    let u = (v.0 - c.0, v.1 - c.1);
    let (a, b, cc) = (norm2(u), c.0 * u.0 + c.1 * u.1, norm2(c) - r * r);
    let t = ((-b + (b * b - a * cc).max(0.0).sqrt()) / a).min(1.0);
    let p = (c.0 + t * u.0, c.1 + t * u.1);
    let len = norm2(p).sqrt();
    Some((p.0 * r / len, p.1 * r / len))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let r: f64 = it.next().unwrap().parse().unwrap();
    let k: usize = it.next().unwrap().parse().unwrap();
    let mut pieces = Vec::with_capacity(k);
    let mut weight = Vec::with_capacity(k);
    for _ in 0..k {
        let x: f64 = it.next().unwrap().parse().unwrap();
        let y: f64 = it.next().unwrap().parse().unwrap();
        pieces.push((x, y));
        weight.push(it.next().unwrap().parse::<i32>().unwrap());
    }
    let mut order: Vec<usize> = (0..k).collect();
    order.sort_by(|&a, &b| weight[b].cmp(&weight[a]));
    for i in order {
        if let Some(p) = seat(&pieces, i, r) {
            println!("{:.10} {:.10}", p.0, p.1);
            return;
        }
    }
}
