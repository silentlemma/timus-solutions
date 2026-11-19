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

fn read_number() -> Option<i64> {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    if byte < 0 {
        return None;
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
    Some(value)
}

fn number() -> i64 {
    read_number().unwrap()
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

fn write_text(text: &[u8]) {
    for &byte in text {
        write_byte(byte);
    }
}

fn inverse(value: i64, modulus: i64) -> i64 {
    let (mut r0, mut r1, mut s0, mut s1) = (modulus, value % modulus, 0, 1);
    while r1 != 0 {
        let quotient = r0 / r1;
        (r0, r1) = (r1, r0 - quotient * r1);
        (s0, s1) = (s1, s0 - quotient * s1);
    }
    (s0 % modulus + modulus) % modulus
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const ROOT: usize = 31623;
    const FIRST_ODD: usize = 3;
    // Store only odd composite marks and two-byte prime values.
    let mut composite = [false; ROOT / 2 + 1];
    let mut primes = vec![2u16];
    for candidate in (FIRST_ODD..=ROOT).step_by(2) {
        if composite[candidate / 2] {
            continue;
        }
        primes.push(candidate as u16);
        for multiple in (candidate * candidate..=ROOT).step_by(2 * candidate) {
            composite[multiple / 2] = true;
        }
    }
    let count = number();
    for _ in 0..count {
        let value = number();
        let prime = i64::from(
            *primes
                .iter()
                .find(|&&prime| value % i64::from(prime) == 0)
                .unwrap(),
        );
        let other = value / prime;
        let first = other * inverse(other, prime) % value;
        let second = value + 1 - first;
        write_text(b"0 1 ");
        write_number(first.min(second));
        write_byte(b' ');
        write_number(first.max(second));
        write_byte(b'\n');
    }

    0
}
