use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut nums = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut next = || nums.next().unwrap();
    let (a1, b1, a2, b2) = (next(), next(), next(), next());
    // the largest singular value of [[a1, b1], [a2, b2]] without cancellation:
    // both sums of squares are exact integers
    let p = (a1 + b2) * (a1 + b2) + (b1 - a2) * (b1 - a2);
    let q = (a1 - b2) * (a1 - b2) + (b1 + a2) * (b1 + a2);
    println!("{:.10}", ((p as f64).sqrt() + (q as f64).sqrt()) / 2.0);
}
