use std::io::{self, Read};

const FIRST_ODD: u64 = 3; // the smallest divisor worth trying

/// Whether n is a product of an odd number of factors, each 2 or an odd
/// number above 1: n = 2^twos * rest with rest odd.
fn paid(mut n: u64) -> bool {
    let mut twos = 0;
    while n % 2 == 0 {
        n /= 2;
        twos += 1;
    }
    if n == 1 {
        return twos % 2 == 1;
    }
    if twos % 2 == 0 {
        return true; // rest as a single factor
    }
    // an odd count needs rest split into two factors, so not a prime
    let mut d = FIRST_ODD;
    while d * d <= n {
        if n % d == 0 {
            return true;
        }
        d += 2;
    }
    false
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<u64> = text
        .split_ascii_whitespace()
        .map(|w| parse_integer(w))
        .collect();
    let mut out = String::new();
    for &n in nums[1..].iter().take(nums[0] as usize) {
        out.push_str(if paid(n) { "YES\n" } else { "NO\n" });
    }
    print!("{}", out);
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
