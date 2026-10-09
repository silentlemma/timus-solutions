use std::io::{self, Read};

const STAGES: usize = 3;

// a line (a, b, c), shifted by a tiny eps: a*x + b*y + c + eps < 0 is the
// half-plane kept
type Line = (i64, i64, i64);

// the corner of lines p and q, all shifted by eps: numerators of x and y as
// value plus eps coefficient, and the common denominator
struct Corner {
    x0: i128,
    xe: i128,
    y0: i128,
    ye: i128,
    det: i128,
}

fn corner(p: Line, q: Line) -> Corner {
    let (ap, bp, cp) = (p.0 as i128, p.1 as i128, p.2 as i128);
    let (aq, bq, cq) = (q.0 as i128, q.1 as i128, q.2 as i128);
    Corner {
        x0: -cp * bq + cq * bp,
        xe: bp - bq,
        y0: cp * aq - cq * ap,
        ye: aq - ap,
        det: ap * bq - aq * bp,
    }
}

// -1, 0 or 1: where the corner lies against the shifted line; the values
// stay below 3 * 10^37, inside 128 bits
fn side(v: Corner, l: Line) -> i32 {
    let (a, b, c) = (l.0 as i128, l.1 as i128, l.2 as i128);
    let mut t0 = a * v.x0 + b * v.y0 + c * v.det;
    let mut t1 = a * v.xe + b * v.ye + v.det;
    if v.det < 0 {
        t0 = -t0;
        t1 = -t1;
    }
    if t0 != 0 {
        t0.signum() as i32
    } else {
        t1.signum() as i32
    }
}

// cut the polygon, given by its lines in boundary order, by the line
fn clip(edges: &[Line], l: Line) -> Vec<Line> {
    let m = edges.len();
    let sides: Vec<i32> = (0..m)
        .map(|k| side(corner(edges[(k + m - 1) % m], edges[k]), l))
        .collect();
    // edge k runs from corner k to corner k + 1; it stays if part of it is inside
    let keep: Vec<bool> = (0..m)
        .map(|k| sides[k] < 0 || sides[(k + 1) % m] < 0)
        .collect();
    let mut out = Vec::new();
    let start = match keep.iter().position(|&k| k) {
        Some(s) => s,
        None => return out,
    };
    for step in 0..m {
        let k = (start + step) % m;
        let next = (k + 1) % m;
        if !keep[k] {
            continue;
        }
        out.push(edges[k]);
        // the boundary leaves the half-plane before the next kept edge
        if !keep[next] || sides[next] > 0 {
            out.push(l);
        }
    }
    if out.len() < STAGES {
        out.clear();
    }
    out
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = tok.next().unwrap() as usize;
    let s: Vec<Vec<i64>> = (0..n)
        .map(|_| tok.by_ref().take(STAGES).collect())
        .collect();
    // the sides of the triangle x > 0, y > 0, x + y < 1, in boundary order
    let triangle: Vec<Line> = vec![(0, -1, 0), (1, 1, -1), (-1, 0, 0)];
    let mut out = String::new();
    for i in 0..n {
        let mut edges = triangle.clone();
        for j in 0..n {
            if j == i || edges.is_empty() {
                continue;
            }
            // with u_k = length_k / s_ik > 0, i beats j when
            // sum (s_jk - s_ik) / s_jk * u_k < 0; times s_j1 s_j2 s_j3 the
            // coefficients are integers below 10^12
            let g: Vec<i64> = (0..STAGES)
                .map(|k| {
                    let others = s[j][(k + 1) % STAGES] * s[j][(k + 2) % STAGES];
                    (s[j][k] - s[i][k]) * others
                })
                .collect();
            // u_3 = 1 - x - y on the triangle
            let l = (g[0] - g[2], g[1] - g[2], g[2]);
            if l.0 == 0 && l.1 == 0 {
                if l.2 >= 0 {
                    edges.clear();
                }
                continue;
            }
            edges = clip(&edges, l);
        }
        out.push_str(if edges.is_empty() { "No\n" } else { "Yes\n" });
    }
    print!("{}", out);
}
