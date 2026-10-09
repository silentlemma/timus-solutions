use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // Horner's scheme: ((a0 * X + a1) * X + a2) ... in reverse Polish notation
    let mut out = String::from("0\n");
    for i in 1..=n {
        writeln!(out, "X\n*\n{}\n+", i).unwrap();
    }
    print!("{}", out);
}
