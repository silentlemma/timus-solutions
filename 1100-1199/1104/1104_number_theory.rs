use std::io::{self, Read};

const MAX_BASE: u32 = 36;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let s = input.split_ascii_whitespace().next().unwrap();
    let digits: Vec<u32> = s.chars().map(|c| c.to_digit(MAX_BASE).unwrap()).collect();
    let total: u32 = digits.iter().sum();
    let top = digits.iter().copied().max().unwrap().max(1);
    // base k is 1 modulo k - 1, so the number is congruent to its digit sum
    match (top + 1..=MAX_BASE).find(|k| total % (k - 1) == 0) {
        Some(k) => println!("{}", k),
        None => println!("No solution."),
    }
}
