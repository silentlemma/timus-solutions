use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| parse_integer::<i64>(t));
    let mut next = || it.next().unwrap();
    let (a, b, c) = (next(), next(), next());
    let (x, y, z) = (next(), next(), next());
    // the dual lands first cover what the red and blue lands miss, and every
    // land left over pays for the mana of any color
    let missing = (x - a).max(0) + (y - b).max(0);
    if missing <= c && a + b + c >= x + y + z {
        println!("It is a kind of magic");
    } else {
        println!("There are no miracles in life");
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
