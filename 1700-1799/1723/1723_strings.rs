use std::io::{self, Read};

const LETTERS: usize = 26;

// every occurrence of a spell starts with an occurrence of its first
// letter, so a most frequent single letter is a strongest spell
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut count = [0; LETTERS];
    let mut best = 0;
    for c in input.trim().bytes() {
        let i = (c - b'a') as usize;
        count[i] += 1;
        if count[i] > count[best] {
            best = i;
        }
    }
    println!("{}", (b'a' + best as u8) as char);
}
