use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // joining i and j whenever i + j > n gives student i a degree of i up to
    // the middle and i - 1 after it, so only one degree is shared, by two
    let pairs: Vec<(usize, usize)> = (1..=n)
        .flat_map(|i| (i + 1..=n).filter(move |&j| i + j > n).map(move |j| (i, j)))
        .collect();
    let mut out = format!("{}\n", pairs.len());
    for (i, j) in pairs {
        writeln!(out, "{} {}", i, j).unwrap();
    }
    print!("{}", out);
}
