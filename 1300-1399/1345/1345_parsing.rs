use std::io::{self, Read, Write};

const KEYWORDS: [&str; 35] = [
    "and",
    "array",
    "begin",
    "case",
    "class",
    "const",
    "div",
    "do",
    "else",
    "end",
    "for",
    "function",
    "if",
    "implementation",
    "interface",
    "mod",
    "not",
    "of",
    "or",
    "procedure",
    "program",
    "record",
    "repeat",
    "shl",
    "shr",
    "string",
    "then",
    "to",
    "type",
    "unit",
    "until",
    "uses",
    "var",
    "with",
    "while",
];

fn is_word(c: u8) -> bool {
    c.is_ascii_alphabetic() || c == b'_'
}

fn wrap(out: &mut Vec<u8>, kind: &str, part: &[u8]) {
    out.extend_from_slice(format!("<span class={}>", kind).as_bytes());
    out.extend_from_slice(part);
    out.extend_from_slice(b"</span>");
}

fn main() {
    let mut raw = Vec::new();
    io::stdin().read_to_end(&mut raw).unwrap();
    let mut text = Vec::with_capacity(raw.len());
    for k in 0..raw.len() {
        if !(raw[k] == b'\r' && raw.get(k + 1) == Some(&b'\n')) {
            text.push(raw[k]);
        }
    }
    let n = text.len();
    let find = |from: usize, target: u8| text[from..].iter().position(|&c| c == target);
    let mut out = Vec::with_capacity(2 * n);
    let mut i = 0;
    while i < n {
        let c = text[i];
        let mut j = i + 1;
        if c == b'{' {
            j = find(i, b'}').map_or(n, |k| i + k + 1);
            wrap(&mut out, "comment", &text[i..j]);
        } else if c == b'/' && text.get(i + 1) == Some(&b'/') {
            // the line break is not part of it
            j = find(i, b'\n').map_or(n, |k| i + k);
            wrap(&mut out, "comment", &text[i..j]);
        } else if c == b'\'' {
            j = find(i + 1, b'\'').map_or(n, |k| i + 1 + k + 1);
            wrap(&mut out, "string", &text[i..j]);
        } else if c == b'#' && text.get(i + 1).map_or(false, |d| d.is_ascii_digit()) {
            j = i + 1;
            while j < n && text[j].is_ascii_digit() {
                j += 1;
            }
            wrap(&mut out, "string", &text[i..j]);
        } else if c.is_ascii_digit() {
            j = i;
            while j < n && text[j].is_ascii_digit() {
                j += 1;
            }
            // one point is allowed, but only with digits after it
            if j + 1 < n && text[j] == b'.' && text[j + 1].is_ascii_digit() {
                j += 1;
                while j < n && text[j].is_ascii_digit() {
                    j += 1;
                }
            }
            wrap(&mut out, "number", &text[i..j]);
        } else if is_word(c) {
            j = i;
            while j < n && (is_word(text[j]) || text[j].is_ascii_digit()) {
                j += 1;
            }
            let word = String::from_utf8_lossy(&text[i..j]).to_ascii_lowercase();
            if KEYWORDS.contains(&word.as_str()) {
                wrap(&mut out, "keyword", &text[i..j]);
            } else {
                out.extend_from_slice(&text[i..j]);
            }
        } else {
            out.push(c);
        }
        i = j;
    }
    io::stdout().write_all(&out).unwrap();
}
