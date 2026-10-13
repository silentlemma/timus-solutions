use std::io::{self, Read};

const BASE: u64 = 1_000_000_000_000_000_000; // a long number in limbs of 18 digits

/// The sum a + b on limbs from the lowest.
fn add(a: &[u64], b: &[u64]) -> Vec<u64> {
    let mut sum = Vec::with_capacity(a.len().max(b.len()) + 1);
    let mut carry = 0;
    let mut i = 0;
    while i < a.len() || i < b.len() || carry > 0 {
        let v = carry + a.get(i).copied().unwrap_or(0) + b.get(i).copied().unwrap_or(0);
        sum.push(v % BASE);
        carry = v / BASE;
        i += 1;
    }
    sum
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // numbers of length k without two zeros in a row: Fibonacci F(k + 2), so
    // F(2N) bars go into F(N) safes, and F(2N) = F(N) L(N) with Lucas L(N)
    let (mut a, mut b) = (vec![2u64], vec![1u64]); // L(0), L(1)
    for _ in 0..n {
        let c = add(&a, &b);
        a = b;
        b = c;
    }
    let mut text = a.last().unwrap().to_string();
    for limb in a.iter().rev().skip(1) {
        text.push_str(&format!("{:018}", limb));
    }
    println!("{}", text);
}
