use std::io::{self, Read};

const DWARFS: u32 = 7;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // the number has up to 51 digits, so take it modulo 7 digit by digit
    let rest = input
        .trim()
        .bytes()
        .fold(0, |r, d| (r * 10 + (d - b'0') as u32) % DWARFS);
    println!("{}", rest);
}
