use std::io::{self, Read};

const OUTER: f64 = 5.0; // three-point Gauss-Legendre weights, as 5/9 and 8/9
const MIDDLE: f64 = 8.0;
const TOTAL: f64 = 9.0;
const TOLERANCE: f64 = 1e-13;
const DEPTH: u32 = 50;
const NODE_SQUARE: f64 = 0.6; // the outer nodes are at +- sqrt(0.6) on [-1, 1]
const LIMIT: f64 = 20.0; // sinh(20) is about 2.4e8, beyond which the tails are negligible

struct Quartic {
    a: Vec<f64>, // the coefficients, lowest first
    node: f64,
}

impl Quartic {
    /// The integrand after x = sinh t, dx = cosh t dt.
    fn f(&self, t: f64) -> f64 {
        let x = t.sinh();
        let p = self.a.iter().rev().fold(0.0, |acc, &c| acc * x + c);
        t.cosh() / p
    }

    fn gauss(&self, lo: f64, hi: f64) -> f64 {
        let (mid, half) = ((lo + hi) / 2.0, (hi - lo) / 2.0);
        let nodes = OUTER * self.f(mid - half * self.node)
            + MIDDLE * self.f(mid)
            + OUTER * self.f(mid + half * self.node);
        half * nodes / TOTAL
    }

    /// Adaptive: split while the halves disagree with the whole.
    fn integrate(&self, lo: f64, hi: f64, whole: f64, depth: u32) -> f64 {
        let mid = (lo + hi) / 2.0;
        let (left, right) = (self.gauss(lo, mid), self.gauss(mid, hi));
        let both = left + right;
        if depth == 0 || (both - whole).abs() <= TOLERANCE * (1.0 + both.abs()) {
            return both;
        }
        self.integrate(lo, mid, left, depth - 1) + self.integrate(mid, hi, right, depth - 1)
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<f64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let q = Quartic {
        a: v,
        node: NODE_SQUARE.sqrt(),
    };
    let whole = q.gauss(-LIMIT, LIMIT);
    println!("{:.10}", q.integrate(-LIMIT, LIMIT, whole, DEPTH));
}
