use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    // modulo n^2 + 1 the first number is -1 and the second is n, so the sum
    // of their squares is 1 + n^2, a multiple of n^2 + 1
    println!("{} {} {}", n * n, n * n + n + 1, n * n + 1);
}
