use std::io::{self, Read};

fn main() {
    let mut text = Vec::new();
    io::stdin().read_to_end(&mut text).unwrap();
    let mut errors = 0;
    // a new sentence waits for its first letter; in_word: the previous character
    // was a letter
    let (mut new_sentence, mut in_word) = (true, false);
    for &c in &text {
        if c.is_ascii_alphabetic() {
            if c.is_ascii_lowercase() && new_sentence {
                errors += 1;
            }
            if c.is_ascii_uppercase() && in_word {
                errors += 1;
            }
            new_sentence = false;
            in_word = true;
        } else {
            in_word = false;
            if c == b'.' || c == b'?' || c == b'!' {
                new_sentence = true;
            }
        }
    }
    println!("{}", errors);
}
