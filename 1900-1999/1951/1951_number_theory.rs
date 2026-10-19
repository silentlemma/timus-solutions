use std::io::{self, Read};

const SIEVE_LIMIT: usize = 10000;
const LOWER_MODULUS: usize = 5000;
const MODULUS_COUNT: usize = 510;

#[derive(Clone, Copy, PartialEq, Eq)]
struct ComplexPair {
    real: i64,
    imaginary: i64,
}

fn prime_moduli() -> Vec<i64> {
    let mut prime = vec![true; SIEVE_LIMIT + 1];
    prime[0] = false;
    prime[1] = false;
    let mut value = 2;
    while value * value <= SIEVE_LIMIT {
        if prime[value] {
            for multiple in (value * value..=SIEVE_LIMIT).step_by(value) {
                prime[multiple] = false;
            }
        }
        value += 1;
    }
    (LOWER_MODULUS..=SIEVE_LIMIT)
        .filter(|&index| prime[index])
        .take(MODULUS_COUNT)
        .map(|index| index as i64)
        .collect()
}

fn multiply(first: ComplexPair, second: ComplexPair, modulus: i64) -> ComplexPair {
    ComplexPair {
        real: (first.real * second.real - first.imaginary * second.imaginary).rem_euclid(modulus),
        imaginary: (first.real * second.imaginary + first.imaginary * second.real)
            .rem_euclid(modulus),
    }
}

fn power(real: i64, imaginary: i64, mut exponent: i32, modulus: i64) -> ComplexPair {
    let mut base = ComplexPair {
        real: real.rem_euclid(modulus),
        imaginary: imaginary.rem_euclid(modulus),
    };
    let mut result = ComplexPair {
        real: 1,
        imaginary: 0,
    };
    while exponent > 0 {
        if exponent & 1 != 0 {
            result = multiply(result, base, modulus);
        }
        base = multiply(base, base, modulus);
        exponent >>= 1;
    }
    result
}

fn gcd(mut first: i32, mut second: i32) -> i32 {
    while second != 0 {
        (first, second) = (second, first % second);
    }
    first
}

fn count_roots(a: i64, b: i64, n: i32, c: i64, d: i64, m: i32, moduli: &[i64]) -> i32 {
    let common = gcd(n, m);
    for &modulus in moduli {
        if power(a, b, m / common, modulus) != power(c, d, n / common, modulus) {
            return 0;
        }
    }
    common
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let a = words.next().unwrap().parse().unwrap();
    let b = words.next().unwrap().parse().unwrap();
    let n = words.next().unwrap().parse().unwrap();
    let c = words.next().unwrap().parse().unwrap();
    let d = words.next().unwrap().parse().unwrap();
    let m = words.next().unwrap().parse().unwrap();
    let moduli = prime_moduli();
    println!("{}", count_roots(a, b, n, c, d, m, &moduli));
}
