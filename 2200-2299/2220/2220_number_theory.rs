use std::io::{self, Read};

const MOD: i64 = 1_000_000_007;
const SIEVE_LIMIT: usize = 100_000;

fn power(mut base: i64, mut exponent: i64) -> i64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent % 2 == 1 {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exponent /= 2;
    }
    result
}

struct Totients {
    n: usize,
    limit: usize,
    small: Vec<i64>,
    large: Vec<i64>,
}

impl Totients {
    fn new(n: usize) -> Self {
        let limit = n.min(SIEVE_LIMIT);
        let small = (0..=limit).map(|i| i as i64).collect();
        let count = n / (limit + 1);
        let mut result = Self {
            n,
            limit,
            small,
            large: vec![0; count + 1],
        };
        for prime in 2..=limit {
            if result.small[prime] == prime as i64 {
                for multiple in (prime..=limit).step_by(prime) {
                    result.small[multiple] -= result.small[multiple] / prime as i64;
                }
            }
        }
        for i in 1..=limit {
            result.small[i] += result.small[i - 1];
        }
        // Smaller quotient arguments have already been computed.
        for index in (1..=count).rev() {
            let x = n / index;
            let mut total = x as i64 * (x + 1) as i64 / 2;
            let mut left = 2;
            while left <= x {
                let quotient = x / left;
                let right = x / quotient;
                total -= (right - left + 1) as i64 * result.get(quotient);
                left = right + 1;
            }
            result.large[index] = total;
        }
        result
    }

    fn get(&self, x: usize) -> i64 {
        if x <= self.limit {
            self.small[x]
        } else {
            self.large[self.n / x]
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.split_whitespace().next().unwrap().parse().unwrap();
    let totients = Totients::new(n);
    let mut factorial = 1;
    let mut weighted = 0;
    let mut previous = 0;
    let mut total = 0;
    let mut left = 1;
    while left <= n {
        let quotient = n / left;
        let right = n / quotient;
        // weighted is factorial times the current harmonic sum.
        for i in left..=right {
            weighted = (weighted * i as i64 + factorial) % MOD;
            factorial = factorial * i as i64 % MOD;
        }
        let harmonic = weighted * power(factorial, MOD - 2) % MOD;
        let difference = (harmonic - previous + MOD) % MOD;
        total = (total + difference * (totients.get(quotient) % MOD)) % MOD;
        previous = harmonic;
        left = right + 1;
    }
    let pairs = n as i64 * (n + 1) as i64 / 2 % MOD;
    println!("{}", total * power(pairs, MOD - 2) % MOD);
}
