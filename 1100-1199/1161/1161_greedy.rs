use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<u32>().unwrap());
    let n = tok.next().unwrap() as usize;
    let mut weights: Vec<u32> = tok.take(n).collect();
    weights.sort_by(|a, b| b.cmp(a));
    // each collision takes a square root of the product, so the heaviest
    // stripies should meet first and be rooted the most times
    let total = weights[1..]
        .iter()
        .fold(weights[0] as f64, |t, &w| 2.0 * (t * w as f64).sqrt());
    println!("{:.2}", total);
}
