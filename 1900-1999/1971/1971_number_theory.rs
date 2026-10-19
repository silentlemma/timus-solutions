use std::collections::HashMap;
use std::io::{self, Read};

const FACTOR_LIMIT: usize = 100;
const LOW_FPS: i32 = 10;
const HIGH_FPS: i32 = 60;
type Counts = [i32; FACTOR_LIMIT + 1];
type Factors = Vec<Vec<(usize, i32)>>;

fn factor_table() -> (Vec<usize>, Factors) {
    let mut primes = Vec::new();
    let mut factors = vec![Vec::new(); FACTOR_LIMIT + 1];
    for value in 2..=FACTOR_LIMIT {
        let mut remaining = value;
        for &prime in &primes {
            let mut exponent = 0;
            while remaining % prime == 0 {
                remaining /= prime;
                exponent += 1;
            }
            if exponent != 0 {
                factors[value].push((prime, exponent));
            }
        }
        if remaining > 1 {
            factors[value].push((remaining, 1));
            if remaining == value {
                primes.push(value);
            }
        }
    }
    (primes, factors)
}

fn classify(
    width: i32,
    height: i32,
    power: i32,
    counts: &Counts,
    primes: &[usize],
) -> &'static str {
    let area = width * height;
    let limit = power / (LOW_FPS * area);
    if limit == 0 {
        return "Slideshow";
    }
    let mut product = 1;
    for &prime in primes {
        for _ in 0..counts[prime] {
            if product > limit / prime as i32 {
                return "Slideshow";
            }
            product *= prime as i32;
        }
    }
    if product <= power / (HIGH_FPS * area) {
        "Perfect"
    } else {
        "So-so"
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let (primes, factors) = factor_table();
    let mut counts = [0; FACTOR_LIMIT + 1];
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut options = HashMap::with_capacity(n);
    for _ in 0..n {
        let name = tokens.next().unwrap();
        let value: usize = tokens.next().unwrap().parse().unwrap();
        options.insert(name, value);
        for &(prime, exponent) in &factors[value] {
            counts[prime] += exponent;
        }
    }
    let mut width = tokens.next().unwrap().parse().unwrap();
    let mut height = tokens.next().unwrap().parse().unwrap();
    let power = tokens.next().unwrap().parse().unwrap();
    let changes: usize = tokens.next().unwrap().parse().unwrap();
    let mut answer = String::from(classify(width, height, power, &counts, &primes));
    answer.push('\n');
    for _ in 0..changes {
        let command = tokens.next().unwrap();
        if command == "Resolution" {
            width = tokens.next().unwrap().parse().unwrap();
            height = tokens.next().unwrap().parse().unwrap();
        } else {
            let name = tokens.next().unwrap();
            let change = if command == "On" { 1 } else { -1 };
            for &(prime, exponent) in &factors[options[name]] {
                counts[prime] += change * exponent;
            }
        }
        answer.push_str(classify(width, height, power, &counts, &primes));
        answer.push('\n');
    }
    print!("{answer}");
}
