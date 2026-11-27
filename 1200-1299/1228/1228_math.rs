use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    // v[1] is the total size. A multiplier times its dimension size equals
    // the preceding multiplier, or the total size for the first dimension.
    let sizes = &v[1..n + 2];
    let bounds: Vec<String> = sizes
        .windows(2)
        .map(|w| (w[0] / w[1] - 1).to_string())
        .collect();
    println!("{}", bounds.join(" "));
}
