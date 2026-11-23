use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| parse_integer::<i64>(t));
    let n = it.next().unwrap() as usize;
    // before[i] is the sum of the first i readings
    let mut before = vec![0i64; n + 1];
    for i in 1..=n {
        before[i] = before[i - 1] + it.next().unwrap();
    }
    let q = it.next().unwrap_or(0);
    let mut out = String::new();
    for _ in 0..q {
        let (i, j) = (it.next().unwrap() as usize, it.next().unwrap() as usize);
        writeln!(out, "{}", before[j] - before[i - 1]).unwrap();
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
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
