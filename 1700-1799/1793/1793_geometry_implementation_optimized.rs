#![no_main]

use std::io::{self, Read};

fn solve_entry() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|x| parse_integer(x))
        .collect();
    let [a, b, d, r1, top1, r2, top2, h] = v[..] else {
        return;
    };
    // the widest part of a plate inside the borders, at height min(d, h),
    // scaled by h to stay in integers
    let low = d.min(h);
    let w1 = r1 * h + (top1 - r1) * low;
    let w2 = r2 * h + (top2 - r2) * low;
    let fits = 2 * w1.max(w2) <= a.min(b) * h;
    // the centres can be this far apart along each side, and the plates
    // must be at least top1 + top2 apart, where they are widest
    let (dx, dy, need) = (a * h - w1 - w2, b * h - w1 - w2, (top1 + top2) * h);
    let apart = dx * dx + dy * dy >= need * need;
    println!("{}", if fits && apart { "YES" } else { "NO" });
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
