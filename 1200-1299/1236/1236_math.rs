use std::fmt::Write as _;
use std::io::{self, Read};

const SPACE: u8 = b' ';
const HEX: u32 = 16;

fn decode(s: &str) -> Vec<u8> {
    s.as_bytes()
        .chunks(2)
        .map(|c| u8::from_str_radix(std::str::from_utf8(c).unwrap(), HEX).unwrap())
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let short = decode(it.next().unwrap());
    let long = decode(it.next().unwrap());
    // the long message is a space followed by the short one, so its first
    // byte gives the first key byte, and byte i+1 of the long message hides
    // the same clear byte as byte i of the short one
    let mut key = vec![long[0] ^ SPACE];
    for (i, &e) in short.iter().enumerate() {
        let prev = key[i];
        key.push(long[i + 1] ^ e ^ prev);
    }
    let mut out = String::with_capacity(2 * key.len());
    for k in key {
        write!(out, "{:02X}", k).unwrap();
    }
    println!("{}", out);
}
