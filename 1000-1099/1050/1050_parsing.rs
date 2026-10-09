use std::io::{self, Read, Write};

// what happens to a double quote
#[derive(Clone, Copy, PartialEq)]
enum Mark {
    Keep,
    Open,
    Close,
    Drop,
}

fn blank(c: u8) -> bool {
    matches!(c, b' ' | b'\t' | b'\r' | b'\x0b' | b'\x0c')
}

// pairs the quotes of the finished paragraph; an unpaired last one goes away
fn close(quotes: &mut Vec<usize>, mark: &mut [Mark]) {
    if quotes.len() % 2 == 1 {
        mark[quotes.pop().unwrap()] = Mark::Drop;
    }
    for (k, &q) in quotes.iter().enumerate() {
        mark[q] = if k % 2 == 0 { Mark::Open } else { Mark::Close };
    }
    quotes.clear();
}

fn main() {
    // the text is handled as bytes: letters above 127 are copied as they are
    let mut s = Vec::new();
    io::stdin().read_to_end(&mut s).unwrap();
    let n = s.len();
    let mut mark = vec![Mark::Keep; n];
    let mut quotes = Vec::new();
    let mut i = 0;
    while i < n {
        if s[i] == b'\\' {
            // \" is an umlaut; otherwise the command name is the letters after \.
            if i + 1 < n && s[i + 1] == b'"' {
                i += 2;
                continue;
            }
            let mut j = i + 1;
            while j < n && s[j].is_ascii_alphabetic() {
                j += 1;
            }
            if &s[i + 1..j] == b"par" {
                close(&mut quotes, &mut mark);
            }
            i = j;
        } else if s[i] == b'"' {
            quotes.push(i);
            i += 1;
        } else {
            // a line of only whitespace that ends with a line break ends a paragraph
            if s[i] == b'\n' {
                let mut j = i + 1;
                while j < n && blank(s[j]) {
                    j += 1;
                }
                if j < n && s[j] == b'\n' {
                    close(&mut quotes, &mut mark);
                }
            }
            i += 1;
        }
    }
    close(&mut quotes, &mut mark);
    let mut out = Vec::with_capacity(n + n / 2);
    for (c, m) in s.iter().zip(mark.iter()) {
        match m {
            Mark::Keep => out.push(*c),
            Mark::Open => out.extend_from_slice(b"``"),
            Mark::Close => out.extend_from_slice(b"''"),
            Mark::Drop => {}
        }
    }
    io::stdout().write_all(&out).unwrap();
}
