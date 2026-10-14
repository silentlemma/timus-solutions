use std::io::{self, Read};

const SMALL: usize = 8; // pieces up to this size are checked triple by triple
const HALF: f64 = 0.5; // a better triangle has every side shorter than half its perimeter

struct Forest {
    xs: Vec<f64>,
    ys: Vec<f64>,
    order: Vec<usize>,
    best: f64,
    answer: (usize, usize, usize),
}

impl Forest {
    fn dist(&self, a: usize, b: usize) -> f64 {
        (self.xs[a] - self.xs[b]).hypot(self.ys[a] - self.ys[b])
    }

    // tries every triple of pts, sorted by y, that fits within reach vertically
    fn triples(&mut self, pts: &[usize], reach: f64) {
        for i in 0..pts.len() {
            let a = pts[i];
            let mut top = self.ys[a] + reach;
            for j in i + 1..pts.len() {
                let b = pts[j];
                if self.ys[b] >= top {
                    break;
                }
                for &c in &pts[j + 1..] {
                    if self.ys[c] >= top {
                        break;
                    }
                    let p = self.dist(a, b) + self.dist(b, c) + self.dist(c, a);
                    if p < self.best {
                        self.best = p;
                        self.answer = (a, b, c);
                        top = self.ys[a] + p * HALF;
                    }
                }
            }
        }
    }

    fn by_y(&self, pts: &mut [usize]) {
        pts.sort_by(|&a, &b| self.ys[a].partial_cmp(&self.ys[b]).unwrap());
    }

    // solves the points order[lo..hi]
    fn solve(&mut self, lo: usize, hi: usize) {
        if hi - lo <= SMALL {
            let mut pts = self.order[lo..hi].to_vec();
            self.by_y(&mut pts);
            self.triples(&pts, f64::INFINITY);
            return;
        }
        let mid = (lo + hi) / 2;
        let split = self.xs[self.order[mid]];
        self.solve(lo, mid);
        self.solve(mid, hi);
        // a better triangle across the split lies in a strip around it
        let reach = self.best * HALF;
        let mut strip: Vec<usize> = self.order[lo..hi]
            .iter()
            .copied()
            .filter(|&p| (self.xs[p] - split).abs() < reach)
            .collect();
        self.by_y(&mut strip);
        self.triples(&strip, reach);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let xs: Vec<f64> = (0..n).map(|i| v[1 + 2 * i]).collect();
    let ys: Vec<f64> = (0..n).map(|i| v[2 + 2 * i]).collect();
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by(|&a, &b| (xs[a], ys[a]).partial_cmp(&(xs[b], ys[b])).unwrap());
    let mut forest = Forest {
        xs,
        ys,
        order,
        best: f64::INFINITY,
        answer: (0, 1, 2),
    };
    forest.solve(0, n);
    let (a, b, c) = forest.answer;
    println!("{:.6}\n{} {} {}", forest.best, a + 1, b + 1, c + 1);
}
