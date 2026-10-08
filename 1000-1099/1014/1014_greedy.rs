use std::io::{self, Read};

const BASE: u64 = 10;

fn smallest(mut n: u64) -> String {
    // a zero digit makes the product zero: 10 is the smallest such number
    if n == 0 {
        return BASE.to_string();
    }
    if n == 1 {
        return "1".to_string();
    }
    // the largest digits first give the fewest digits; then sort them up
    let mut digits = Vec::new();
    for d in (2..BASE).rev() {
        while n % d == 0 {
            digits.push(d);
            n /= d;
        }
    }
    if n != 1 {
        return "-1".to_string();
    }
    digits.iter().rev().map(|d| d.to_string()).collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    println!("{}", smallest(input.trim().parse().unwrap()));
}
