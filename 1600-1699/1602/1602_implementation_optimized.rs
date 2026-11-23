use std::io::{self, Read};

const HUNDRED: i64 = 100; // times are kept in hundredths of a second, exactly
const STAND: i64 = 15 * HUNDRED; // the lift stands this long on the first floor
const BOARD: i64 = 5 * HUNDRED; // getting into the lift
const DIGITS: usize = 2;

/// A number with at most two decimals, as an exact integer of hundredths.
fn hundredths(word: &str) -> i64 {
    let mut parts = word.splitn(2, '.');
    let whole: i64 = parse_integer(parts.next().unwrap());
    let frac = format!("{}00", parts.next().unwrap_or(""));
    whole * HUNDRED + parse_integer::<i64>(&frac[..DIGITS])
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let w: Vec<&str> = s.split_ascii_whitespace().collect();
    let (n, k, u, v) = match w[..] {
        [n, k, u, v] => (
            parse_integer::<i64>(n),
            parse_integer::<i64>(k),
            hundredths(u),
            hundredths(v),
        ),
        _ => return,
    };
    // walking all the way down needs no lift
    let (mut best_floor, mut best_time) = (1, (n - 1) * u);
    let ready = (k - 1) * v + STAND; // the lift may leave the first floor from then on
    for f in 2..=n {
        // Petya calls the lift on reaching floor f; it comes up, waits for
        // the boarding and goes down again
        let start = ready.max((n - f) * u);
        let total = start + (f - 1) * v + BOARD + (f - 1) * v;
        // a later floor means less walking, so ties go to it
        if total <= best_time {
            best_floor = f;
            best_time = total;
        }
    }
    println!("{}", best_floor);
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
