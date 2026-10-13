use std::io::{self, Read};

// the counts for N = 1 and N = 2; from N = 3 on, 1575 and N - 3 zeros
const SMALL: [&str; 3] = ["", "14", "155"];
const SHORT: usize = 3;
const BASE: &str = "1575";

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    if n < SHORT {
        println!("{}", SMALL[n]);
    } else {
        println!("{}{}", BASE, "0".repeat(n - SHORT));
    }
}
