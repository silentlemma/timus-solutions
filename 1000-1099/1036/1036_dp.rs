use std::io::{self, Read};

const DIGITS: usize = 10;
const BASE: u64 = 1_000_000_000;

// a non-negative number as base-10^9 limbs, the lowest limb first
type Big = Vec<u64>;

fn add_to(a: &mut Big, b: &Big) {
    if a.len() < b.len() {
        a.resize(b.len(), 0);
    }
    let mut carry = 0;
    for i in 0..a.len() {
        let s = a[i] + carry + b.get(i).copied().unwrap_or(0);
        a[i] = s % BASE;
        carry = s / BASE;
    }
    if carry > 0 {
        a.push(carry);
    }
}

fn multiply(a: &Big, b: &Big) -> Big {
    let mut acc = vec![0u64; a.len() + b.len() + 1];
    for i in 0..a.len() {
        for j in 0..b.len() {
            acc[i + j] += a[i] * b[j];
            acc[i + j + 1] += acc[i + j] / BASE;
            acc[i + j] %= BASE;
        }
    }
    for i in 0..acc.len() - 1 {
        acc[i + 1] += acc[i] / BASE;
        acc[i] %= BASE;
    }
    while acc.len() > 1 && *acc.last().unwrap() == 0 {
        acc.pop();
    }
    acc
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, s) = (it.next().unwrap(), it.next().unwrap());
    let half = s / 2;
    if s % 2 != 0 || half > (DIGITS - 1) * n {
        println!("0");
        return;
    }
    // ways[t]: the number of strings of the digits seen so far with digit sum t
    let mut ways: Vec<Big> = vec![vec![0]; half + 1];
    ways[0] = vec![1];
    for _ in 0..n {
        let mut next: Vec<Big> = vec![vec![0]; half + 1];
        for t in 0..=half {
            for d in 0..DIGITS.min(t + 1) {
                add_to(&mut next[t], &ways[t - d]);
            }
        }
        ways = next;
    }
    // the two halves are chosen independently
    let r = multiply(&ways[half], &ways[half]);
    let mut out = r.last().unwrap().to_string();
    for limb in r.iter().rev().skip(1) {
        out.push_str(&format!("{:09}", limb));
    }
    println!("{}", out);
}
