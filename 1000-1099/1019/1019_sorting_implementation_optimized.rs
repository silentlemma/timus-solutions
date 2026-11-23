#![no_main]

use std::io::{self, Read};

const END: i64 = 1_000_000_000;

fn solve_entry() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = parse_integer(tokens.next().unwrap());
    let mut paints = Vec::with_capacity(n);
    let mut xs = vec![0, END];
    for _ in 0..n {
        let a: i64 = parse_integer(tokens.next().unwrap());
        let b: i64 = parse_integer(tokens.next().unwrap());
        let c = tokens.next().unwrap().as_bytes()[0];
        paints.push((a, b, c));
        xs.push(a);
        xs.push(b);
    }
    xs.sort_unstable();
    xs.dedup();
    let index = |x: i64| xs.binary_search(&x).unwrap();

    // piece i is [xs[i], xs[i + 1]); repaint the pieces of every segment
    let mut piece = vec![b'w'; xs.len() - 1];
    for &(a, b, c) in &paints {
        piece[index(a)..index(b)].fill(c);
    }

    // the longest run of white pieces; a strict comparison keeps the leftmost
    let (mut best_x, mut best_y) = (0, 0);
    let mut i = 0;
    while i < piece.len() {
        let mut j = i;
        while j < piece.len() && piece[j] == piece[i] {
            j += 1;
        }
        if piece[i] == b'w' && xs[j] - xs[i] > best_y - best_x {
            best_x = xs[i];
            best_y = xs[j];
        }
        i = j;
    }
    println!("{} {}", best_x, best_y);
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: &str) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_bytes();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
}

// Run the algorithm directly and flush Rust's global output before returning to C.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    solve_entry();
    std::io::Write::flush(&mut std::io::stdout()).unwrap();
    0
}
