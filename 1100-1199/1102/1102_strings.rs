use std::io::{self, BufRead, Write};

const WORDS: [&[u8]; 6] = [b"out", b"output", b"puton", b"in", b"input", b"one"];

/// Read backwards the words never start one another, so at most one word
/// ends at each position and the line is cut greedily from its end.
fn dialogue(s: &[u8]) -> bool {
    let mut end = s.len();
    while end > 0 {
        match WORDS.iter().find(|w| s[..end].ends_with(w)) {
            Some(w) => end -= w.len(),
            None => return false,
        }
    }
    true
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().split(b'\n');
    let first = lines.next().unwrap().unwrap();
    let n: usize = String::from_utf8_lossy(&first).trim().parse().unwrap();
    let mut out = String::new();
    for _ in 0..n {
        let line = lines.next().unwrap().unwrap();
        let s: &[u8] = line.strip_suffix(b"\r").unwrap_or(&line);
        out.push_str(if dialogue(s) { "YES\n" } else { "NO\n" });
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
