use std::io::{self, Read};

const BOOK: [u8; 3] = [b'd', b'h', b'u']; // letters in the order of the book

fn step(c: u8) -> i64 {
    match c {
        b'u' => 1,
        b'd' => -1,
        _ => 0,
    }
}

/// Can a garland at this height end at the ground in exactly `left` links?
/// On the ground a link must go up, above it horizontal links can pad.
fn finishes(height: i64, left: i64) -> bool {
    if height == 0 {
        left == 0 || left >= 2
    } else {
        left >= height
    }
}

/// Never below the ground, and no horizontal link on it.
fn allowed(c: u8, height: i64) -> bool {
    height + step(c) >= 0 && !(c == b'h' && height == 0)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let s = it.next().unwrap().as_bytes();
    let mut heights = vec![0i64; n + 1];
    for i in 0..n {
        heights[i + 1] = heights[i] + step(s[i]);
    }
    // the last link that can take a larger letter and still be finished
    for i in (0..n).rev() {
        for &c in BOOK.iter() {
            let rest = (n - i - 1) as i64;
            if c > s[i] && allowed(c, heights[i]) && finishes(heights[i] + step(c), rest) {
                let mut out = s[..i].to_vec();
                out.push(c);
                let mut height = heights[i] + step(c);
                // the rest is the smallest garland that still finishes
                for left in (1..=rest).rev() {
                    for &d in BOOK.iter() {
                        if allowed(d, height) && finishes(height + step(d), left - 1) {
                            out.push(d);
                            height += step(d);
                            break;
                        }
                    }
                }
                println!("{}", String::from_utf8(out).unwrap());
                return;
            }
        }
    }
    println!("No solution");
}
