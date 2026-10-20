use std::io::{self, Read};

const CHOICES: u64 = 3;

fn mod_pow(mut base: u64, mut exponent: u64, modulus: u64) -> u64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent % 2 == 1 {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exponent /= 2;
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: u64 = tokens.next().unwrap().parse().unwrap();
    let p: u64 = tokens.next().unwrap().parse().unwrap();

    let half = (p - 1) / 2;
    let mut exponent = 0;
    let mut remaining = n;
    let mut digits = Vec::new();
    while remaining > 0 {
        let mut digit = remaining % p;
        // Reflect upper digits to keep the recurrence below half the modulus.
        if digit > half {
            digit = p - 1 - digit;
            exponent += half - digit;
        }
        digits.push(digit);
        remaining /= p;
    }
    digits.sort_unstable();

    let mut index = 0;
    let mut previous = 1;
    let mut current = 1;
    let mut factorial = 1;
    let mut numerator = 1;
    let mut denominator = 1;
    for digit in digits {
        while index < digit {
            index += 1;
            // Scaling the central coefficient by index! avoids modular division.
            let next =
                ((2 * index - 1) * current + CHOICES * (index - 1) * (index - 1) * previous) % p;
            previous = current;
            current = next;
            factorial = factorial * index % p;
        }
        numerator = numerator * current % p;
        denominator = denominator * factorial % p;
    }

    let mut draws = numerator * mod_pow(denominator, p - 2, p) % p;
    draws = draws * mod_pow(p - CHOICES, exponent, p) % p;
    let mut answer = (mod_pow(CHOICES, n, p) + p - draws) % p;
    answer = answer * ((p + 1) / 2) % p;
    println!("{}", answer);
}
