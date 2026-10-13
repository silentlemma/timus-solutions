use std::io::{self, Read, Write};

// these bases make Miller-Rabin exact for every n below 3.2 * 10^9
const BASES: [u64; 4] = [2, 3, 5, 7];
const SMALLEST_SPLIT: u64 = 4; // the smallest even number that is a sum of two primes

fn power(mut b: u64, mut e: u64, m: u64) -> u64 {
    let mut r = 1;
    b %= m;
    while e > 0 {
        if e & 1 == 1 {
            r = r * b % m;
        }
        b = b * b % m;
        e >>= 1;
    }
    r
}

fn is_prime(n: u64) -> bool {
    if n < 2 {
        return false;
    }
    for &b in BASES.iter() {
        if n % b == 0 {
            return n == b;
        }
    }
    let (mut d, mut s) = (n - 1, 0);
    while d % 2 == 0 {
        d /= 2;
        s += 1;
    }
    'bases: for &b in BASES.iter() {
        let mut x = power(b, d, n);
        if x == 1 || x == n - 1 {
            continue;
        }
        for _ in 1..s {
            x = x * x % n;
            if x == n - 1 {
                continue 'bases;
            }
        }
        return false;
    }
    true
}

/// An even n >= 4 as the smallest prime p and n - p.
fn two_primes(n: u64) -> Vec<u64> {
    let mut p = 2;
    while !(is_prime(p) && is_prime(n - p)) {
        p += 1;
    }
    vec![p, n - p]
}

fn split(n: u64) -> Vec<u64> {
    if is_prime(n) {
        return vec![n];
    }
    if n % 2 == 0 {
        return two_primes(n);
    }
    if is_prime(n - 2) {
        return vec![2, n - 2];
    }
    // the largest prime p that leaves an even rest of at least 4
    let mut p = n - SMALLEST_SPLIT;
    while !is_prime(p) {
        p -= 2;
    }
    let mut parts = vec![p];
    parts.extend(two_primes(n - p));
    parts
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<u64>().unwrap());
    let t = it.next().unwrap_or(0);
    let mut out = String::new();
    for n in it.take(t as usize) {
        let parts: Vec<String> = split(n).iter().map(|p| p.to_string()).collect();
        out.push_str(&parts.join(" "));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
