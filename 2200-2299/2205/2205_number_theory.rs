use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const FIRST_ODD_PRIME: usize = 3;

fn smallest_factors(limit: usize) -> Vec<u16> {
    let mut factors = vec![0; (limit + 1) / 2];
    let mut prime = FIRST_ODD_PRIME;
    while prime <= limit / prime {
        if factors[prime / 2] == 0 {
            for value in (prime * prime..=limit).step_by(2 * prime) {
                if factors[value / 2] == 0 {
                    factors[value / 2] = prime as u16;
                }
            }
        }
        prime += 2;
    }
    factors
}

fn largest_factor(mut value: usize, factors: &[u16]) -> usize {
    if value % 2 == 0 {
        value >>= value.trailing_zeros();
        if value == 1 {
            return 2;
        }
    }
    while factors[value / 2] != 0 {
        value /= factors[value / 2] as usize;
    }
    value
}

fn gcd(mut a: usize, mut b: usize) -> usize {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let queries: Vec<usize> = tokens.map(|token| token.parse().unwrap()).collect();
    let factors = smallest_factors(*queries.iter().max().unwrap());
    let mut output = String::new();
    for pair in queries.chunks_exact(2).take(count) {
        let (a, b) = (pair[0], pair[1]);
        let mut common = gcd(a, b);
        if common != 1 && a != b {
            // Shared factors survive exactly when they are at least this threshold.
            let threshold =
                largest_factor(a / common, &factors).max(largest_factor(b / common, &factors));
            if threshold > 2 {
                common >>= common.trailing_zeros();
            }
            while common > 1 {
                let mut prime = if common % 2 == 0 {
                    2
                } else {
                    factors[common / 2] as usize
                };
                if prime == 0 {
                    prime = common;
                }
                if prime >= threshold {
                    break;
                }
                common /= prime;
            }
        }
        writeln!(output, "{common}").unwrap();
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}
