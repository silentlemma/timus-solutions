use std::io::{self, Read};

const LEGS: i32 = 40;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i32> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let (a, b) = (v[0], v[1]);
    // either every right slipper turns up while the left legs are dressed,
    // or 39 rights do, and then every spare left slipper is thrown away
    // before the last right leg is dressed
    println!("{}", (2 * b + LEGS).max(2 * a + LEGS - 1));
}
