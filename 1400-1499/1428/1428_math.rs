use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u32> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (a, b, c) = (v[0], v[1], v[2]);
    // 2^(C-1) + 2^(C-1) = 2^C, and A and B both divide C - 1
    println!("{}", 1u64 << ((c - 1) / a));
    println!("{}", 1u64 << ((c - 1) / b));
    println!("2");
}
