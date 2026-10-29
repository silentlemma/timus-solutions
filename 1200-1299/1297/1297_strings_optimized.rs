use std::io::{self, Read, Write};

const INPUT_CAPACITY: usize = 1024;

fn main() {
    // the letters are read and written as bytes, with no UTF-8 string between
    let mut input = Vec::with_capacity(INPUT_CAPACITY);
    io::stdin().read_to_end(&mut input).unwrap();
    let s = input
        .split(|ch| ch.is_ascii_whitespace())
        .find(|part| !part.is_empty())
        .unwrap_or(&[]);
    let n = s.len() as i64;
    let (mut best_start, mut best_len) = (0i64, 0i64);
    // every letter and every gap between two letters is a centre, 2n - 1 in all, and
    // each is expanded as far as it goes; ties keep the leftmost start
    for centre in 0..(2 * n - 1).max(0) {
        let (mut lo, mut hi) = (centre / 2, (centre + 1) / 2);
        while lo >= 0 && hi < n && s[lo as usize] == s[hi as usize] {
            lo -= 1;
            hi += 1;
        }
        let (length, start) = (hi - lo - 1, lo + 1);
        if length > best_len || (length == best_len && start < best_start) {
            best_start = start;
            best_len = length;
        }
    }
    let answer = &s[best_start as usize..(best_start + best_len) as usize];
    let stdout = io::stdout();
    let mut output = stdout.lock();
    output.write_all(answer).unwrap();
    output.write_all(b"\n").unwrap();
}
