use std::fmt::Write as _;
use std::io::{self, Read};

const LIMIT: usize = 1 << 16; // N < 65536

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

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    // smallest prime factor of every number below the limit
    let mut spf: Vec<usize> = (0..LIMIT).collect();
    let mut i = 2;
    while i * i < LIMIT {
        if spf[i] == i {
            for j in (i * i..LIMIT).step_by(i) {
                if spf[j] == j {
                    spf[j] = i;
                }
            }
        }
        i += 1;
    }
    let mut known = vec![0usize; LIMIT];
    let t = it.next().unwrap();
    let mut out = String::new();
    for p in it.take(t) {
        if known[p] == 0 {
            // g is a primitive root when no g^((p-1)/q) is 1 for a prime q | p-1
            let mut quotients = Vec::new();
            let mut rest = p - 1;
            while rest > 1 {
                let q = spf[rest];
                quotients.push((p - 1) / q);
                while rest % q == 0 {
                    rest /= q;
                }
            }
            let mut g = p - 1;
            while quotients
                .iter()
                .any(|&e| power(g as u64, e as u64, p as u64) == 1)
            {
                g -= 1;
            }
            known[p] = g;
        }
        writeln!(out, "{}", known[p]).unwrap();
    }
    print!("{}", out);
}
