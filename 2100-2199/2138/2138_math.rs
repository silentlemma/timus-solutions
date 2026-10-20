use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: u32 = input.split_whitespace().nth(1).unwrap().parse().unwrap();
    // Both directions reverse the four base-256 digits, so the type does not matter.
    println!("{}", v.swap_bytes());
}
