#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn read_byte() -> i32 {
    // SAFETY: getchar has no pointer arguments and reads the standard stream.
    unsafe { getchar() }
}

fn number() -> i64 {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    let negative = byte == b'-' as i32;
    if negative || byte == b'+' as i32 {
        byte = read_byte();
    }
    let mut value = 0i64;
    while (b'0' as i32..=b'9' as i32).contains(&byte) {
        let digit = i64::from(byte - b'0' as i32);
        // Accumulating negatives directly also accepts i64::MIN.
        value = if negative {
            value * 10 - digit
        } else {
            value * 10 + digit
        };
        byte = read_byte();
    }
    value
}

fn write_byte(byte: u8) {
    // SAFETY: putchar accepts a byte promoted to int and has no pointers.
    unsafe {
        putchar(i32::from(byte));
    }
}

fn write_number(value: i64) {
    const DIGITS: usize = 20;
    let mut remaining = value.unsigned_abs();
    if value < 0 {
        write_byte(b'-');
    }
    let mut buffer = [0u8; DIGITS];
    let mut start = buffer.len();
    loop {
        start -= 1;
        buffer[start] = b'0' + (remaining % 10) as u8;
        remaining /= 10;
        if remaining == 0 {
            break;
        }
    }
    for &digit in &buffer[start..] {
        write_byte(digit);
    }
}

const BASE: u64 = 1_000_000_000;
const PERCENT: u64 = 100;

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn big(mut value: u128) -> Vec<u32> {
    let mut limbs = Vec::new();
    loop {
        limbs.push((value % u128::from(BASE)) as u32);
        value /= u128::from(BASE);
        if value == 0 {
            break;
        }
    }
    limbs
}

fn multiply(value: &mut Vec<u32>, factor: u64) {
    let mut carry = 0;
    for limb in value.iter_mut() {
        let next = u64::from(*limb) * factor + carry;
        *limb = (next % BASE) as u32;
        carry = next / BASE;
    }
    if carry != 0 {
        value.push(carry as u32);
    }
}

fn greater(a: &[u32], b: &[u32]) -> bool {
    if a.len() != b.len() {
        return a.len() > b.len();
    }
    a.iter().rev().cmp(b.iter().rev()) == std::cmp::Ordering::Greater
}

fn years(gold: u64, limit: u64, fee: u64) -> i64 {
    if gold <= limit {
        return 0;
    }
    let initial = gcd(gold, limit);
    let common = gcd(PERCENT - fee, PERCENT);
    let (numerator, denominator) = ((PERCENT - fee) / common, PERCENT / common);
    let (mut left, mut right) = (u128::from(gold / initial), u128::from(limit / initial));
    let mut years = 0;
    while left > right {
        match (
            left.checked_mul(u128::from(numerator)),
            right.checked_mul(u128::from(denominator)),
        ) {
            (Some(a), Some(b)) => {
                left = a;
                right = b;
                years += 1;
            }
            _ => {
                // Neither attempted product was assigned: promote both current values exactly.
                let (mut a, mut b) = (big(left), big(right));
                while greater(&a, &b) {
                    multiply(&mut a, numerator);
                    multiply(&mut b, denominator);
                    years += 1;
                }
                break;
            }
        }
    }
    years
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (gold, limit, fee) = (number() as u64, number() as u64, number() as u64);
    write_number(years(gold, limit, fee));
    write_byte(b'\n');
    0
}
