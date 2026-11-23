use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| parse_integer(t))
        .collect();
    let (n, a) = (v[0], &v[1..=v[0]]);
    // n + 1 prefix sums modulo n take at most n values: two of them are
    // equal, and the numbers between them sum to a multiple of n
    let mut first = vec![usize::MAX; n];
    first[0] = 0;
    let mut sum = 0;
    for i in 1..=n {
        sum = (sum + a[i - 1]) % n;
        if first[sum] != usize::MAX {
            let part = &a[first[sum]..i];
            let mut out = String::new();
            writeln!(out, "{}", part.len()).unwrap();
            for x in part {
                writeln!(out, "{}", x).unwrap();
            }
            print!("{}", out);
            return;
        }
        first[sum] = i;
    }
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
