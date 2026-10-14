use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let words: Vec<&str> = s.split_ascii_whitespace().collect();
    let n: usize = words[0].parse().unwrap();
    let letter = words[1 + n].as_bytes()[0];
    // the dictionary order is kept, repeated entries are printed every time
    let mut out = String::new();
    for w in &words[1..=n] {
        if w.as_bytes()[0] == letter {
            out.push_str(w);
            out.push('\n');
        }
    }
    print!("{}", out);
}
