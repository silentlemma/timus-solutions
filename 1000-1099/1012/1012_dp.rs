use std::fmt::Write as _;
use std::io::{self, Read};

// Big numbers: base 10^9 digits, least significant first.
const BASE: u64 = 1_000_000_000;
const DIGITS_PER_LIMB: usize = 9;

fn add(a: &[u64], b: &[u64]) -> Vec<u64> {
    let mut r = Vec::with_capacity(a.len().max(b.len()) + 1);
    let mut carry = 0;
    for i in 0..a.len().max(b.len()) {
        let s = carry + a.get(i).unwrap_or(&0) + b.get(i).unwrap_or(&0);
        r.push(s % BASE);
        carry = s / BASE;
    }
    if carry > 0 {
        r.push(carry);
    }
    r
}

fn multiply(a: &[u64], m: u64) -> Vec<u64> {
    let mut r = Vec::with_capacity(a.len() + 1);
    let mut carry = 0;
    for &x in a {
        let s = carry + x * m;
        r.push(s % BASE);
        carry = s / BASE;
    }
    if carry > 0 {
        r.push(carry);
    }
    r
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (v[0], v[1]);
    // numbers of valid prefixes ending with a zero and with another digit,
    // where the first digit is not zero
    let (mut zero, mut other) = (vec![0], vec![k - 1]);
    for _ in 1..n {
        let next = multiply(&add(&zero, &other), k - 1);
        zero = std::mem::replace(&mut other, next);
    }
    let answer = add(&zero, &other);
    let mut out = answer.last().unwrap().to_string();
    for limb in answer.iter().rev().skip(1) {
        write!(out, "{:0width$}", limb, width = DIGITS_PER_LIMB).unwrap();
    }
    println!("{}", out);
}
