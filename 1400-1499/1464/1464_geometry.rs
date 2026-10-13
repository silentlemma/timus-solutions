use std::io::{self, Read};

const DIGITS: usize = 4; // coordinates are given to four decimals
const SCALE: i64 = 10_000;

/// A coordinate times 10^4, read exactly.
fn exact(text: &str) -> i64 {
    let (sign, text) = match text.strip_prefix('-') {
        Some(rest) => (-1, rest),
        None => (1, text),
    };
    let (whole, frac) = text.split_once('.').unwrap_or((text, ""));
    let padded = format!("{:0<width$}", frac, width = DIGITS);
    let w: i64 = if whole.is_empty() {
        0
    } else {
        whole.parse().unwrap()
    };
    let f: i64 = padded[..DIGITS].parse().unwrap();
    sign * (w * SCALE + f)
}

struct Tree {
    num: Vec<f64>,
    ex: Vec<f64>,
    ey: Vec<f64>,
    mid: Vec<(f64, f64)>,
    first: Vec<usize>,
    best: Vec<usize>,
    size: usize,
}

const NONE: usize = usize::MAX;

impl Tree {
    /// How far along the middle ray of gap k the line of edge e lies.
    fn distance(&self, e: usize, k: usize) -> f64 {
        let (u, v) = self.mid[k];
        self.num[e] / (u * self.ey[e] - v * self.ex[e])
    }

    /// Each node keeps the nearest edge among those covering all its gaps,
    /// and edges never cross, so one gap decides for the whole node.
    fn offer(&mut self, x: usize, e: usize) {
        let k = self.first[x];
        if self.best[x] == NONE || self.distance(e, k) < self.distance(self.best[x], k) {
            self.best[x] = e;
        }
    }

    fn cover(&mut self, lo: usize, hi: usize, e: usize) {
        let (mut lo, mut hi) = (lo + self.size, hi + self.size);
        while lo < hi {
            if lo & 1 == 1 {
                self.offer(lo, e);
                lo += 1;
            }
            if hi & 1 == 1 {
                hi -= 1;
                self.offer(hi, e);
            }
            lo >>= 1;
            hi >>= 1;
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();
    let px = exact(it.next().unwrap());
    let py = exact(it.next().unwrap());
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut xs = vec![0i64; n];
    let mut ys = vec![0i64; n];
    for i in 0..n {
        xs[i] = exact(it.next().unwrap()) - px;
        ys[i] = exact(it.next().unwrap()) - py;
    }
    // the directions of the corners seen from the lamp, equal ones merged
    let angle: Vec<f64> = (0..n).map(|i| (ys[i] as f64).atan2(xs[i] as f64)).collect();
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by(|&a, &b| angle[a].partial_cmp(&angle[b]).unwrap());
    let mut group = vec![0usize; n];
    let (mut dx, mut dy): (Vec<i64>, Vec<i64>) = (Vec::new(), Vec::new());
    for &i in &order {
        let same = match (dx.last(), dy.last()) {
            (Some(&a), Some(&b)) => xs[i] * b == ys[i] * a && xs[i] * a + ys[i] * b > 0,
            _ => false,
        };
        if !same {
            dx.push(xs[i]);
            dy.push(ys[i]);
        }
        group[i] = dx.len() - 1;
    }
    let m = dx.len();
    // every gap between neighbouring directions is below half a turn; its middle
    let mid: Vec<(f64, f64)> = (0..m)
        .map(|k| {
            let l = (k + 1) % m;
            let la = (dx[k] as f64).hypot(dy[k] as f64);
            let lb = (dx[l] as f64).hypot(dy[l] as f64);
            (
                dx[k] as f64 / la + dx[l] as f64 / lb,
                dy[k] as f64 / la + dy[l] as f64 / lb,
            )
        })
        .collect();
    let size = m.next_power_of_two();
    let mut first = vec![0usize; 2 * size];
    for x in (1..2 * size).rev() {
        first[x] = if x >= size { x - size } else { first[2 * x] };
    }
    let mut tree = Tree {
        num: Vec::new(),
        ex: Vec::new(),
        ey: Vec::new(),
        mid,
        first,
        best: vec![NONE; 2 * size],
        size,
    };
    for i in 0..n {
        let j = (i + 1) % n;
        let c = xs[i] * ys[j] - ys[i] * xs[j];
        if c == 0 {
            continue; // seen edge-on, it hides nothing
        }
        let (a, b) = if c > 0 { (i, j) } else { (j, i) };
        let e = tree.num.len();
        tree.num
            .push((xs[a] * (ys[b] - ys[a]) - ys[a] * (xs[b] - xs[a])) as f64);
        tree.ex.push((xs[b] - xs[a]) as f64);
        tree.ey.push((ys[b] - ys[a]) as f64);
        if group[a] < group[b] {
            tree.cover(group[a], group[b], e);
        } else {
            tree.cover(group[a], m, e);
            tree.cover(0, group[b], e);
        }
    }
    let mut area = 0.0;
    for k in 0..m {
        let mut near = NONE;
        let mut x = k + size;
        while x > 0 {
            let b = tree.best[x];
            if b != NONE && (near == NONE || tree.distance(b, k) < tree.distance(near, k)) {
                near = b;
            }
            x >>= 1;
        }
        let l = (k + 1) % m;
        let (ax, ay, bx, by) = (dx[k] as f64, dy[k] as f64, dx[l] as f64, dy[l] as f64);
        let ta = tree.num[near] / (ax * tree.ey[near] - ay * tree.ex[near]);
        let tb = tree.num[near] / (bx * tree.ey[near] - by * tree.ex[near]);
        area += ta * tb * (ax * by - ay * bx) / 2.0;
    }
    let scale = SCALE as f64;
    println!("{:.4}", area / scale / scale);
}
