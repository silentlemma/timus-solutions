use std::io::{self, Read};

const SHIFT: i32 = 5; // added to the first letter
const LETTERS: i32 = 26;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // each code is the previous code plus the letter, modulo 26: take differences
    let mut prev = SHIFT;
    let plain: String = input
        .trim()
        .bytes()
        .map(|ch| {
            let code = (ch - b'a') as i32;
            let letter = (b'a' + (code - prev).rem_euclid(LETTERS) as u8) as char;
            prev = code;
            letter
        })
        .collect();
    println!("{}", plain);
}
