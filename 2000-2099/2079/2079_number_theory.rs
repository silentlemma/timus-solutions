use std::collections::{BTreeSet, HashSet};
use std::io::{self, Read};

const SMALL: i64 = 50; // small primes: walk the whole sequence
const FIVE: i64 = 5;
const QUAD: i64 = 4; // the discriminant of a y^2 + b y + c is b^2 - 4 a c

fn power(mut b: i64, mut e: i64, p: i64) -> i64 {
    let mut r = 1;
    b %= p;
    while e > 0 {
        if e & 1 == 1 {
            r = r * b % p;
        }
        b = b * b % p;
        e >>= 1;
    }
    r
}

// a square root of a modulo the odd prime p (Tonelli-Shanks)
fn sqrt_mod(a: i64, p: i64) -> Option<i64> {
    let a = a % p;
    if a == 0 {
        return Some(0);
    }
    if power(a, (p - 1) / 2, p) != 1 {
        return None;
    }
    let (mut q, mut s) = (p - 1, 0);
    while q % 2 == 0 {
        q /= 2;
        s += 1;
    }
    let mut z = 2;
    while power(z, (p - 1) / 2, p) != p - 1 {
        z += 1;
    }
    let (mut m, mut c) = (s, power(z, q, p));
    let (mut t, mut r) = (power(a, q, p), power(a, (q + 1) / 2, p));
    while t != 1 {
        let (mut i, mut t2) = (0, t);
        while t2 != 1 {
            t2 = t2 * t2 % p;
            i += 1;
        }
        let b = power(c, 1 << (m - i - 1), p);
        m = i;
        c = b * b % p;
        t = t * c % p;
        r = r * b % p;
    }
    Some(r)
}

// (a t + b)(c t + d) with t^2 = t + 1
fn mul(u: (i64, i64), v: (i64, i64), p: i64) -> (i64, i64) {
    let ac = u.0 * v.0 % p;
    let cross = (u.0 * v.1 + u.1 * v.0) % p;
    ((ac + cross) % p, (ac + u.1 * v.1) % p)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_whitespace().map(|t| t.parse().unwrap()).collect();
    let (p, x) = (v[0], v[1]);
    let mut found = BTreeSet::new();
    if p <= SMALL {
        // the pairs (F(k), F(k + 1)) repeat with a period of at most 4p + 4
        let (mut a, mut b) = (0, 1);
        loop {
            if a == x {
                found.insert(b);
            }
            let c = (a + b) % p;
            a = b;
            b = c;
            if (a, b) == (0, 1) {
                break;
            }
        }
    } else {
        // t^k = F(k) t + F(k - 1), and Cassini's identity
        // F(k + 1)^2 - F(k + 1) F(k) - F(k)^2 = (-1)^k limits y = F(k + 1)
        // to the roots of y^2 - x y - x^2 - s = 0, s = 1 or -1
        let mut candidates = HashSet::new();
        let half = (p + 1) / 2;
        for s in [1, -1] {
            if let Some(root) = sqrt_mod(((x * x + QUAD * (x * x + s)) % p + p) % p, p) {
                candidates.insert((x + root) % p * half % p);
                candidates.insert((x - root + p) % p * half % p);
            }
        }
        // a pair is a power of t when the discrete logarithm exists: baby steps
        // t^j, giant steps by t^-m; the period divides p - 1 or 2 (p + 1)
        let bound = if p % FIVE == 1 || p % FIVE == FIVE - 1 { p - 1 } else { 2 * (p + 1) };
        let m = (bound as f64).sqrt() as i64 + 1;
        let mut baby = HashSet::new();
        let mut e = (0, 1);
        for _ in 0..m {
            baby.insert(e);
            e = mul(e, (1, 0), p);
        }
        let (mut back, mut inverse, mut k) = ((0, 1), (1, p - 1), m); // t^-m = (t - 1)^m
        while k > 0 {
            if k & 1 == 1 {
                back = mul(back, inverse, p);
            }
            inverse = mul(inverse, inverse, p);
            k >>= 1;
        }
        for &y in &candidates {
            let mut e = (x, (y - x + p) % p);
            for _ in 0..=m {
                if baby.contains(&e) {
                    found.insert(y);
                    break;
                }
                e = mul(e, back, p);
            }
        }
    }
    println!("{}", found.len());
    if !found.is_empty() {
        let values: Vec<String> = found.iter().map(|y| y.to_string()).collect();
        println!("{}", values.join(" "));
    }
}
