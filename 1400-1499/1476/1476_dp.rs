use std::io::{self, Read};

/// Non-negative integers as base 10^9 limbs, the lowest first.
type Big = Vec<u32>;
const BASE: u128 = 1_000_000_000;

/// a += b * factor, with factor below 2^64.
fn add_mul(a: &mut Big, b: &Big, factor: u64) {
    if a.len() < b.len() {
        a.resize(b.len(), 0);
    }
    let mut carry: u128 = 0;
    for i in 0..a.len() {
        let v = carry + a[i] as u128 + b.get(i).map_or(0, |&x| x as u128 * factor as u128);
        a[i] = (v % BASE) as u32;
        carry = v / BASE;
    }
    while carry > 0 {
        a.push((carry % BASE) as u32);
        carry /= BASE;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (m, n, k) = (v[0], v[1], v[2]);
    let mut binom = vec![vec![0u64; m + 1]; m + 1];
    for i in 0..=m {
        binom[i][0] = 1;
        for j in 1..=i {
            binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
        }
    }
    // step[c][d]: ways to follow a column with c ones by one with d ones,
    // turning at most k zeros into ones (at most 2^40 of them)
    let mut step = vec![vec![0u64; m + 1]; m + 1];
    for c in 0..=m {
        for t in 0..=k.min(m - c) {
            for s in 0..=c {
                step[c][s + t] += binom[m - c][t] * binom[c][s];
            }
        }
    }
    // ways[c]: fillings of the columns so far whose last column has c ones
    let mut ways: Vec<Big> = (0..=m)
        .map(|c| {
            let mut w = Big::new();
            add_mul(&mut w, &vec![1], binom[m][c]);
            w
        })
        .collect();
    for _ in 1..n {
        let mut next: Vec<Big> = vec![Big::new(); m + 1];
        for c in 0..=m {
            for d in 0..=m {
                if step[c][d] > 0 {
                    add_mul(&mut next[d], &ways[c], step[c][d]);
                }
            }
        }
        ways = next;
    }
    let mut total = Big::new();
    for w in &ways {
        add_mul(&mut total, w, 1);
    }
    while total.len() > 1 && *total.last().unwrap() == 0 {
        total.pop();
    }
    let mut s = total.last().map_or(0, |&x| x).to_string();
    for x in total.iter().rev().skip(1) {
        s.push_str(&format!("{:09}", x));
    }
    println!("{}", s);
}
