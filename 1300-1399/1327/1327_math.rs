use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    // the fuses burn on the odd days; (x + 1) / 2 odd days are in 1..x
    println!("{}", (v[1] + 1) / 2 - v[0] / 2);
}
