use std::io::{self, Read};

const CAPACITY: i64 = 10000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (k, s) = (v[0], v[1]);
    let mut binom = vec![vec![0i64; s + 1]; s + 1];
    for n in 0..=s {
        binom[n][0] = 1;
        for r in 1..=n {
            binom[n][r] = binom[n - 1][r - 1] + binom[n - 1][r];
        }
    }
    // Moebius function by a sieve: -1 per prime factor, 0 with a square factor
    let mut mu = vec![1i64; s + 1];
    let mut prime = vec![true; s + 1];
    for p in 2..=s {
        if !prime[p] {
            continue;
        }
        for m in (p..=s).step_by(p) {
            prime[m] = m == p;
            mu[m] = -mu[m];
        }
        for m in (p * p..=s).step_by(p * p) {
            mu[m] = 0;
        }
    }
    // inclusion-exclusion: sets of multiples of d count with the sign -mu(d)
    let total: i64 = (2..=s)
        .filter(|&d| s / d >= k)
        .map(|d| -mu[d] * binom[s / d][k])
        .sum();
    println!("{}", total.min(CAPACITY));
}
