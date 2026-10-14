use std::io::{self, Read};

const FOUR: u64 = 4;
const SEVEN: u64 = 7;
const EIGHT: u64 = 8;
const RESIDUE: u64 = 3; // the primes 4k + 3
const FIRST_ODD: u64 = 3; // the first odd divisor to try
const THREE_SQUARES: u32 = 3;
const FOUR_SQUARES: u32 = 4;

fn is_square(n: u64) -> bool {
    let mut r = (n as f64).sqrt() as u64;
    while r * r > n {
        r -= 1;
    }
    while (r + 1) * (r + 1) <= n {
        r += 1;
    }
    r * r == n
}

/// Fermat: every prime 4k + 3 must appear an even number of times.
fn two_squares(mut n: u64) -> bool {
    while n % 2 == 0 {
        n /= 2;
    }
    let mut d = FIRST_ODD;
    while d * d <= n {
        let mut count = 0;
        while n % d == 0 {
            n /= d;
            count += 1;
        }
        if d % FOUR == RESIDUE && count % 2 == 1 {
            return false;
        }
        d += 2;
    }
    // what is left is 1 or a prime
    n % FOUR != RESIDUE
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let n: u64 = match s.trim().parse() {
        Ok(v) => v,
        Err(_) => return,
    };
    let mut m = n;
    while m % FOUR == 0 {
        m /= FOUR;
    }
    let answer = if is_square(n) {
        1
    } else if two_squares(n) {
        2
    } else if m % EIGHT == SEVEN {
        FOUR_SQUARES // Legendre: exactly the numbers 4^a (8b + 7) need four
    } else {
        THREE_SQUARES
    };
    println!("{}", answer);
}
