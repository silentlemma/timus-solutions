use std::io::{self, Read};

const BASE: u64 = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut n: u64 = parse_integer(input.trim());
    // balanced ternary: digits 1 go into the payment, digits -1 into the tip
    let (mut pay, mut tip, mut power) = (0u64, 0u64, 1u64);
    while n > 0 {
        if n % BASE == 1 {
            pay += power;
            n -= 1;
        } else if n % BASE == BASE - 1 {
            tip += power;
            n += 1;
        }
        n /= BASE;
        power *= BASE;
    }
    // no tip yet: add the smallest bill the payment lacks to both
    power = 1;
    while tip == 0 {
        if pay / power % BASE == 0 {
            pay += power;
            tip = power;
        }
        power *= BASE;
    }
    println!("{} {}", pay, tip);
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
