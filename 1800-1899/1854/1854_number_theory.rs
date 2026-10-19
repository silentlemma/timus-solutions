use std::io::{self, Read};

const FIRST_ODD_PRIME: u64 = 3; // n is odd

// the integer square root, corrected after the floating-point guess
fn isqrt(n: u64) -> u64 {
    let mut r = (n as f64).sqrt() as u64;
    while r * r > n {
        r -= 1;
    }
    while (r + 1) * (r + 1) <= n {
        r += 1;
    }
    r
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut n: u64 = input.trim().parse().unwrap();
    // the gods number a square divisor of n: a number has an odd count of
    // divisors exactly when it is a square
    let mut best = 1u64;
    let mut p = FIRST_ODD_PRIME;
    while p * p * p <= n {
        let mut power = 0;
        while n % p == 0 {
            n /= p;
            power += 1;
        }
        for _ in 0..power / 2 {
            best *= p * p;
        }
        p += 2;
    }
    // what is left has no prime factor up to its cube root, so at most two
    // prime factors: it is a square only as the square of one prime
    let r = isqrt(n);
    if r * r == n {
        best *= n;
    }
    println!("{}", best);
}
