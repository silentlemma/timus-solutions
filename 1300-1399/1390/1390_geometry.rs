use std::fmt::Write as _;
use std::io::{self, Read};

const DIGITS: i64 = 1_000_000_000; // the time is printed with nine digits after the point
const WALL: usize = 4; // numbers that describe a wall
const TREE: usize = 4; // a segment tree over n leaves has under 4 n nodes

fn gcd(a: i64, b: i64) -> i64 {
    let (mut a, mut b) = (a.abs(), b.abs());
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

fn reduced(x: i64, y: i64) -> (i64, i64) {
    let g = gcd(x, y);
    (x / g, y / g)
}

/// Counterclockwise order of directions, starting from the positive x axis.
fn before(a: (i64, i64), b: (i64, i64)) -> bool {
    let ha = a.1 < 0 || (a.1 == 0 && a.0 < 0);
    let hb = b.1 < 0 || (b.1 == 0 && b.0 < 0);
    if ha != hb {
        return hb;
    }
    a.0 * b.1 - a.1 * b.0 > 0
}

/// Walls as lines nx x + ny y = c with c > 0: a shot v hits one at time c / (n . v).
struct Walls {
    leaves: Vec<(i64, i64)>,
    lines: Vec<(i64, i64, i64)>,
    tree: Vec<i64>,
}

impl Walls {
    fn better(&self, w: usize, u: usize, leaf: usize) -> bool {
        let (vx, vy) = self.leaves[leaf];
        let (a, b) = (self.lines[w], self.lines[u]);
        (a.0 * vx + a.1 * vy) * b.2 > (b.0 * vx + b.1 * vy) * a.2
    }

    /// Li Chao insertion: two walls swap places at most once on an arc below pi.
    fn push(&mut self, mut node: usize, mut lo: usize, mut hi: usize, mut w: usize) {
        loop {
            if self.tree[node] < 0 {
                self.tree[node] = w as i64;
                return;
            }
            let mid = (lo + hi) / 2;
            let cur = self.tree[node] as usize;
            if self.better(w, cur, mid) {
                self.tree[node] = w as i64;
                w = cur;
            }
            if lo == hi {
                return;
            }
            let cur = self.tree[node] as usize;
            if self.better(w, cur, lo) {
                node *= 2;
                hi = mid;
            } else if self.better(w, cur, hi) {
                node = 2 * node + 1;
                lo = mid + 1;
            } else {
                return;
            }
        }
    }

    fn insert(&mut self, node: usize, lo: usize, hi: usize, left: i64, right: i64, w: usize) {
        if right < lo as i64 || (hi as i64) < left {
            return;
        }
        if left <= lo as i64 && hi as i64 <= right {
            self.push(node, lo, hi, w);
            return;
        }
        let mid = (lo + hi) / 2;
        self.insert(2 * node, lo, mid, left, right, w);
        self.insert(2 * node + 1, mid + 1, hi, left, right, w);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut events: Vec<Vec<i64>> = Vec::new();
    while let Some(word) = it.next() {
        if word == "end" {
            break;
        }
        let count = if word == "shot" { 2 } else { WALL };
        events.push(
            (0..count)
                .map(|_| it.next().unwrap().parse().unwrap())
                .collect(),
        );
    }
    // the leaves: distinct shot directions by angle
    let mut leaves: Vec<(i64, i64)> = events
        .iter()
        .filter(|e| e.len() == 2)
        .map(|e| reduced(e[0], e[1]))
        .collect();
    leaves.sort_by(|&a, &b| {
        if before(a, b) {
            std::cmp::Ordering::Less
        } else if before(b, a) {
            std::cmp::Ordering::Greater
        } else {
            std::cmp::Ordering::Equal
        }
    });
    leaves.dedup();
    let size = leaves.len().max(1);
    let lower_bound = |leaves: &[(i64, i64)], d| leaves.partition_point(|&l| before(l, d));
    let upper_bound = |leaves: &[(i64, i64)], d| leaves.partition_point(|&l| !before(d, l));
    let mut walls = Walls {
        leaves,
        lines: Vec::new(),
        tree: vec![-1; TREE * size],
    };
    let mut out = String::new();
    for e in &events {
        if e.len() == WALL {
            if walls.leaves.is_empty() {
                continue; // no shots at all
            }
            let (mut x1, mut y1, mut x2, mut y2) = (e[0], e[1], e[2], e[WALL - 1]);
            if x1 * y2 - y1 * x2 < 0 {
                std::mem::swap(&mut x1, &mut x2);
                std::mem::swap(&mut y1, &mut y2);
            }
            let (a, b) = (y2 - y1, x1 - x2);
            walls.lines.push((a, b, a * x1 + b * y1));
            let w = walls.lines.len() - 1;
            // the wall covers the directions from its first end counterclockwise to the second
            let (first, last) = (reduced(x1, y1), reduced(x2, y2));
            let lo = lower_bound(&walls.leaves, first) as i64;
            let hi = upper_bound(&walls.leaves, last) as i64 - 1;
            if before(first, last) {
                walls.insert(1, 0, size - 1, lo, hi, w);
            } else {
                walls.insert(1, 0, size - 1, lo, size as i64 - 1, w);
                walls.insert(1, 0, size - 1, 0, hi, w);
            }
            continue;
        }
        let (vx, vy) = (e[0], e[1]);
        let leaf = lower_bound(&walls.leaves, reduced(vx, vy));
        let (mut node, mut lo, mut hi, mut best) = (1usize, 0usize, size - 1, -1i64);
        loop {
            let cur = walls.tree[node];
            if cur >= 0 && (best < 0 || walls.better(cur as usize, best as usize, leaf)) {
                best = cur;
            }
            if lo == hi {
                break;
            }
            let mid = (lo + hi) / 2;
            if leaf <= mid {
                node *= 2;
                hi = mid;
            } else {
                node = 2 * node + 1;
                lo = mid + 1;
            }
        }
        if best < 0 {
            out.push_str("Infinite\n");
        } else {
            let (a, b, c) = walls.lines[best as usize];
            let den = a * vx + b * vy;
            let q = (2 * c * DIGITS + den) / (2 * den);
            writeln!(out, "{}.{:09}", q / DIGITS, q % DIGITS).unwrap();
        }
    }
    print!("{}", out);
}
