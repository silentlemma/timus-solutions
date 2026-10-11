use std::io::{self, Read, Write};

const WIDTH: usize = 40;

fn main() {
    let mut raw = Vec::new();
    io::stdin().read_to_end(&mut raw).unwrap();
    raw.retain(|&c| c != b'\r');
    let lines: Vec<&[u8]> = raw.split(|&c| c == b'\n').collect();
    let n: usize = String::from_utf8_lossy(lines[0]).trim().parse().unwrap();
    // a rule s1-s2 matches words ending in s1s2 and carries s2 over
    let rules: Vec<(Vec<u8>, usize)> = lines[1..=n]
        .iter()
        .map(|line| {
            let line: Vec<u8> = line
                .iter()
                .copied()
                .filter(|c| !c.is_ascii_whitespace())
                .collect();
            let dash = line.iter().position(|&c| c == b'-').unwrap();
            let pattern: Vec<u8> = line
                .iter()
                .filter(|&&c| c != b'-')
                .map(|c| c.to_ascii_lowercase())
                .collect();
            (pattern, line.len() - dash - 1)
        })
        .collect();
    let text = lines[n + 1..].join(&b'\n');
    let mut out = Vec::with_capacity(text.len() * 2);
    let mut col = 0;
    let mut i = 0;
    while i < text.len() {
        let c = text[i];
        if c == b'\n' {
            out.push(c);
            col = 0;
            i += 1;
            continue;
        }
        if !c.is_ascii_alphabetic() {
            // a full line moves a separator to the next one
            if col == WIDTH {
                out.push(b'\n');
                col = 0;
            }
            out.push(c);
            col += 1;
            i += 1;
            continue;
        }
        let start = i;
        while i < text.len() && text[i].is_ascii_alphabetic() {
            i += 1;
        }
        let word = &text[start..i];
        let len = word.len();
        if col + len <= WIDTH {
            out.extend_from_slice(word);
            col += len;
            continue;
        }
        // the shortest carried part whose head and '-' still fit
        let low = word.to_ascii_lowercase();
        let mut carry = rules
            .iter()
            .filter(|(pattern, cut)| low.ends_with(pattern) && col + len + 1 <= WIDTH + cut)
            .map(|&(_, cut)| cut)
            .min()
            .unwrap_or(0);
        if carry > 0 {
            out.extend_from_slice(&word[..len - carry]);
            out.extend_from_slice(b"-\n");
            out.extend_from_slice(&word[len - carry..]);
        } else {
            out.push(b'\n');
            out.extend_from_slice(word);
            carry = len;
        }
        col = carry;
    }
    io::stdout().write_all(&out).unwrap();
}
