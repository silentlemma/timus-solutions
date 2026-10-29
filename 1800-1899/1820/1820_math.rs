use std::io::{self, Read};

const SIDES: u32 = 2;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u32> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (v[0], v[1]);
    // every minute fries at most k of the 2n sides, and one steak takes
    // two minutes on its own; rotating sides cyclically reaches both bounds
    println!("{}", SIDES.max((SIDES * n + k - 1) / k));
}
