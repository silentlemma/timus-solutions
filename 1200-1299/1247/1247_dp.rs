use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (s, n) = (v[0] as usize, v[1]);
    // the sum of A_i - 1 over every segment must stay at most N, so only the
    // largest such sum matters: Kadane's scan keeps the best one ending here
    let (mut best, mut here) = (0, 0);
    for &a in &v[2..2 + s] {
        here = here.max(0) + a - 1;
        best = best.max(here);
    }
    println!("{}", if best <= n { "YES" } else { "NO" });
}
