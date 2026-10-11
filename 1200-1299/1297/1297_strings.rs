use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let s = input.lines().next().unwrap_or("").trim_end().as_bytes();
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
    println!("{}", String::from_utf8_lossy(answer));
}
