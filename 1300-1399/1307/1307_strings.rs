use std::io::{self, BufWriter, Read, Write};

// common pieces of English, tried in this order; each one that pays off
// gets a printable character the text never uses
const PIECES: [&str; 44] = [
    "\n", " the ", "the ", " and ", "ing ", " of ", " to ", "ed ", "he ", "th", "in", "er", "an",
    "re", "on", "at", "en", "nd", "es", "or", "ou", "ha", "is", "it", "te", "st", "ar", "al", "le",
    "se", "ve", "me", "ne", "hi", "as", "ng", "e ", "s ", "d ", "t ", ", ", ". ", "y ", "o ",
];
const ENTRY: usize = 24; // the size of one table line, so a piece must save more than this
const CHUNK: usize = 1000; // characters of the coded text per string literal

const FIRST: u8 = 33; // the first printable character that may become a code
const LAST: u8 = 126; // and the last one
const SPECIAL: &[u8] = b"\"\\?"; // need a backslash inside a C string

// the text as it is written inside a C string literal
fn write_literal(out: &mut impl Write, text: &[u8]) {
    for &ch in text {
        if ch == b'\n' {
            out.write_all(b"\\n").unwrap();
            continue;
        }
        if SPECIAL.contains(&ch) {
            out.write_all(b"\\").unwrap();
        }
        out.write_all(&[ch]).unwrap();
    }
}

fn main() {
    let mut text = Vec::new();
    io::stdin().read_to_end(&mut text).unwrap();
    text.retain(|&c| c != b'\r');
    let mut free: Vec<u8> = (FIRST..=LAST)
        .filter(|c| !text.contains(c) && !SPECIAL.contains(c))
        .collect();
    free.reverse();
    let mut table: Vec<(u8, &str)> = Vec::new();
    for piece in PIECES {
        let code = match free.last() {
            Some(&c) => c,
            None => break,
        };
        let p = piece.as_bytes();
        let mut uses = 0;
        let mut at = 0;
        while at + p.len() <= text.len() {
            if &text[at..at + p.len()] == p {
                uses += 1;
                at += p.len();
            } else {
                at += 1;
            }
        }
        // every use saves the written length of the piece less one character
        let written: usize = p
            .iter()
            .map(|c| {
                if *c == b'\n' || SPECIAL.contains(c) {
                    2
                } else {
                    1
                }
            })
            .sum();
        if uses * (written - 1) <= ENTRY {
            continue;
        }
        // replace in place, left to right: the text only gets shorter
        let (mut read, mut write) = (0, 0);
        while read < text.len() {
            if text[read..].starts_with(p) {
                text[write] = code;
                read += p.len();
            } else {
                text[write] = text[read];
                read += 1;
            }
            write += 1;
        }
        text.truncate(write);
        table.push((code, piece));
        free.pop();
    }
    let mut out = BufWriter::new(io::stdout().lock());
    out.write_all(b"//CPP\n#include <cstdio>\nconst char *d[] = {\n")
        .unwrap();
    for part in text.chunks(CHUNK) {
        out.write_all(b"\"").unwrap();
        write_literal(&mut out, part);
        out.write_all(b"\",\n").unwrap();
    }
    out.write_all(b"0};\nint main() {\n    const char *t[256] = {0};\n")
        .unwrap();
    for (code, piece) in table {
        write!(out, "    t[{}] = \"", code).unwrap();
        write_literal(&mut out, piece.as_bytes());
        out.write_all(b"\";\n").unwrap();
    }
    out.write_all(
        b"    for (int k = 0; d[k]; k++)\n        for (const char *p = d[k]; *p; p++)\n            \
          if (t[(unsigned char)*p]) fputs(t[(unsigned char)*p], stdout);\n            \
          else putchar(*p);\n    return 0;\n}\n",
    )
    .unwrap();
}
