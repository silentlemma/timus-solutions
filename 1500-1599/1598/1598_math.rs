use std::collections::HashMap;
use std::io::{self, Read};

fn mulmod(a: u64, b: u64, m: u64) -> u64 {
    (a as u128 * b as u128 % m as u128) as u64
}

fn power(mut b: u64, mut e: u64, m: u64) -> u64 {
    let mut r = 1 % m;
    b %= m;
    while e > 0 {
        if e & 1 == 1 {
            r = mulmod(r, b, m);
        }
        b = mulmod(b, b, m);
        e >>= 1;
    }
    r
}

/// The x in [0, q) with g^x = y modulo p, where g has order q:
/// baby steps g^j for j < m, then giant steps y g^(-m i).
fn discrete_log(g: u64, y: u64, p: u64, q: u64) -> u64 {
    let m = (q as f64).sqrt() as u64 + 1;
    let mut baby = HashMap::with_capacity(2 * m as usize);
    let mut cur = 1;
    for j in 0..m {
        baby.entry(cur).or_insert(j);
        cur = mulmod(cur, g, p);
    }
    let step = power(g, (q - m % q) % q, p); // g^(-m), since g^q = 1
    cur = y % p;
    for i in 0..=m {
        if let Some(&j) = baby.get(&cur) {
            return (i * m + j) % q;
        }
        cur = mulmod(cur, step, p);
    }
    0
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<u64> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (q, p, g, y, h) = match v[..] {
        [_, _, q, p, g, y, h] => (q, p, g, y, h),
        _ => return,
    };
    // the hash is fixed, so the signature needs the secret key x itself
    let x = discrete_log(g, y, p, q);
    let mut k = 0;
    loop {
        k += 1;
        let r = power(g, k, p) % q;
        if r == 0 {
            continue;
        }
        // q is prime, so k^(q-2) is the inverse of k
        let s = mulmod(power(k, q - 2, q), (h + mulmod(x, r, q)) % q, q);
        if s != 0 {
            println!("{} {}", r, s);
            return;
        }
    }
}
