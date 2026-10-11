use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    // v[1] is the whole array; each factor is the next one times the size of
    // the next dimension, and the first one times the size of the first
    let sizes = &v[1..n + 2];
    let bounds: Vec<String> = sizes
        .windows(2)
        .map(|w| (w[0] / w[1] - 1).to_string())
        .collect();
    println!("{}", bounds.join(" "));
}
