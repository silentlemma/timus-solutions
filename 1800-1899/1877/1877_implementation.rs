use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u32> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (first, second) = (v[0], v[1]);
    // on night k the thief tries code k on lock 1 when k is even and on
    // lock 2 when k is odd
    println!(
        "{}",
        if first % 2 == 0 || second % 2 == 1 {
            "yes"
        } else {
            "no"
        }
    );
}
