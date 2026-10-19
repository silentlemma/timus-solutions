use std::fmt::Write;
use std::io::{self, Read};

// non-negative numbers in base 10^9, least significant limb first
const BASE: u64 = 1_000_000_000;

fn multiply(x: &mut Vec<u64>, k: u64) {
    let mut carry = 0;
    for limb in x.iter_mut() {
        let v = *limb * k + carry;
        *limb = v % BASE;
        carry = v / BASE;
    }
    while carry > 0 {
        x.push(carry % BASE);
        carry /= BASE;
    }
}

fn add(x: &mut Vec<u64>, y: &[u64]) {
    if x.len() < y.len() {
        x.resize(y.len(), 0);
    }
    let mut carry = 0;
    for i in 0..x.len() {
        let v = x[i] + y.get(i).copied().unwrap_or(0) + carry;
        x[i] = v % BASE;
        carry = v / BASE;
    }
    if carry > 0 {
        x.push(carry);
    }
}

// x - y for x >= y
fn subtract(x: &mut Vec<u64>, y: &[u64]) {
    let mut borrow = 0;
    for i in 0..x.len() {
        let take = y.get(i).copied().unwrap_or(0) + borrow;
        if x[i] >= take {
            x[i] -= take;
            borrow = 0;
        } else {
            x[i] = x[i] + BASE - take;
            borrow = 1;
        }
    }
    while x.len() > 1 && *x.last().unwrap() == 0 {
        x.pop();
    }
}

fn divide(x: &mut Vec<u64>, k: u64) {
    let mut rest = 0;
    for limb in x.iter_mut().rev() {
        let v = rest * BASE + *limb;
        *limb = v / k;
        rest = v % k;
    }
    while x.len() > 1 && *x.last().unwrap() == 0 {
        x.pop();
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<u64>().unwrap());
    let (a, n) = (it.next().unwrap(), it.next().unwrap());
    let mut primes = Vec::new();
    let mut rest = n;
    let mut p = 2;
    while p * p <= rest {
        if rest % p == 0 {
            primes.push(p);
            while rest % p == 0 {
                rest /= p;
            }
        }
        p += 1;
    }
    if rest > 1 {
        primes.push(rest);
    }
    // keys up to rotation without a shorter period are Lyndon words: by
    // Moebius inversion n times their number is the sum over square-free
    // divisors d of n of mu(d) a^(n / d)
    let (mut plus, mut minus) = (vec![0u64], vec![0u64]);
    for mask in 0..1usize << primes.len() {
        let (mut d, mut negative) = (1, false);
        for (i, &q) in primes.iter().enumerate() {
            if mask >> i & 1 == 1 {
                d *= q;
                negative = !negative;
            }
        }
        let mut term = vec![1u64];
        for _ in 0..n / d {
            multiply(&mut term, a);
        }
        add(if negative { &mut minus } else { &mut plus }, &term);
    }
    subtract(&mut plus, &minus);
    divide(&mut plus, n);
    let mut out = plus.last().unwrap().to_string();
    for limb in plus.iter().rev().skip(1) {
        write!(out, "{:09}", limb).unwrap();
    }
    println!("{}", out);
}
