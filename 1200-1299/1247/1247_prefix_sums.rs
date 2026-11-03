use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<i32>().unwrap());
    let (size, limit) = (numbers.next().unwrap(), numbers.next().unwrap());
    let mut prefix = 0;
    // Total excess equals limit. A negative prefix makes the remaining
    // suffix too heavy; a prefix above limit itself violates the bound.
    for _ in 0..size {
        prefix += numbers.next().unwrap() - 1;
        if prefix < 0 || prefix > limit {
            println!("NO");
            return;
        }
    }
    println!("YES");
}
