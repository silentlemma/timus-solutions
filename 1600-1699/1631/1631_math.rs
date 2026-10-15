use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut nums = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let (m, n) = (nums.next().unwrap(), nums.next().unwrap());
    // m * n moves close the tour; m + n + 1 of them are diagonal
    let diagonal = m + n + 1;
    let length = (m * n) as f64 + diagonal as f64 * (std::f64::consts::SQRT_2 - 1.0);
    println!("{:.12}", length);
}
