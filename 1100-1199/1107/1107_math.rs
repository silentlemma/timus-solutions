use std::fmt::Write;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let mut next = || tok.next().unwrap();
    let (n, k, _) = (next(), next(), next());
    // removing an item changes the sum by 1..N and replacing one by -N+1..N-1,
    // never by a multiple of N + 1, so similar sets differ modulo N + 1
    let mut out = String::from("YES\n");
    for _ in 0..k {
        let count = next();
        let sum: usize = (0..count).map(|_| next()).sum();
        writeln!(out, "{}", sum % (n + 1) + 1).unwrap();
    }
    print!("{}", out);
}
