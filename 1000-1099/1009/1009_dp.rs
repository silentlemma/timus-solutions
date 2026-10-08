use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (v[0], v[1]);
    // numbers of valid prefixes ending with a zero and with another digit,
    // where the first digit is not zero
    let (mut zero, mut other) = (0, k - 1);
    for _ in 1..n {
        (zero, other) = (other, (zero + other) * (k - 1));
    }
    println!("{}", zero + other);
}
