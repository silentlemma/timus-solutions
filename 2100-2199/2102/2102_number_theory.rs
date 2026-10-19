use std::io::{self, Read};

const TARGET: i32 = 20;
const BOUND: u64 = 2_000_000; // trial divisors; beyond them at most two primes remain

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut n: u64 = input.trim().parse().unwrap();
    let mut count = 0;
    let mut d = 2;
    while d <= BOUND && d * d <= n {
        while n % d == 0 {
            n /= d;
            count += 1;
        }
        d += 1;
    }
    if n > 1 {
        if d * d > n {
            count += 1; // what is left is prime
        } else {
            // n >= BOUND^2 here, so the divided part is at most 10^18 / BOUND^2,
            // fewer than 18 factors, and the rest adds at most two
            count = -1;
        }
    }
    println!("{}", if count == TARGET { "Yes" } else { "No" });
}
