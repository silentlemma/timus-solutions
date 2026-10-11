use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // rows of the ages 1..k starting with 1: a(k) = a(k-1) + a(k-3) + 1,
    // with a(1) = 1 and the rule run back to a(0) = 0, a(-1) = -1
    let (mut older, mut old, mut cur) = (-1i64, 0i64, 1i64);
    for _ in 1..n {
        (older, old, cur) = (old, cur, cur + older + 1);
    }
    println!("{}", cur);
}
