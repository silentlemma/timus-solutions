use std::f64::consts::PI;
use std::io::{self, Read};

const EPS: f64 = 1e-9;
const DEPTH: u32 = 50;
const CONE: f64 = 1.0 / 3.0; // a cone holds a third of its cylinder

// the Simpson rule: weights of the ends and the middle of an interval,
// and the factor of its error estimate on halves
const POINTS: usize = 3;
const SIMPSON: [f64; POINTS] = [1.0 / 6.0, 4.0 / 6.0, 1.0 / 6.0];
const RICHARDSON: f64 = 15.0;

struct Pile {
    r: f64,
    d: f64,
    k: f64,
}

impl Pile {
    /// The powder lost in the slice at x, parallel to the slit x = d: the cone
    /// surface k (r - rho) drops to k |x - d| wherever rho < a = r - |x - d|.
    fn lost(&self, x: f64) -> f64 {
        let a = self.r - (x - self.d).abs();
        if a <= x.abs() {
            return 0.0;
        }
        let y = (a * a - x * x).sqrt();
        let tail = if x != 0.0 {
            x * x * ((a + y) / x.abs()).ln()
        } else {
            0.0
        };
        self.k * (a * y - tail)
    }

    fn adaptive(
        &self,
        lo: f64,
        hi: f64,
        f: [f64; POINTS],
        whole: f64,
        eps: f64,
        depth: u32,
    ) -> f64 {
        let mid = (lo + hi) / 2.0;
        let (fl, fr) = (self.lost((lo + mid) / 2.0), self.lost((mid + hi) / 2.0));
        let left = rule(lo, mid, [f[0], fl, f[1]]);
        let right = rule(mid, hi, [f[1], fr, f[2]]);
        let delta = left + right - whole;
        if depth == 0 || delta.abs() <= RICHARDSON * eps {
            return left + right + delta / RICHARDSON;
        }
        self.adaptive(lo, mid, [f[0], fl, f[1]], left, eps / 2.0, depth - 1)
            + self.adaptive(mid, hi, [f[1], fr, f[2]], right, eps / 2.0, depth - 1)
    }

    fn integral(&self, lo: f64, hi: f64) -> f64 {
        if hi <= lo {
            return 0.0;
        }
        let f = [self.lost(lo), self.lost((lo + hi) / 2.0), self.lost(hi)];
        self.adaptive(lo, hi, f, rule(lo, hi, f), EPS, DEPTH)
    }
}

fn rule(lo: f64, hi: f64, f: [f64; POINTS]) -> f64 {
    (hi - lo) * (SIMPSON[0] * f[0] + SIMPSON[1] * f[1] + SIMPSON[2] * f[2])
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (r, d, h) = (v[0], v[1], v[2]);
    let pile = Pile { r, d, k: h / r }; // k is the slope of the powder
    let mut volume = PI * r * r * h * CONE;
    if d < r {
        // the slit cuts the base between (d - r) / 2 and (d + r) / 2, kinks at 0 and d
        volume -= pile.integral((d - r) / 2.0, 0.0)
            + pile.integral(0.0, d)
            + pile.integral(d, (d + r) / 2.0);
    }
    println!("{:.6}", volume);
}
