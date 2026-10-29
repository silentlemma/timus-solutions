use std::io::{self, Read, Write};

fn main() {
    const MAX_LENGTH: usize = 200000;
    let mut text = Vec::with_capacity(MAX_LENGTH + 2);
    io::stdin().read_to_end(&mut text).unwrap();
    let mut size = 0;
    // a letter equal to the one before it cancels that one: removing the
    // inserted pairs in any order leaves the same text
    for i in 0..text.len() {
        let ch = text[i];
        if !ch.is_ascii_lowercase() {
            continue;
        }
        // the processed beginning of the input is the stack: it is never longer
        // than the part already read
        if size > 0 && text[size - 1] == ch {
            size -= 1;
        } else {
            text[size] = ch;
            size += 1;
        }
    }
    text.truncate(size);
    text.push(b'\n');
    io::stdout().lock().write_all(&text).unwrap();
}
