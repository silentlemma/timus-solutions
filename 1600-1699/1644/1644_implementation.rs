use std::io::{self, Read};

const KNOWN_HUNGRY: u32 = 2; // given in the statement
const KNOWN_FULL: u32 = 10;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let words: Vec<&str> = text.split_ascii_whitespace().collect();
    let (mut hungry, mut full) = (KNOWN_HUNGRY, KNOWN_FULL);
    for pair in words[1..].chunks(2) {
        let count: u32 = pair[0].parse().unwrap();
        if pair[1] == "hungry" {
            hungry = hungry.max(count);
        } else {
            full = full.min(count);
        }
    }
    // the smallest satisfying amount must exceed the largest hungry one
    if full > hungry {
        println!("{}", full);
    } else {
        println!("Inconsistent");
    }
}
