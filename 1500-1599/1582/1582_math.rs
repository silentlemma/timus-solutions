use std::io::{self, Read};

const TOTAL: f64 = 1000.0;
const HALF: f64 = 0.5;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let inverse: f64 = text
        .split_ascii_whitespace()
        .map(|w| 1.0 / w.parse::<f64>().unwrap())
        .sum();
    // betting in proportion to 1 / k on every outcome pays the same whatever
    // happens, and any other split pays less on some outcome
    println!("{}", (TOTAL / inverse + HALF).floor() as i64);
}
