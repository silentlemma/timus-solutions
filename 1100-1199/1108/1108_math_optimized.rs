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

const BASE: u64 = 10000;
const CHUNK: usize = 4;
fn next_term(value: &[u32], result: &mut Vec<u32>, scratch: &mut Vec<u64>) {
    scratch.clear();
    scratch.resize(2 * value.len() + 1, 0);
    for (i, &left) in value.iter().enumerate() {
        scratch[2 * i] += u64::from(left) * u64::from(left);
        for (j, &right) in value.iter().enumerate().skip(i + 1) {
            scratch[i + j] += 2 * u64::from(left) * u64::from(right);
        }
    }
    let mut carry = 0;
    result.clear();
    for &coefficient in scratch.iter() {
        let current = coefficient + carry;
        result.push((current % BASE) as u32);
        carry = current / BASE;
    }
    assert_eq!(carry, 0);
    let mut borrow = 0i64;
    for (i, digit) in result.iter_mut().enumerate() {
        let current = i64::from(*digit) - i64::from(value.get(i).copied().unwrap_or(0)) - borrow;
        borrow = i64::from(current < 0);
        *digit = (current + borrow * BASE as i64) as u32;
    }
    assert_eq!(borrow, 0);
    result[0] += 1;
    while result.len() > 1 && result.last() == Some(&0) {
        result.pop();
    }
}
fn print_chunk(mut value: u32) {
    let mut digits = [b'0'; CHUNK];
    for digit in digits.iter_mut().rev() {
        *digit += (value % 10) as u8;
        value /= 10;
    }
    for digit in digits {
        write_byte(digit);
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let count = number();
    let mut value = vec![2u32];
    let mut next = Vec::new();
    let mut scratch = Vec::new();
    for term in 0..count {
        write_number(i64::from(*value.last().unwrap()));
        for &chunk in value.iter().rev().skip(1) {
            print_chunk(chunk);
        }
        write_byte(b'\n');
        if term + 1 < count {
            next_term(&value, &mut next, &mut scratch);
            std::mem::swap(&mut value, &mut next);
        }
    }

    0
}
