use std::io::{self, Read};

const ALPHABET: usize = 3;
const TARGET: usize = 6;

fn solve(values: &[usize]) -> bool {
    let mut counts = [0_usize; ALPHABET];
    let mut ways = 1;
    for (index, &value) in values.iter().enumerate() {
        counts[value - 1] += 1;
        ways = ways * (index + 1) / counts[value - 1];
        if ways >= TARGET {
            return true;
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let n = tokens.next().unwrap();
    let values: Vec<usize> = tokens.take(n).collect();
    println!("{}", if solve(&values) { "Yes" } else { "No" });
}
