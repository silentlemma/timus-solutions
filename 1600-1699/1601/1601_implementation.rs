use std::io::{self, Read, Write};

const ENDS: &[u8] = b".!?"; // marks that end a sentence

fn main() {
    let mut text = Vec::new();
    io::stdin().read_to_end(&mut text).unwrap();
    let mut start = true; // the next letter opens a sentence
    for c in text.iter_mut() {
        if c.is_ascii_uppercase() {
            if !start {
                *c = c.to_ascii_lowercase();
            }
            start = false;
        } else if ENDS.contains(c) {
            start = true;
        }
    }
    io::stdout().write_all(&text).unwrap();
}
