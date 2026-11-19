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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const THREE: u32 = 3;
    const FOUR: u32 = 4;
    const BASE: u32 = 1_000_000_000;
    const LIMB_DIGITS: usize = 9;
    let count = number() as u32;
    if count < FOUR {
        write_number(i64::from(count));
        write_byte(b'\n');
        return 0;
    }
    let (mut threes, mut rest) = (count / THREE, count % THREE);
    if rest == 1 {
        threes -= 1;
        rest = FOUR;
    }
    // Nine decimal digits per limb replace the old one-digit representation.
    let mut limbs = vec![rest.max(1)];
    for _ in 0..threes {
        let mut carry = 0;
        for limb in &mut limbs {
            let value = *limb * THREE + carry;
            *limb = value % BASE;
            carry = value / BASE;
        }
        if carry != 0 {
            limbs.push(carry);
        }
    }
    write_number(i64::from(*limbs.last().unwrap()));
    for &limb in limbs[..limbs.len() - 1].iter().rev() {
        let mut digits = [b'0'; LIMB_DIGITS];
        let mut value = limb;
        for digit in digits.iter_mut().rev() {
            *digit += (value % 10) as u8;
            value /= 10;
        }
        for &digit in &digits {
            write_byte(digit);
        }
    }
    write_byte(b'\n');

    0
}
