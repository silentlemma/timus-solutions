use std::io::{self, Read, Write};

fn main() {
    let mut text = Vec::new();
    io::stdin().read_to_end(&mut text).unwrap();
    // every run of Latin letters is reversed in place; everything else stays
    let mut i = 0;
    while i < text.len() {
        let mut j = i;
        while j < text.len() && text[j].is_ascii_alphabetic() {
            j += 1;
        }
        text[i..j].reverse();
        i = j.max(i + 1);
    }
    io::stdout().write_all(&text).unwrap();
}
