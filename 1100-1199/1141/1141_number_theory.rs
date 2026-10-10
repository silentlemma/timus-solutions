use std::fmt::Write as _;
use std::io::{self, Read};

// n is a product of two odd primes, so trial division starts here
const SMALLEST: i64 = 3;

fn power(mut b: i64, mut e: i64, n: i64) -> i64 {
    let mut r = 1;
    b %= n;
    while e > 0 {
        if e % 2 == 1 {
            r = r * b % n;
        }
        b = b * b % n;
        e /= 2;
    }
    r
}

// the inverse of e modulo phi by the extended Euclidean algorithm
fn inverse(e: i64, phi: i64) -> i64 {
    let (mut a, mut b, mut x, mut y) = (e % phi, phi, 1i64, 0i64);
    while b != 0 {
        let q = a / b;
        (a, b) = (b, a - q * b);
        (x, y) = (y, x - q * y);
    }
    (x % phi + phi) % phi
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let k = tok.next().unwrap();
    let mut out = String::new();
    for _ in 0..k {
        let (e, n, c) = (
            tok.next().unwrap(),
            tok.next().unwrap(),
            tok.next().unwrap(),
        );
        let mut p = SMALLEST;
        while n % p != 0 {
            p += 2;
        }
        let phi = (p - 1) * (n / p - 1);
        // m^(e d) = m modulo n when e d = 1 modulo phi, so the private
        // exponent d undoes the public one
        writeln!(out, "{}", power(c, inverse(e, phi), n)).unwrap();
    }
    print!("{}", out);
}
