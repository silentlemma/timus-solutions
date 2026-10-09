use std::io::{self, Read};

// three stones in a row can be cleared down to one, which settles the 2D case
const GROUP: u32 = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut v: Vec<u32> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    v.sort();
    let (m, n) = (v[0], v[1]);
    let answer = if m == 1 {
        (n + 1) / 2
    } else if m % GROUP == 0 || n % GROUP == 0 {
        2
    } else {
        1
    };
    println!("{}", answer);
}
