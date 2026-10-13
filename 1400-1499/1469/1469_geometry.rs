use std::io::{self, Read};
use std::process::exit;

const SHEAR: i64 = 20001; // x' = SHEAR x + y keeps all points apart and no segment vertical
const FIELDS: usize = 4; // a cigarette: x1, y1, x2, y2

type Pt = (i64, i64);

fn orient(a: Pt, b: Pt, c: Pt) -> i64 {
    ((b.0 - a.0) * (c.1 - a.1) - (b.1 - a.1) * (c.0 - a.0)).signum()
}

fn on_box(a: Pt, b: Pt, c: Pt) -> bool {
    a.0.min(b.0) <= c.0 && c.0 <= a.0.max(b.0) && a.1.min(b.1) <= c.1 && c.1 <= a.1.max(b.1)
}

/// Closed segments pq and rs share a point.
fn touch(p: Pt, q: Pt, r: Pt, s: Pt) -> bool {
    let (o1, o2, o3, o4) = (
        orient(p, q, r),
        orient(p, q, s),
        orient(r, s, p),
        orient(r, s, q),
    );
    if o1 * o2 < 0 && o3 * o4 < 0 {
        return true;
    }
    (o1 == 0 && on_box(p, q, r))
        || (o2 == 0 && on_box(p, q, s))
        || (o3 == 0 && on_box(r, s, p))
        || (o4 == 0 && on_box(r, s, q))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let plain: Vec<(Pt, Pt)> = v[1..1 + FIELDS * n]
        .chunks(FIELDS)
        .map(|c| match *c {
            [x1, y1, x2, y2] => ((x1, y1), (x2, y2)),
            _ => unreachable!(),
        })
        .collect();
    // Shamos-Hoey: sweep a vertical line over the sheared plane, keep the
    // segments it crosses ordered by height, and test only neighbours
    let seg: Vec<(Pt, Pt)> = plain
        .iter()
        .map(|&(a, b)| {
            let (sa, sb) = ((SHEAR * a.0 + a.1, a.1), (SHEAR * b.0 + b.1, b.1));
            if sb.0 < sa.0 {
                (sb, sa)
            } else {
                (sa, sb)
            }
        })
        .collect();
    // the sign of the height of segment i above point p, at the x of p
    let side = |i: usize, p: Pt| -> i64 {
        let ((x1, y1), (x2, y2)) = seg[i];
        (y1 * (x2 - x1) + (y2 - y1) * (p.0 - x1) - p.1 * (x2 - x1)).signum()
    };
    let slope_less = |i: usize, j: usize| -> bool {
        let ((a1, b1), (a2, b2)) = seg[i];
        let ((c1, d1), (c2, d2)) = seg[j];
        (b2 - b1) * (c2 - c1) < (d2 - d1) * (a2 - a1)
    };
    let meet = |i: usize, j: usize| {
        if touch(plain[i].0, plain[i].1, plain[j].0, plain[j].1) {
            println!("YES\n{} {}", i + 1, j + 1);
            exit(0);
        }
    };
    // at one x, segments starting there come before those ending there
    let mut events: Vec<(i64, u8, usize)> = Vec::with_capacity(2 * n);
    for (i, s) in seg.iter().enumerate() {
        events.push((s.0 .0, 0, i));
        events.push((s.1 .0, 1, i));
    }
    events.sort_unstable();
    let mut line: Vec<usize> = Vec::new();
    for &(_, kind, i) in &events {
        if kind == 0 {
            let p = seg[i].0;
            let (mut lo, mut hi) = (0, line.len());
            while lo < hi {
                let mid = (lo + hi) / 2;
                let c = side(line[mid], p);
                if c < 0 || (c == 0 && slope_less(line[mid], i)) {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            line.insert(lo, i);
            if lo > 0 {
                meet(i, line[lo - 1]);
            }
            if lo + 1 < line.len() {
                meet(i, line[lo + 1]);
            }
        } else {
            let p = seg[i].1;
            let (mut lo, mut hi) = (0, line.len());
            while lo < hi {
                let mid = (lo + hi) / 2;
                if side(line[mid], p) < 0 {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            let mut k = lo;
            while k < line.len() && line[k] != i {
                k += 1;
            }
            if k == line.len() {
                k = line.iter().position(|&x| x == i).unwrap();
            }
            line.remove(k);
            if k > 0 && k < line.len() {
                meet(line[k - 1], line[k]);
            }
        }
    }
    println!("NO");
}
