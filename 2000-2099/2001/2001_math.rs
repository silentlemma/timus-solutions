use std::io::{self, Read};

fn solve(first: i32, second: i32, empty_first: i32, empty_second: i32) -> (i32, i32) {
    (first - empty_first, second - empty_second)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let a1: i32 = tokens.next().unwrap().parse().unwrap();
    let b1: i32 = tokens.next().unwrap().parse().unwrap();
    let _ = tokens.next().unwrap();
    let b2: i32 = tokens.next().unwrap().parse().unwrap();
    let a3: i32 = tokens.next().unwrap().parse().unwrap();
    let _ = tokens.next().unwrap();
    let (first, second) = solve(a1, b1, a3, b2);
    println!("{} {}", first, second);
}
