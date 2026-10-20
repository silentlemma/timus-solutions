use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;

struct Entry {
    value: usize,
    size: usize,
}

fn modular_power(mut base: u64, mut exponent: u64) -> u64 {
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

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut stack: Vec<Entry> = Vec::with_capacity(n);
    let mut factorial = 1;
    let mut denominator = 1;

    for i in 1..=n {
        let value = tokens.next().unwrap().parse().unwrap();
        let mut size = 0;
        // Popped nodes now have complete Cartesian subtrees.
        while stack.last().map_or(false, |entry| entry.value > value) {
            size += stack.pop().unwrap().size;
            denominator = denominator * size as u64 % MOD;
        }
        stack.push(Entry {
            value,
            size: size + 1,
        });
        factorial = factorial * i as u64 % MOD;
    }

    let mut size = 0;
    while let Some(entry) = stack.pop() {
        size += entry.size;
        denominator = denominator * size as u64 % MOD;
    }

    // The tree hook-length formula counts the equivalent permutations.
    println!("{}", factorial * modular_power(denominator, MOD - 2) % MOD);
}
