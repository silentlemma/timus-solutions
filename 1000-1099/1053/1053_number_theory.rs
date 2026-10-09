use std::io::{self, Read};

fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<u64>().unwrap());
    let n = it.next().unwrap() as usize;
    // cutting a shorter piece off a longer one keeps the gcd of all lengths,
    // so the last piece is always the gcd and the answer is never ambiguous
    let g = it.take(n).fold(0, gcd);
    println!("{}", g);
}
