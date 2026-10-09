use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let k = v[0];
    let mut size = v[1..=k].to_vec();
    // win a majority of the groups, choosing the smallest ones; a group of s
    // voters needs s / 2 + 1 supporters
    size.sort_unstable();
    let supporters: usize = size[..=k / 2].iter().map(|s| s / 2 + 1).sum();
    println!("{}", supporters);
}
