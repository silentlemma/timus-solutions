use std::collections::HashMap;
use std::io::{self, Read};

const BASE: u32 = 10;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // the exponents of the primes in the product of all the numbers
    let mut exponent: HashMap<u32, u32> = HashMap::new();
    for token in input.split_ascii_whitespace() {
        let mut x: u32 = token.parse().unwrap();
        let mut p = 2;
        while p * p <= x {
            while x % p == 0 {
                *exponent.entry(p).or_insert(0) += 1;
                x /= p;
            }
            p += 1;
        }
        if x > 1 {
            *exponent.entry(x).or_insert(0) += 1;
        }
    }
    // a divisor picks each prime from 0 to its exponent times
    let last = exponent.values().fold(1, |acc, &e| acc * (e + 1) % BASE);
    println!("{}", last);
}
