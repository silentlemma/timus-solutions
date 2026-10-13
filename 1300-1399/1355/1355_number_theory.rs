use std::io::{self, Read, Write};

/// How many primes multiply to n, counted with repetition.
fn prime_factors(mut n: u64) -> u32 {
    let mut count = 0;
    let mut d = 2;
    while d * d <= n {
        while n % d == 0 {
            n /= d;
            count += 1;
        }
        d += 1;
    }
    if n > 1 {
        count += 1;
    }
    count
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<u64>().unwrap());
    let t = it.next().unwrap_or(0);
    let mut out = String::new();
    for _ in 0..t {
        let (a, b) = (it.next().unwrap(), it.next().unwrap());
        // every step multiplies the number by at least one prime
        let answer = if b % a == 0 {
            1 + prime_factors(b / a)
        } else {
            0
        };
        out.push_str(&answer.to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
