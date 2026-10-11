use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u64 = input.trim().parse().unwrap();
    // Euler's totient: the turns 2*pi*m/n with gcd(m, n) = 1
    let (mut phi, mut rest) = (n, n);
    let mut p = 2;
    while p * p <= rest {
        if rest % p == 0 {
            while rest % p == 0 {
                rest /= p;
            }
            phi -= phi / p;
        }
        p += 1;
    }
    if rest > 1 {
        phi -= phi / rest;
    }
    println!("{}", phi / 2);
}
