use std::io::{self, Read};

const NAME: &[u8] = b"Sandro";
const COINS: u32 = 5;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let text = input.trim().as_bytes();
    let best = text
        .windows(NAME.len())
        .map(|window| {
            window
                .iter()
                .zip(NAME)
                .map(|(a, b)| {
                    // one fee for the wrong case, one for the wrong letter
                    let case = (a.is_ascii_uppercase() != b.is_ascii_uppercase()) as u32;
                    let letter = (a.to_ascii_lowercase() != b.to_ascii_lowercase()) as u32;
                    COINS * (case + letter)
                })
                .sum::<u32>()
        })
        .min()
        .unwrap();
    println!("{}", best);
}
