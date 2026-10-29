use std::io::{self, BufWriter, Read, Write};

const OUTPUT_BUFFER_SIZE: usize = 256;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    // every hieroglyph is two letters, kept as a pair of bytes, and the answer
    // goes out through a small buffered writer
    let mut words = Vec::with_capacity(count);
    for _ in 0..count {
        let word = tokens.next().unwrap().as_bytes();
        words.push([word[0], word[1]]);
    }
    let letter = tokens.next().unwrap().as_bytes()[0];
    let stdout = io::stdout();
    let mut output = BufWriter::with_capacity(OUTPUT_BUFFER_SIZE, stdout.lock());
    // the dictionary order is kept, repeated entries are printed every time
    for word in words {
        if word[0] == letter {
            output.write_all(&word).unwrap();
            output.write_all(b"\n").unwrap();
        }
    }
}
