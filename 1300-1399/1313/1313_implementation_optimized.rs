use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = parse_integer(it.next().unwrap());
    let grid: Vec<Vec<&str>> = (0..n).map(|_| it.by_ref().take(n).collect()).collect();
    // diagonal s holds the cells with row + column = s; each is read from
    // its lowest row up
    let mut out: Vec<&str> = Vec::with_capacity(n * n);
    for s in 0..2 * n - 1 {
        let lo = s.saturating_sub(n - 1);
        for i in (lo..=s.min(n - 1)).rev() {
            out.push(grid[i][s - i]);
        }
    }
    println!("{}", out.join(" "));
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
