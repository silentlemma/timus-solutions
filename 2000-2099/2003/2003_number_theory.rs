use std::collections::HashMap;
use std::io::{self, Read};

const PERSISTENT_COUNT: usize = 3;

fn solve(values: &[usize]) -> String {
    let maximum = *values.iter().max().unwrap();
    let mut limit = 0;
    while (limit + 1) * (limit + 1) <= maximum {
        limit += 1;
    }
    let mut composite = vec![false; limit + 1];
    let mut primes = Vec::new();
    for prime in 2..=limit {
        if composite[prime] {
            continue;
        }
        primes.push(prime);
        let mut multiple = prime * prime;
        while multiple <= limit {
            composite[multiple] = true;
            multiple += prime;
        }
    }
    let mut counts = HashMap::new();
    let mut best = 0;
    for &original in values {
        let mut value = original;
        for &prime in &primes {
            if prime * prime > value {
                break;
            }
            if value % prime != 0 {
                continue;
            }
            let count = counts.entry(prime).or_insert(0);
            *count += 1;
            if *count == PERSISTENT_COUNT {
                return "infinity".to_string();
            }
            best = best.max(*count);
            while value % prime == 0 {
                value /= prime;
            }
        }
        if value > 1 {
            let count = counts.entry(value).or_insert(0);
            *count += 1;
            if *count == PERSISTENT_COUNT {
                return "infinity".to_string();
            }
            best = best.max(*count);
        }
    }
    best.to_string()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let size: usize = tokens.next().unwrap().parse().unwrap();
    let values: Vec<usize> = (0..size)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    println!("{}", solve(&values));
}
