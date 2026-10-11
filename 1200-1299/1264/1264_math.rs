use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<u64>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    // one line for each element and each value 0..M
    println!("{}", n * (m + 1));
}
