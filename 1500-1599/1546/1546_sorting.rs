use std::io::{self, Read, Write};

/// A name written so that plain string order compares it (a number becomes "0",
/// its length without leading zeros in seven digits and those digits, a letter
/// "1" and itself), and minus the leading zeros of each number.
fn key_of(s: &[u8]) -> (Vec<u8>, Vec<i64>) {
    let (mut main, mut zeros) = (Vec::new(), Vec::new());
    let mut i = 0;
    while i < s.len() {
        if !s[i].is_ascii_digit() {
            main.push(b'1');
            main.push(s[i]);
            i += 1;
            continue;
        }
        let start = i;
        while i < s.len() && s[i] == b'0' {
            i += 1;
        }
        let digits = i;
        while i < s.len() && s[i].is_ascii_digit() {
            i += 1;
        }
        main.push(b'0');
        main.extend(format!("{:07}", i - digits).bytes());
        main.extend_from_slice(&s[digits..i]);
        zeros.push(start as i64 - digits as i64);
    }
    (main, zeros)
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut names: Vec<(Vec<u8>, Vec<i64>, &str)> = s
        .split_ascii_whitespace()
        .map(|w| {
            let (main, zeros) = key_of(w.as_bytes());
            (main, zeros, w)
        })
        .collect();
    // letters and numbers by value first; then, run by run, more leading zeros first
    names.sort_by(|a, b| (&a.0, &a.1).cmp(&(&b.0, &b.1)));
    let mut out = String::new();
    for (_, _, w) in &names {
        out.push_str(w);
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
