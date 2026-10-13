use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let sum: i64 = v[1..=n].iter().sum();
    // the mean of squared distances is smallest at the arithmetic mean
    println!("{:.6}", sum as f64 / n as f64);
}
