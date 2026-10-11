use std::fmt::Write as _;
use std::io::{self, Read};

const PERCENT: f64 = 100.0;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let mut votes = vec![0usize; n + 1];
    for c in it.take(m) {
        votes[c] += 1;
    }
    let mut out = String::new();
    for &v in &votes[1..] {
        writeln!(out, "{:.2}%", PERCENT * v as f64 / m as f64).unwrap();
    }
    print!("{}", out);
}
