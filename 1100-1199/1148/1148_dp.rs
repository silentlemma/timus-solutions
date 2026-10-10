use std::fmt::Write as _;
use std::io::{self, Read};

// counts are kept only for every STRIDE-th height, so that the table fits in
// the memory limit; the heights between are recomputed by recursion
const STRIDE: usize = 4;

struct Towers {
    offset: Vec<Vec<Option<usize>>>,
    memo: Vec<i64>,
}

// a tower with h levels whose lowest has m bricks uses at most this many
fn most(h: i64, m: i64) -> i64 {
    m * h + h * (h - 1) / 2
}

impl Towers {
    // towers of h levels starting with m bricks that use at most n bricks
    fn count(&mut self, n: i64, h: usize, m: i64) -> i64 {
        if m == 0 || n < m {
            return 0;
        }
        if h == 1 {
            return 1;
        }
        let n = n.min(most(h as i64, m));
        let key = self
            .offset
            .get(h)
            .and_then(|row| row.get(m as usize))
            .copied()
            .flatten()
            .map(|k| k + n as usize);
        if let Some(k) = key {
            if self.memo[k] >= 0 {
                return self.memo[k];
            }
        }
        let ways = self.count(n - m, h - 1, m - 1) + self.count(n - m, h - 1, m + 1);
        if let Some(k) = key {
            self.memo[k] = ways;
        }
        ways
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let total = tok.next().unwrap();
    let height = tok.next().unwrap() as usize;
    let base = tok.next().unwrap();
    // offset[h][m] starts the stored counts for h levels and m bricks below,
    // kept only for the widths that a tower can reach at that height
    let mut offset = vec![vec![None; base as usize + height + 2]; height + 1];
    let mut size = 0;
    for h in (STRIDE..=height).step_by(STRIDE) {
        let depth = (height - h) as i64;
        let mut low = base - depth;
        while low < 1 {
            low += 2;
        }
        for m in (low..=base + depth).step_by(2) {
            offset[h][m as usize] = Some(size);
            size += most(h as i64, m) as usize + 1;
        }
    }
    let mut towers = Towers {
        offset,
        memo: vec![-1; size],
    };
    let mut out = format!("{}\n", towers.count(total, height, base));
    for mut k in tok {
        if k < 0 {
            break;
        }
        // lexicographic order: the narrower next level comes first
        let (mut n, mut m) = (total, base);
        write!(out, "{}", m).unwrap();
        for h in (2..=height).rev() {
            let fewer = towers.count(n - m, h - 1, m - 1);
            n -= m;
            if k <= fewer {
                m -= 1;
            } else {
                k -= fewer;
                m += 1;
            }
            write!(out, " {}", m).unwrap();
        }
        out.push('\n');
    }
    print!("{}", out);
}
