use std::collections::HashSet;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut lines = text.split('\n');
    let n: usize = parse_integer(lines.next().unwrap().trim());
    // a name is the whole line, spaces included; only the line end goes
    let names: Vec<&str> = lines.take(n).map(|l| l.trim_end_matches('\r')).collect();
    let distinct: HashSet<&str> = names.iter().copied().collect();
    println!("{}", names.len() - distinct.len());
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
