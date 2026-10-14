use std::io::{self, Read};

const FASTEST: i64 = 100000; // no speed above this
const MOST: usize = 19; // K < 20 leagues
const SLACK: f64 = 1e-9; // floating point margin for the pruning bound
const BIG: i64 = 1 << 61;

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

struct Search {
    harmonic: Vec<f64>,
    path: Vec<i64>,
}

impl Search {
    /// The largest sum of count unit fractions with denominators from start.
    fn most(&self, start: i64, count: usize) -> f64 {
        let end = (start + count as i64 - 1).min(FASTEST);
        if start <= end {
            self.harmonic[end as usize] - self.harmonic[start as usize - 1]
        } else {
            0.0
        }
    }

    /// Writes p / q as left or fewer unit fractions above 1 / last.
    fn run(&mut self, p: i64, q: i64, last: i64, left: usize) -> bool {
        if p == 0 {
            return true;
        }
        if left == 0 {
            return false;
        }
        // 1 / d must fit into p / q, and left fractions of 1 / d must reach it
        let start = (last + 1).max((q + p - 1) / p);
        let stop = if q > BIG / left as i64 {
            FASTEST
        } else {
            FASTEST.min(left as i64 * q / p)
        };
        if start > stop || self.most(start, left) + SLACK < p as f64 / q as f64 {
            return false;
        }
        for d in start..=stop {
            if p as f64 / q as f64 - 1.0 / d as f64 > self.most(d + 1, left - 1) + SLACK {
                continue;
            }
            // keep every fraction within 64 bits
            if q > BIG / d || p > BIG / d {
                continue;
            }
            let (np, nq) = (p * d - q, q * d);
            let g = gcd(np, nq);
            self.path.push(d);
            if self.run(np / g, nq / g, d, left - 1) {
                return true;
            }
            self.path.pop();
        }
        false
    }
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<i64> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (m, n) = (v[0], v[1]);
    // M / N hours over legs of one league each: M / N = 1 / V1 + ... + 1 / VK
    // with distinct whole speeds, a sum of distinct unit fractions
    let mut harmonic = vec![0.0; FASTEST as usize + 2];
    for d in 1..=FASTEST as usize {
        harmonic[d] = harmonic[d - 1] + 1.0 / d as f64;
    }
    let mut search = Search {
        harmonic,
        path: Vec::new(),
    };
    // the fewest fractions first keeps the search small
    for k in 1..=MOST {
        if search.run(m, n, 0, k) {
            let speeds: Vec<String> = search.path.iter().rev().map(|d| d.to_string()).collect();
            println!("{}\n{}", speeds.len(), speeds.join(" "));
            return;
        }
    }
    println!("-1");
}
