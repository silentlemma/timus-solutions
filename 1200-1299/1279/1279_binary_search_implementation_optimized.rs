#![no_main]

use std::io::{self, Read};

fn solve_entry() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| parse_integer::<i64>(t));
    let (n, m, k) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    let heights: Vec<i64> = it.take((n * m) as usize).collect();
    // filling the lowest sections first raises every section to a level h
    // and some of them one higher, so the answer is the largest h whose
    // missing containers, the sum of h - height below h, fit into K
    let mut lo = *heights.iter().min().unwrap();
    let mut hi = lo + k;
    while lo < hi {
        let mid = (lo + hi + 1) / 2;
        let need: i64 = heights.iter().filter(|&&h| h < mid).map(|&h| mid - h).sum();
        if need <= k {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    println!("{}", lo);
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
