use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<u64> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let mut out = String::new();
    for &x in nums.iter().rev() {
        out.push_str(&format!("{:.4}\n", (x as f64).sqrt()));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
