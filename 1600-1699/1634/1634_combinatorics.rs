use std::collections::HashMap;
use std::io::{self, Read};

const EPS: f64 = 1e-9; // keeps an exact integer whole; no expectation lies that close below one

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let n: usize = text.trim().parse().unwrap();
    // dp[s][l]: the chance that a random permutation of s elements has only
    // cycles of the lengths seen so far, and that their lcm is l
    let mut dp: Vec<HashMap<u64, f64>> = vec![HashMap::new(); n + 1];
    dp[0].insert(1, 1.0);
    for k in 1..=n {
        let mut next = dp.clone();
        for s in 0..n {
            for (&lcm, &w) in &dp[s] {
                let joined = lcm / gcd(lcm, k as u64) * k as u64;
                let mut weight = w;
                let mut m = 1;
                while s + m * k <= n {
                    weight /= (k * m) as f64; // m cycles of length k: 1 / (k^m m!)
                    *next[s + m * k].entry(joined).or_insert(0.0) += weight;
                    m += 1;
                }
            }
        }
        dp = next;
    }
    let expected: f64 = dp[n].iter().map(|(&lcm, &w)| lcm as f64 * w).sum();
    println!("{}", (expected + EPS) as u64);
}
