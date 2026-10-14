use std::io::{self, Read};

/// Non-negative big numbers as base-10^9 digits, lowest first.
const BASE: u64 = 1_000_000_000;

fn mul_small(a: &mut Vec<u64>, s: u64) {
    let mut carry = 0;
    for d in a.iter_mut() {
        let cur = *d * s + carry;
        *d = cur % BASE;
        carry = cur / BASE;
    }
    while carry > 0 {
        a.push(carry % BASE);
        carry /= BASE;
    }
}

/// Exact division by a small number.
fn div_small(a: &mut Vec<u64>, s: u64) {
    let mut rem = 0;
    for d in a.iter_mut().rev() {
        let cur = rem * BASE + *d;
        *d = cur / s;
        rem = cur % s;
    }
    while a.len() > 1 && *a.last().unwrap() == 0 {
        a.pop();
    }
}

fn show(a: &[u64]) -> String {
    let mut s = a.last().unwrap().to_string();
    for d in a.iter().rev().skip(1) {
        s.push_str(&format!("{:09}", d));
    }
    s
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let n: u64 = text.trim().parse().unwrap();
    // The Catalan numbers: every leading square of their Hankel matrix has
    // determinant 1. C(k + 1) = C(k) * 2 (2k + 1) / (k + 2), always exact.
    let mut c = vec![1u64];
    let mut out = String::new();
    for k in 0..2 * n - 1 {
        out.push_str(&show(&c));
        out.push('\n');
        mul_small(&mut c, 2 * (2 * k + 1));
        div_small(&mut c, k + 2);
    }
    print!("{}", out);
}
