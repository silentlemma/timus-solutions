use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // every day uses three pairs and every pair may meet three times, so
    // at most n (n - 1) / 2 days; the triples i, i + d, i + 2d modulo n
    // give each pair three meetings: twice as neighbours, once apart
    let mut out = String::new();
    writeln!(out, "{}", n * (n - 1) / 2).unwrap();
    for d in 1..=(n - 1) / 2 {
        for i in 0..n {
            writeln!(out, "{} {} {}", i + 1, (i + d) % n + 1, (i + 2 * d) % n + 1).unwrap();
        }
    }
    print!("{}", out);
}
