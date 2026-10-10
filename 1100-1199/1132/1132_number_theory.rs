use std::fmt::Write as _;
use std::io::{self, Read};

// moduli are below this bound
const LIMIT: usize = 32768;

fn power(mut b: i64, mut e: i64, p: i64) -> i64 {
    let mut r = 1;
    b %= p;
    while e > 0 {
        if e % 2 == 1 {
            r = r * b % p;
        }
        b = b * b % p;
        e /= 2;
    }
    r
}

// Tonelli-Shanks for an odd prime p = q * 2^s + 1, a quadratic residue a and a
// non-residue z
fn sqrt_mod(a: i64, p: i64, z: i64) -> i64 {
    let (mut q, mut s) = (p - 1, 0);
    while q % 2 == 0 {
        q /= 2;
        s += 1;
    }
    let (mut c, mut t, mut r) = (power(z, q, p), power(a, q, p), power(a, (q + 1) / 2, p));
    while t != 1 {
        // the order of t is 2^i with i < s; b fixes the top bits
        let (mut i, mut tt) = (0, t);
        while tt != 1 {
            tt = tt * tt % p;
            i += 1;
        }
        let b = power(c, 1i64 << (s - i - 1), p);
        s = i;
        c = b * b % p;
        t = t * c % p;
        r = r * b % p;
    }
    r
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let k = tok.next().unwrap();
    let mut non_residue = vec![0i64; LIMIT];
    let mut out = String::new();
    for _ in 0..k {
        let (a, p) = (tok.next().unwrap(), tok.next().unwrap());
        let a = a % p;
        if p == 2 {
            out.push_str("1\n");
            continue;
        }
        let half = (p - 1) / 2;
        if power(a, half, p) != 1 {
            out.push_str("No root\n");
            continue;
        }
        if non_residue[p as usize] == 0 {
            let mut z = 2;
            while power(z, half, p) != p - 1 {
                z += 1;
            }
            non_residue[p as usize] = z;
        }
        let r = sqrt_mod(a, p, non_residue[p as usize]);
        writeln!(out, "{} {}", r.min(p - r), r.max(p - r)).unwrap();
    }
    print!("{}", out);
}
