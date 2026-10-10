use std::io::{self, Read};

const BYTES: usize = 256;

// the text between quotes starting at p, with doubled quotes undone, and the
// index just past the closing quote
fn quoted(line: &[u8], mut p: usize) -> (Vec<u8>, usize) {
    let mut out = Vec::new();
    p += 1;
    while p < line.len() {
        if line[p] == b'\'' {
            if p + 1 < line.len() && line[p + 1] == b'\'' {
                out.push(b'\'');
                p += 2;
                continue;
            }
            return (out, p + 1);
        }
        out.push(line[p]);
        p += 1;
    }
    (out, p)
}

fn like(text: &[u8], pattern: &[u8]) -> bool {
    let (n, m) = (text.len(), pattern.len());
    // reach[i]: the pattern so far can match exactly the first i bytes
    let mut reach = vec![false; n + 1];
    reach[0] = true;
    let mut j = 0;
    while j < m {
        let c = pattern[j];
        let mut next = vec![false; n + 1];
        if c == b'%' {
            let mut seen = false;
            for i in 0..=n {
                seen = seen || reach[i];
                next[i] = seen;
            }
            j += 1;
        } else if c == b'[' {
            // a set of bytes, negated after ^, with ranges a-b unless b is ]
            let mut k = j + 1;
            let negated = k < m && pattern[k] == b'^';
            if negated {
                k += 1;
            }
            let mut accepted = [false; BYTES];
            while k < m && pattern[k] != b']' {
                let (lo, mut hi) = (pattern[k], pattern[k]);
                if k + 2 < m && pattern[k + 1] == b'-' && pattern[k + 2] != b']' {
                    hi = pattern[k + 2];
                    k += 2;
                }
                for x in lo..=hi {
                    accepted[x as usize] = true;
                }
                k += 1;
            }
            if k == m {
                return false; // a [ with no closing ] never matches
            }
            for i in 0..n {
                next[i + 1] = reach[i] && accepted[text[i] as usize] != negated;
            }
            j = k + 1;
        } else {
            for i in 0..n {
                next[i + 1] = reach[i] && (c == b'_' || text[i] == c);
            }
            j += 1;
        }
        reach = next;
    }
    reach[n]
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut lines = input.split(|&b| b == b'\n');
    let first = String::from_utf8_lossy(lines.next().unwrap())
        .trim()
        .to_string();
    let n: usize = first.parse().unwrap();
    let mut out = String::new();
    for line in lines.take(n) {
        let line = line.strip_suffix(b"\r").unwrap_or(line);
        let start = line.iter().position(|&b| b == b'\'').unwrap();
        let (text, p) = quoted(line, start);
        let second = p + line[p..].iter().position(|&b| b == b'\'').unwrap();
        let (pattern, _) = quoted(line, second);
        out += if like(&text, &pattern) {
            "YES\n"
        } else {
            "NO\n"
        };
    }
    print!("{}", out);
}
