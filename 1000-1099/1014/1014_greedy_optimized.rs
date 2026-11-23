use std::io::{self, Read};

const BASE: u64 = 10;

fn smallest(mut n: u64) -> String {
    // a zero digit makes the product zero: 10 is the smallest such number
    if n == 0 {
        return BASE.to_string();
    }
    if n == 1 {
        return "1".to_string();
    }
    // the largest digits first give the fewest digits; then sort them up
    let mut digits = Vec::new();
    for d in (2..BASE).rev() {
        while n % d == 0 {
            digits.push(d);
            n /= d;
        }
    }
    if n != 1 {
        return "-1".to_string();
    }
    digits.iter().rev().map(|d| d.to_string()).collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    println!("{}", smallest(parse_integer(input.trim())));
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
