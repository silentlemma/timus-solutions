use std::io::{self, Read};

const NONE: i64 = 1_000_000_000;

struct Layer<'a> {
    black: &'a [i64],
    prev: &'a [i64],
    cur: Vec<i64>,
}

impl Layer<'_> {
    // horses j..i-1 in one stable: black times white
    fn cost(&self, j: usize, i: usize) -> i64 {
        let b = self.black[i] - self.black[j];
        b * ((i - j) as i64 - b)
    }

    // fills cur[lo..=hi] knowing that their best last splits lie in
    // [opt_lo, opt_hi]
    fn solve(&mut self, lo: usize, hi: usize, opt_lo: usize, opt_hi: usize) {
        if lo > hi {
            return;
        }
        let mid = (lo + hi) / 2;
        let (mut best, mut arg) = (i64::MAX, opt_lo);
        for j in opt_lo..=opt_hi.min(mid - 1) {
            let v = self.prev[j] + self.cost(j, mid);
            if v < best {
                best = v;
                arg = j;
            }
        }
        self.cur[mid] = best;
        if mid > lo {
            self.solve(lo, mid - 1, opt_lo, arg);
        }
        self.solve(mid + 1, hi, arg, opt_hi);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (v[0], v[1]);
    let mut black = vec![0i64; n + 1];
    for i in 0..n {
        black[i + 1] = black[i] + v[2 + i] as i64;
    }
    // prev[j]: the least unhappiness of the first j horses in the stables so
    // far; with no stables only j = 0 is possible
    let mut prev = vec![NONE; n + 1];
    prev[0] = 0;
    for stables in 1..=k {
        // the best last split never moves left as i grows (the black-white
        // cost satisfies the quadrangle inequality)
        let mut layer = Layer {
            black: &black,
            prev: &prev,
            cur: vec![0; n + 1],
        };
        layer.solve(stables, n, stables - 1, n - 1);
        prev = layer.cur;
    }
    println!("{}", prev[n]);
}
