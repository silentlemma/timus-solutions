use std::io::{self, Read};

const SMALLEST: u64 = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let k: u64 = input.trim().parse().unwrap();
    // the second player wins exactly when L + 1 divides K: find the smallest
    // divisor of K that is at least 3
    let small = (SMALLEST..).take_while(|d| d * d <= k).find(|d| k % d == 0);
    // no such divisor up to sqrt(K): above it the candidates are K / 2 and K
    let d = small.unwrap_or(if k % 2 == 0 && k / 2 >= SMALLEST {
        k / 2
    } else {
        k
    });
    println!("{}", d - 1);
}
