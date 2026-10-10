use std::io::{self, Read};

// the sum of all divisors of n by trial division
fn divisor_sum(n: i64) -> i64 {
    let mut total = 0;
    let mut d = 1;
    while d * d <= n {
        if n % d == 0 {
            total += if d * d == n { d } else { d + n / d };
        }
        d += 1;
    }
    total
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (lo, hi) = (v[0], v[1]);
    // 1 has no proper divisors at all
    if lo == 1 {
        println!("1");
        return;
    }
    // a prime p has the ratio 1/p, and the largest prime in range beats every
    // composite there (it is above hi / 2 by Bertrand's postulate), so only a
    // range without primes, at most 113 numbers here, needs comparing
    if let Some(p) = (lo..=hi).rev().find(|&n| divisor_sum(n) == n + 1) {
        println!("{}", p);
        return;
    }
    let mut best = lo;
    for n in lo + 1..=hi {
        // sigma(n) / n < sigma(best) / best, the smaller number winning a tie
        if divisor_sum(n) * best < divisor_sum(best) * n {
            best = n;
        }
    }
    println!("{}", best);
}
