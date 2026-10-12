use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u64 = input.trim().parse().unwrap();
    // (n^2)^2 = n^4 = n^3 * n
    println!("{}", n * n);
    println!("{}", n);
}
