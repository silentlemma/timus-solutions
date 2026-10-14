use std::io::{self, Read};

// the boolean product of two matrices kept as row bitmasks
fn multiply(x: &[u64], y: &[u64]) -> Vec<u64> {
    x.iter()
        .map(|&row| {
            (0..y.len())
                .filter(|&j| row >> j & 1 == 1)
                .fold(0, |acc, j| acc | y[j])
        })
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u32> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    // only whether an entry is zero matters: all entries are non-negative
    let a: Vec<u64> = (0..n)
        .map(|i| {
            (0..n)
                .filter(|&j| v[1 + i * n + j] != 0)
                .fold(0, |m, j| m | 1 << j)
        })
        .collect();
    let (low, high) = (n * (n - 1), n * (n + 1));
    // A^low by repeated squaring
    let mut cur: Vec<u64> = (0..n).map(|i| 1 << i).collect();
    let mut base = a.clone();
    let mut e = low;
    while e > 0 {
        if e & 1 == 1 {
            cur = multiply(&cur, &base);
        }
        base = multiply(&base, &base);
        e >>= 1;
    }
    let mut seen = vec![0u64; n];
    for _ in low..=high {
        for (s, c) in seen.iter_mut().zip(&cur) {
            *s |= c;
        }
        cur = multiply(&cur, &a);
    }
    let full = (1u64 << n) - 1;
    println!(
        "{}",
        if seen.iter().all(|&s| s == full) {
            "Yes"
        } else {
            "No"
        }
    );
}
