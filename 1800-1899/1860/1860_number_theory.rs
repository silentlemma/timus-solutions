use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // F_n is the product of k^fib(n - k + 1) over k from 1 to n, with
    // fib(1) = fib(2) = 1; weight[k] = fib(n - k + 1) modulo MOD
    let mut fib = vec![0u64; n + 2];
    fib[1] = 1;
    for i in 2..=n + 1 {
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD;
    }
    let weight: Vec<u64> = (0..=n).map(|k| if k == 0 { 0 } else { fib[n - k + 1] }).collect();
    let mut composite = vec![false; n + 1];
    // the exponent of a prime p sums the weights of the multiples of p, of
    // p^2, and so on; the divisors number the product of exponents plus 1
    let mut answer = 1u64;
    for p in 2..=n {
        if composite[p] {
            continue;
        }
        for q in (p * p..=n).step_by(p) {
            composite[q] = true;
        }
        let mut exponent = 0u64;
        let mut power = p;
        while power <= n {
            let part: u64 = (power..=n).step_by(power).map(|k| weight[k]).sum();
            exponent = (exponent + part) % MOD;
            power = power.saturating_mul(p);
        }
        answer = answer * ((exponent + 1) % MOD) % MOD;
    }
    println!("{}", answer);
}
