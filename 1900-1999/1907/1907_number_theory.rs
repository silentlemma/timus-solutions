use std::io::{self, Read};

const FIRST_ODD_PRIME: i64 = 3;

fn coprime_count(bound: i64, index: usize, primes: &[i64], odd_only: bool) -> i64 {
    if bound == 0 {
        return 0;
    }
    if index == primes.len() {
        return if odd_only { (bound + 1) / 2 } else { bound };
    }
    coprime_count(bound, index + 1, primes, odd_only)
        - coprime_count(bound / primes[index], index + 1, primes, odd_only)
}

fn count_sizes(first: i64, limit: i64) -> i64 {
    let mut odd_part = first;
    while odd_part % 2 == 0 {
        odd_part /= 2;
    }
    let mut primes = Vec::new();
    let mut divisor = FIRST_ODD_PRIME;
    while divisor * divisor <= odd_part {
        if odd_part % divisor == 0 {
            primes.push(divisor);
            while odd_part % divisor == 0 {
                odd_part /= divisor;
            }
        }
        divisor += 2;
    }
    if odd_part > 1 {
        primes.push(odd_part);
    }
    let odd_only = first % 2 == 0;
    let bound = if odd_only { limit } else { limit / 2 };
    limit - coprime_count(bound, 0, &primes, odd_only)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_whitespace()
        .map(|token| token.parse::<i64>().unwrap());
    let first = tokens.next().unwrap();
    let limit = tokens.next().unwrap();
    println!("{}", count_sizes(first, limit));
}
