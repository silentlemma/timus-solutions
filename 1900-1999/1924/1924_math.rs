use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let size = input.trim().parse::<usize>().unwrap();
    let total = size * (size + 1) / 2;
    println!("{}", if total % 2 == 0 { "black" } else { "grimy" });
}
