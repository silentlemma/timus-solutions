use std::io::{self, Read};

// samples per smooth piece and golden-section steps around the best samples
const SAMPLES: usize = 64;
const STEPS: usize = 60;
const EPS: f64 = 1e-12;
// the step of the golden-section search, (sqrt(5) - 1) / 2
const GOLDEN: f64 = 0.618_033_988_749_894_9;

struct Polygon {
    n: usize,
    vx: Vec<f64>,
    vy: Vec<f64>,
    pre: Vec<f64>,
    half: f64,
}

impl Polygon {
    // the point at boundary position u (a vertex index plus a fraction of the edge)
    fn at(&self, u: f64) -> (f64, f64, usize) {
        let i = u as usize;
        let t = u - i as f64;
        (
            self.vx[i] + t * (self.vx[i + 1] - self.vx[i]),
            self.vy[i] + t * (self.vy[i + 1] - self.vy[i]),
            i,
        )
    }

    // the position w in (u, u + n) of the other end of the halving cut from u
    fn partner(&self, u: f64) -> f64 {
        let (px, py, i) = self.at(u);
        // twice the area of P, V[i+1], ..., V[j]
        let fan = |j: usize| {
            px * self.vy[i + 1] - self.vx[i + 1] * py + self.pre[j] - self.pre[i + 1]
                + self.vx[j] * py
                - px * self.vy[j]
        };
        let (mut lo, mut hi) = (i + 1, i + self.n);
        while hi - lo > 1 {
            let mid = (lo + hi) / 2;
            if fan(mid) <= self.half {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        let j = lo;
        // on the edge V[j] -> V[j+1] the area grows linearly with the position
        let (ex, ey) = (self.vx[j + 1] - self.vx[j], self.vy[j + 1] - self.vy[j]);
        let slope = self.vx[j] * ey - ex * self.vy[j] + ex * py - px * ey;
        let s = if slope > 0.0 {
            (self.half - fan(j)) / slope
        } else {
            0.0
        };
        j as f64 + s.max(0.0).min(1.0)
    }

    fn length(&self, u: f64) -> f64 {
        let (px, py, _) = self.at(u);
        let (qx, qy, _) = self.at(self.partner(u));
        (qx - px).hypot(qy - py)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut xs = Vec::new();
    let mut ys = Vec::new();
    for _ in 0..n {
        xs.push(it.next().unwrap().parse::<f64>().unwrap());
        ys.push(it.next().unwrap().parse::<f64>().unwrap());
    }
    // the walk below needs counterclockwise order, whatever order is given
    let twice: f64 = (0..n)
        .map(|i| {
            let j = (i + n - 1) % n;
            xs[j] * ys[i] - xs[i] * ys[j]
        })
        .sum();
    if twice < 0.0 {
        xs.reverse();
        ys.reverse();
    }
    // vertices repeated twice so that a walk along the boundary never wraps
    let vx: Vec<f64> = (0..=2 * n).map(|k| xs[k % n]).collect();
    let vy: Vec<f64> = (0..=2 * n).map(|k| ys[k % n]).collect();
    // pre[k]: twice the signed area swept by the edges 0 .. k-1 from the origin
    let mut pre = vec![0.0];
    for k in 0..2 * n {
        pre.push(pre[k] + vx[k] * vy[k + 1] - vx[k + 1] * vy[k]);
    }
    let half = pre[n] / 2.0;
    let poly = Polygon {
        n,
        vx,
        vy,
        pre,
        half,
    };
    // the cut length is smooth between the vertices and the partners of the
    // vertices; sample every piece and refine around its local minima
    let mut breaks: Vec<f64> = (0..=n).map(|k| k as f64).collect();
    for k in 0..n {
        breaks.push(poly.partner(k as f64) % n as f64);
    }
    breaks.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mut best = poly.length(0.0);
    for b in 0..breaks.len() - 1 {
        let (from, to) = (breaks[b], breaks[b + 1]);
        if to - from < EPS {
            continue;
        }
        let us: Vec<f64> = (0..=SAMPLES)
            .map(|k| from + (to - from) * k as f64 / SAMPLES as f64)
            .collect();
        let vals: Vec<f64> = us.iter().map(|&u| poly.length(u)).collect();
        for &v in &vals {
            best = best.min(v);
        }
        for k in 0..=SAMPLES {
            // a local minimum among the samples, the piece ends included
            let (left, right) = (k.saturating_sub(1), (k + 1).min(SAMPLES));
            if vals[k] > vals[left] || vals[k] > vals[right] {
                continue;
            }
            let (mut lo, mut hi) = (us[left], us[right]);
            for _ in 0..STEPS {
                let (m1, m2) = (hi - GOLDEN * (hi - lo), lo + GOLDEN * (hi - lo));
                if poly.length(m1) < poly.length(m2) {
                    hi = m2;
                } else {
                    lo = m1;
                }
            }
            best = best.min(poly.length((lo + hi) / 2.0));
        }
    }
    println!("{:.6}", best);
}
