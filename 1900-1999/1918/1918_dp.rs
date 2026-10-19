use std::io::{self, Read};

const MODULUS: u64 = 1000000007;

fn power(mut value: u64, mut exponent: usize) -> u64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 != 0 {
            result = result * value % MODULUS;
        }
        value = value * value % MODULUS;
        exponent >>= 1;
    }
    result
}

fn settings_counts(size: usize) -> Vec<u64> {
    let mut ways = vec![0; size + 1];
    for count in 1..=size {
        let mut closed = 0;
        let base = count as u64;
        for &coefficient in &ways[1..count] {
            closed = (closed * base + coefficient) % MODULUS;
        }
        let difference = (power(base, count - 1) + MODULUS - closed) % MODULUS;
        ways[count] = base * difference % MODULUS;
    }
    ways
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let size = text.trim().parse::<usize>().unwrap();
    println!("{}", settings_counts(size)[size]);
}
