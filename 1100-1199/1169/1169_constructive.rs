use std::io;

const SMALLEST_CYCLE: usize = 3;

fn pairs(s: usize) -> usize {
    s * (s.max(1) - 1) / 2
}

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let v: Vec<i64> = line
        .split_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    // a pair is not critical exactly when both computers lie in the same
    // 2-edge-connected part; such a part has one computer or at least three,
    // so the sizes must split n with pairs(size) adding up to pairs(n) - k
    let target = pairs(n) as i64 - v[1];
    let sizes: Vec<usize> = std::iter::once(1).chain(SMALLEST_CYCLE..=n).collect();
    // reach[m][t] tells whether m computers can be split with t inner pairs
    let mut reach = vec![vec![false; pairs(n) + 1]; n + 1];
    reach[0][0] = true;
    for m in 1..=n {
        for &s in sizes.iter().filter(|&&s| s <= m) {
            for t in pairs(s)..=pairs(n) {
                if reach[m - s][t - pairs(s)] {
                    reach[m][t] = true;
                }
            }
        }
    }
    if target < 0 || !reach[n][target as usize] {
        println!("-1");
        return;
    }
    let mut parts = Vec::new();
    let (mut m, mut t) = (n, target as usize);
    while m > 0 {
        let s = *sizes
            .iter()
            .find(|&&s| s <= m && pairs(s) <= t && reach[m - s][t - pairs(s)])
            .unwrap();
        parts.push(s);
        m -= s;
        t -= pairs(s);
    }
    // each part is a cycle (or a single computer), and bridges join the first
    // computers of consecutive parts
    let mut out = String::new();
    let (mut first, mut prev) = (1, 0);
    for s in parts {
        if s > 1 {
            for j in 0..s {
                out += &format!("{} {}\n", first + j, first + (j + 1) % s);
            }
        }
        if prev > 0 {
            out += &format!("{} {}\n", prev, first);
        }
        prev = first;
        first += s;
    }
    print!("{}", out);
}
