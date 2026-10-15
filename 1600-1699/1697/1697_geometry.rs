use std::io::{self, Read};

const DIM: usize = 3; // coordinates of the sniper
const AREA: usize = 3; // corners of a polygon with an inside

const SIDES: usize = 4; // the wall constraints come first
// the fields of a building
const LX: usize = 0;
const LY: usize = 1;
const RX: usize = 2;
const RY: usize = 3;
const HEIGHT: usize = 4;
const FIELDS: usize = 5;

// (p, q, c): the closed half-plane p u + q v >= c
type Line = (i64, i64, i64);

// the open interval (lo_n / lo_d, hi_n / hi_d) of t
#[derive(Clone, Copy)]
struct Gap {
    lo_n: i64,
    lo_d: i64,
    hi_n: i64,
    hi_d: i64,
}

// the open interval of t for which the shot from S to A + t (B - A) passes
// through the inside of the box; a point of the shot is S + u (A - S) +
// v (B - A) with v = u t, so the box pulls back to a convex polygon in (u, v)
fn blocked_interval(s: &[i64], a: &[i64], b: &[i64], bx: &[i64]) -> Option<Gap> {
    let (ax, ay, dx, dy) = (a[0] - s[0], a[1] - s[1], b[0] - a[0], b[1] - a[1]);
    let mut cons: Vec<Line> = vec![
        (ax, dx, bx[LX] - s[0]),
        (-ax, -dx, s[0] - bx[RX]),
        (ay, dy, bx[LY] - s[1]),
        (-ay, -dy, s[1] - bx[RY]),
        (1, 0, 0),  // u >= 0
        (-1, 0, -1), // u <= 1
        (1, 1, 0),  // t >= -1 and t <= 2 keep the polygon bounded
        (2, -1, 0),
    ];
    if cons[..SIDES].iter().any(|&(p, q, c)| p == 0 && q == 0 && c >= 0) {
        return None; // the plane of the shots holds a wall or misses the box
    }
    if s[2] > 0 {
        cons.push((s[2], 0, s[2] - bx[HEIGHT])); // below the roof: sz (1 - u) <= h
    }
    let mut corners: Vec<(i64, i64, i64)> = Vec::new();
    for i in 0..cons.len() {
        for j in i + 1..cons.len() {
            let ((p1, q1, c1), (p2, q2, c2)) = (cons[i], cons[j]);
            let mut den = p1 * q2 - p2 * q1;
            if den == 0 {
                continue;
            }
            let (mut u, mut v) = (c1 * q2 - c2 * q1, p1 * c2 - p2 * c1);
            if den < 0 {
                den = -den;
                u = -u;
                v = -v;
            }
            let fits = cons.iter().all(|&(p, q, c)| p * u + q * v >= c * den);
            let fresh = corners
                .iter()
                .all(|&(cu, cv, cd)| !(u * cd == cu * den && v * cd == cv * den));
            if fits && fresh {
                corners.push((u, v, den));
            }
        }
    }
    // the polygon has an inside exactly when it has three different corners
    if corners.len() < AREA {
        return None;
    }
    // t = v / u, and u > 0 at every corner, as S is outside the box
    let (u0, v0, _) = corners[0];
    let mut gap = Gap { lo_n: v0, lo_d: u0, hi_n: v0, hi_d: u0 };
    for &(u, v, _) in &corners {
        if v * gap.lo_d < gap.lo_n * u {
            gap.lo_n = v;
            gap.lo_d = u;
        }
        if v * gap.hi_d > gap.hi_n * u {
            gap.hi_n = v;
            gap.hi_d = u;
        }
    }
    Some(gap)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut take = |count: usize| -> Vec<i64> {
        (0..count).map(|_| words.next().unwrap()).collect()
    };
    let (s, a, b) = (take(DIM), take(2), take(2));
    let n = take(1)[0] as usize;
    let gaps: Vec<Gap> = (0..n)
        .filter_map(|_| blocked_interval(&s, &a, &b, &take(FIELDS)))
        .collect();
    // the free times form a closed set whose first point is 0 or the right
    // end of some blocked interval
    let mut candidates: Vec<(i64, i64)> = vec![(0, 1)];
    for g in &gaps {
        if 0 <= g.hi_n && g.hi_n <= g.hi_d {
            candidates.push((g.hi_n, g.hi_d));
        }
    }
    candidates.sort_by(|f, g| (f.0 * g.1).cmp(&(g.0 * f.1)));
    for &(tn, td) in &candidates {
        if gaps.iter().all(|g| !(g.lo_n * td < tn * g.lo_d && tn * g.hi_d < g.hi_n * td)) {
            let t = tn as f64 / td as f64;
            let x = a[0] as f64 + (b[0] - a[0]) as f64 * t;
            let y = a[1] as f64 + (b[1] - a[1]) as f64 * t;
            println!("{:.10} {:.10}", x, y);
            return;
        }
    }
    println!("Impossible");
}
