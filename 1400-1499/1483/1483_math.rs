use std::io::{self, Read};

const WIN: u32 = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u32 = input.trim().parse().unwrap();
    // every match gives out at least 2 points (a draw) and at most WIN,
    // so the leader has at least the average of all draws and the last team
    // at most the average of all wins; both bounds can be reached
    println!("{} {}", n - 1, WIN * (n - 1) / 2);
}
