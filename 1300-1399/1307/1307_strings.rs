use std::io::{self, BufWriter, Read, Write};

// common pieces of English, tried along with the frequent words of the text
const PIECES: [&str; 44] = [
    "\n", " the ", "the ", " and ", "ing ", " of ", " to ", "ed ", "he ", "th", "in", "er", "an",
    "re", "on", "at", "en", "nd", "es", "or", "ou", "ha", "is", "it", "te", "st", "ar", "al", "le",
    "se", "ve", "me", "ne", "hi", "as", "ng", "e ", "s ", "d ", "t ", ", ", ". ", "y ", "o ",
];
const LINE: usize = 17; // a table line without its piece: '    t[NNN] = "";' and a line end
const CHUNK: usize = 1000; // characters of the coded text per string literal
const WORDS: usize = 300; // the most promising words of the text that are tried

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

fn written_length(piece: &[u8]) -> usize {
    piece
        .iter()
        .map(|c| if *c == b'\n' || SPECIAL.contains(c) { 2 } else { 1 })
        .sum()
}

// uses of a piece, counted left to right without overlaps
fn count(text: &[u8], piece: &[u8]) -> usize {
    let mut uses = 0;
    let mut at = 0;
    while at + piece.len() <= text.len() {
        if &text[at..at + piece.len()] == piece {
            uses += 1;
            at += piece.len();
        } else {
            at += 1;
        }
    }
    uses
}

// candidates by their estimated saving, then by the piece
fn better(a: &(Vec<u8>, usize), b: &(Vec<u8>, usize)) -> std::cmp::Ordering {
    b.1.cmp(&a.1).then_with(|| a.0.cmp(&b.0))
}

fn main() {
    let mut text = Vec::new();
    io::stdin().read_to_end(&mut text).unwrap();
    text.retain(|&c| c != b'\r');
    let mut used = [false; 256];
    for &c in &text {
        used[c as usize] = true;
    }
    let mut free: Vec<u8> = (FIRST..=LAST)
        .filter(|c| !used[*c as usize] && !SPECIAL.contains(c))
        .collect();
    free.reverse();
    // the words of the text, with the space before them and without, as
    // (start, length) in the text; sorting them groups equal ones
    let mut spans: Vec<(usize, usize)> = Vec::new();
    let mut i = 0;
    while i < text.len() {
        if !text[i].is_ascii_alphabetic() {
            i += 1;
            continue;
        }
        let mut j = i;
        while j < text.len() && text[j].is_ascii_alphabetic() {
            j += 1;
        }
        if j - i >= 2 {
            if i > 0 && text[i - 1] == b' ' {
                spans.push((i - 1, j - i + 1));
            }
            spans.push((i, j - i));
        }
        i = j;
    }
    spans.sort_by(|a, b| text[a.0..a.0 + a.1].cmp(&text[b.0..b.0 + b.1]));
    let mut words: Vec<(Vec<u8>, usize)> = Vec::new();
    let mut i = 0;
    while i < spans.len() {
        let word = &text[spans[i].0..spans[i].0 + spans[i].1];
        let mut j = i;
        while j < spans.len() && &text[spans[j].0..spans[j].0 + spans[j].1] == word {
            j += 1;
        }
        words.push((word.to_vec(), (j - i) * (word.len() - 1)));
        i = j;
    }
    drop(spans);
    words.sort_by(better);
    words.truncate(WORDS);
    // a piece made only of characters of the text can never match a code
    let mut order: Vec<(Vec<u8>, usize)> = PIECES
        .iter()
        .map(|p| p.as_bytes())
        .filter(|p| p.iter().all(|c| used[*c as usize]))
        .map(|p| (p.to_vec(), count(&text, p) * (written_length(p) - 1)))
        .collect();
    for (word, estimate) in words {
        match order.iter_mut().find(|c| c.0 == word) {
            Some(c) => c.1 = c.1.max(estimate),
            None => order.push((word, estimate)),
        }
    }
    order.sort_by(better);
    let mut table: Vec<(u8, Vec<u8>)> = Vec::new();
    for (p, _) in order {
        let code = match free.last() {
            Some(&c) => c,
            None => break,
        };
        let written = written_length(&p);
        // every use saves the written length of the piece less one character
        if count(&text, &p) * (written - 1) <= LINE + written {
            continue;
        }
        // replace in place, left to right: the text only gets shorter
        let (mut read, mut write) = (0, 0);
        while read < text.len() {
            if text[read..].starts_with(&p) {
                text[write] = code;
                read += p.len();
            } else {
                text[write] = text[read];
                read += 1;
            }
            write += 1;
        }
        text.truncate(write);
        table.push((code, p));
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
        write_literal(&mut out, &piece);
        out.write_all(b"\";\n").unwrap();
    }
    out.write_all(
        b"    for (int k = 0; d[k]; k++)\n        for (const char *p = d[k]; *p; p++)\n            \
          if (t[(unsigned char)*p]) fputs(t[(unsigned char)*p], stdout);\n            \
          else putchar(*p);\n    return 0;\n}\n",
    )
    .unwrap();
}
