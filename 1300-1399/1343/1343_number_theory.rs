use std::io::{self, Read};

const DIGITS: usize = 12;
const BASES: [u64; 6] = [2, 3, 5, 7, 11, 13]; // enough for every number below 3 * 10^12

fn mulmod(a: u64, b: u64, n: u64) -> u64 {
    (a as u128 * b as u128 % n as u128) as u64
}

fn powmod(mut a: u64, mut e: u64, n: u64) -> u64 {
    let mut r = 1;
    a %= n;
    while e > 0 {
        if e & 1 == 1 {
            r = mulmod(r, a, n);
        }
        a = mulmod(a, a, n);
        e >>= 1;
    }
    r
}

// Miller-Rabin with fixed bases, exact for all 12-digit numbers
fn is_prime(n: u64) -> bool {
    if n < 2 {
        return false;
    }
    for &p in &BASES {
        if n % p == 0 {
            return n == p;
        }
    }
    let (mut d, mut s) = (n - 1, 0);
    while d % 2 == 0 {
        d /= 2;
        s += 1;
    }
    BASES.iter().all(|&a| {
        let mut x = powmod(a, d, n);
        let mut witness = x != 1 && x != n - 1;
        for _ in 1..s {
            if !witness {
                break;
            }
            x = mulmod(x, x, n);
            witness = x != n - 1;
        }
        !witness
    })
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let count: usize = words.next().unwrap().parse().unwrap();
    let digits: String = words.collect(); // the digits, together or apart
    let prefix = &digits[..count.min(digits.len())];
    let mut number: u64 = if prefix.is_empty() {
        0
    } else {
        prefix.parse().unwrap()
    };
    for _ in count..DIGITS {
        number *= 10;
    }
    if count < DIGITS {
        while !is_prime(number) {
            number += 1;
        }
    }
    println!("{:0width$}", number, width = DIGITS);
}
