use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut base: Vec<u32> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let _separator = tokens.next();
    let k: usize = tokens.next().unwrap().parse().unwrap();
    // the i-th smallest element is the i-th element of the sorted database
    base.sort_unstable();
    let mut out = String::new();
    for _ in 0..k {
        let i: usize = tokens.next().unwrap().parse().unwrap();
        writeln!(out, "{}", base[i - 1]).unwrap();
    }
    print!("{}", out);
}
