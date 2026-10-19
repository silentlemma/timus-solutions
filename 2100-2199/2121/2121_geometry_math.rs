use std::io::{self, Read};

const SIDE_FACTOR: u64 = 4; // the area is 4a - 1/3

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let a: u64 = input.trim().parse().unwrap();
    // 4a - 1/3 = (4a - 1) + 2/3, and 2/3 rounds to 0.6666666667
    println!("{}.6666666667", SIDE_FACTOR * a - 1);
}
