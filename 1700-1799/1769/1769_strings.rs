use std::io::{self, Read};

// the line has at most 10^5 pieces of each length, fewer than the 9 * 10^5
// numbers of six digits, so the answer has at most six digits
const DIGITS: usize = 6;
const LIMIT: usize = 1_000_000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let s = input.trim().as_bytes();
    let mut seen = vec![false; LIMIT + 1];
    for i in 0..s.len() {
        if s[i] == b'0' {
            continue;
        }
        let mut value = 0;
        for &c in &s[i..s.len().min(i + DIGITS)] {
            value = value * 10 + (c - b'0') as usize;
            seen[value] = true;
        }
    }
    let mut answer = 1;
    while seen[answer] {
        answer += 1;
    }
    println!("{}", answer);
}
