use std::io::{self, Read};

const STEPS: usize = 200; // halvings of the search interval: far below the 1e-6 asked
const QUARTIC: usize = 4;

fn value(poly: &[f64], x: f64) -> f64 {
    poly.iter().fold(0.0, |s, &c| s * x + c)
}

fn sign(v: f64) -> i32 {
    (v > 0.0) as i32 - (v < 0.0) as i32
}

// points where poly changes sign inside (lo, hi); between neighbouring sign
// changes of the derivative the polynomial is monotone
fn sign_roots(poly: &[f64], lo: f64, hi: f64) -> Vec<f64> {
    if poly.len() < 2 {
        return Vec::new();
    }
    let n = poly.len() - 1;
    let deriv: Vec<f64> = (0..n).map(|i| poly[i] * (n - i) as f64).collect();
    let mut cuts = vec![lo];
    cuts.extend(sign_roots(&deriv, lo, hi));
    cuts.push(hi);
    let mut found = Vec::new();
    for w in cuts.windows(2) {
        let (mut a, mut b) = (w[0], w[1]);
        let (sa, sb) = (sign(value(poly, a)), sign(value(poly, b)));
        if sa == 0 || sb == 0 || sa == sb {
            continue;
        }
        for _ in 0..STEPS {
            let mid = (a + b) / 2.0;
            if sign(value(poly, mid)) == sa {
                a = mid;
            } else {
                b = mid;
            }
        }
        found.push((a + b) / 2.0);
    }
    found
}

// a root p/q of poly
fn rational_root(poly: &[i64]) -> Option<(i64, i64)> {
    let (lead, last) = (poly[0].abs(), poly[poly.len() - 1].abs());
    for q in (1..=lead).filter(|q| lead % q == 0) {
        for pa in (1..=last).filter(|pa| last % pa == 0) {
            for p in [pa, -pa] {
                // q^n f(p/q), exact in integers
                let (mut s, mut qp) = (0i64, 1i64);
                for &c in poly {
                    s = s * p + c * qp;
                    qp *= q;
                }
                if s == 0 {
                    return Some((p, q));
                }
            }
        }
    }
    None
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = nums[0] as usize;
    let mut poly = nums[1..n + 2].to_vec(); // the leading coefficient first
    let mut roots: Vec<f64> = Vec::new();
    // rational roots p/q, with p dividing the constant term and q the
    // leading one; dividing by (q x - p) keeps integer coefficients
    while poly.len() > 1 && poly[poly.len() - 1] == 0 {
        roots.push(0.0);
        poly.pop();
    }
    while poly.len() > 1 {
        let (p, q) = match rational_root(&poly) {
            Some(pq) => pq,
            None => break,
        };
        let mut out = vec![poly[0] / q];
        for i in 1..poly.len() - 1 {
            let prev = out[i - 1];
            out.push((poly[i] + p * prev) / q);
        }
        poly = out;
        roots.push(p as f64 / q as f64);
    }
    // what is left has no rational roots; a repeated irrational root would
    // need its quadratic twice, so only a0 (x^2 + b x + d)^2 can repeat
    if let [a0, c3, c2, c1, c0] = poly[..] {
        let u = QUARTIC as i64 * a0;
        let e = u * c2 - c3 * c3; // then b = 2 c3 / u, d = 2 e / u^2
        if 2 * c3 * e == c1 * u * u && e * e == c0 * u * u * u {
            let w = c3 * c3 - 2 * e; // the roots are (-c3 +- sqrt(w)) / u
            if w > 0 {
                let root = (w as f64).sqrt();
                for r in [
                    (-c3 as f64 - root) / u as f64,
                    (-c3 as f64 + root) / u as f64,
                ] {
                    roots.push(r);
                    roots.push(r);
                }
            }
            poly = vec![1];
        }
    }
    let rest: Vec<f64> = poly.iter().map(|&c| c as f64).collect();
    let bound = rest[1..]
        .iter()
        .fold(1.0f64, |m, &c| m.max(1.0 + (c / rest[0]).abs()));
    roots.extend(sign_roots(&rest, -bound, bound));
    roots.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let out: String = roots.iter().map(|r| format!("{:.10}\n", r)).collect();
    print!("{}", out);
}
