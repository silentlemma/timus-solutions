use std::collections::HashSet;
use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let input = input.replace('\r', "");
    let lines: Vec<&str> = input.split('\n').collect();
    let stop = lines.iter().position(|l| l.trim() == "#").unwrap();
    let known: HashSet<&str> = lines[..stop]
        .iter()
        .map(|l| l.trim())
        .filter(|w| !w.is_empty())
        .collect();
    let mut errors = 0;
    let mut fix = |word: &str| -> String {
        if known.contains(word) {
            return word.to_string();
        }
        // only a single wrong letter is corrected, never a missing or extra one
        for d in &known {
            if d.len() == word.len()
                && d.bytes().zip(word.bytes()).filter(|(a, b)| a != b).count() == 1
            {
                errors += 1;
                return d.to_string();
            }
        }
        word.to_string()
    };
    let mut text = lines[stop + 1..].join("\n");
    if !text.ends_with('\n') {
        text.push('\n');
    }
    let bytes = text.as_bytes();
    let mut out = String::new();
    let mut i = 0;
    while i < bytes.len() {
        if !bytes[i].is_ascii_lowercase() {
            out.push(bytes[i] as char);
            i += 1;
            continue;
        }
        let mut j = i;
        while j < bytes.len() && bytes[j].is_ascii_lowercase() {
            j += 1;
        }
        out.push_str(&fix(&text[i..j]));
        i = j;
    }
    out.push_str(&format!("{}\n", errors));
    io::stdout().write_all(out.as_bytes()).unwrap();
}
