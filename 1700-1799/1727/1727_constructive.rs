use std::io::{self, Read, Write};

const LIMIT: i32 = 100000;
const BASE: i32 = 10;
const SMALL: i32 = BASE - 1;
const REMAINDER: i32 = SMALL * (SMALL + 1) / 2;

fn digit_sum(mut value: i32) -> i32 {
    let mut sum = 0;
    while value > 0 {
        sum += value % BASE;
        value /= BASE;
    }
    sum
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut remaining: i32 = input.trim().parse().unwrap();
    let mut chosen = Vec::new();
    let mut value = LIMIT - 1;
    // The first ten thousand candidates have digit sum 270000 in total.
    // This phase stops before any one-digit number is used.
    while remaining > REMAINDER {
        chosen.push(value);
        remaining -= digit_sum(value);
        value -= 1;
    }
    // Distinct digits 1..9 can make every sum from zero through 45.
    for digit in (1..=SMALL).rev() {
        if digit <= remaining {
            chosen.push(digit);
            remaining -= digit;
        }
    }
    let mut out = io::BufWriter::new(io::stdout().lock());
    writeln!(out, "{}", chosen.len()).unwrap();
    for number in chosen {
        write!(out, "{} ", number).unwrap();
    }
    writeln!(out).unwrap();
}
