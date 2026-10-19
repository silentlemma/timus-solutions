use std::io::{self, Read};

// page i open is bit i - 1 of a Gray code word: F1 flips bit 0, the other
// move flips the bit above the lowest set one; these are the reflected Gray
// code steps, so the states form one path ordered by the decoded word
fn rank(pages: &str) -> i64 {
    let mut gray = pages.bytes().rev().fold(0i64, |g, c| g * 2 + (c - b'0') as i64);
    let mut place = 0;
    while gray != 0 {
        place ^= gray;
        gray >>= 1;
    }
    place
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().skip(1);
    if let (Some(start), Some(goal)) = (it.next(), it.next()) {
        println!("{}", (rank(start) - rank(goal)).abs());
    }
}
