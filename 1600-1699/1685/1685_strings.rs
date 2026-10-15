use std::io::{self, BufRead};

fn main() {
    let mut line = String::new();
    io::stdin().lock().read_line(&mut line).unwrap();
    let text = line.trim_end_matches(|c| c == '\r' || c == '\n').as_bytes();
    let n = text.len() as i64;
    let mut out = vec![b' '; text.len()];
    // the encoded text lists the middle of a range, then its left part,
    // then its right part: replay that order and put each letter back
    let mut stack = vec![(0i64, n - 1)];
    let mut at = 0;
    while let Some((lo, hi)) = stack.pop() {
        if lo > hi {
            continue;
        }
        let mid = (lo + hi) / 2;
        out[mid as usize] = text[at];
        at += 1;
        stack.push((mid + 1, hi));
        stack.push((lo, mid - 1));
    }
    println!("{}", String::from_utf8(out).unwrap());
}
