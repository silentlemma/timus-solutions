use std::io::{self, Read};

fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn primes_of(mut n: u64) -> Vec<u64> {
    let mut found = Vec::new();
    let mut p = 2;
    while p * p <= n {
        if n % p == 0 {
            found.push(p);
            while n % p == 0 {
                n /= p;
            }
        }
        p += 1;
    }
    if n > 1 {
        found.push(n);
    }
    found
}

fn power(mut base: u64, mut exp: u64, modulus: u64) -> u64 {
    let mut result = 1;
    base %= modulus;
    while exp > 0 {
        if exp & 1 == 1 {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exp >>= 1;
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (a, n) = (v[0], v[1]);
    if gcd(a, n) != 1 {
        // the remainders keep a common factor with N and never reach 1
        println!("0");
        return;
    }
    // the order divides phi(N): strip prime factors while a power stays 1
    let mut phi = n;
    for p in primes_of(n) {
        phi = phi / p * (p - 1);
    }
    let mut order = phi;
    for p in primes_of(phi) {
        while order % p == 0 && power(a, order / p, n) == 1 {
            order /= p;
        }
    }
    println!("{}", order);
}
