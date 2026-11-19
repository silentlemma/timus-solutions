#![no_main]

const LARGEST_RADIX: i32 = 36;

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn read_byte() -> i32 {
    // SAFETY: getchar has no pointer arguments and reads the standard stream.
    unsafe { getchar() }
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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (mut total, mut highest) = (0, 1);
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    while byte > b' ' as i32 {
        let digit = if byte >= b'A' as i32 {
            byte - b'A' as i32 + 10
        } else {
            byte - b'0' as i32
        };
        total += digit;
        highest = highest.max(digit);
        byte = read_byte();
    }
    for radix in highest + 1..=LARGEST_RADIX {
        if total % (radix - 1) == 0 {
            write_number(i64::from(radix));
            write_byte(b'\n');
            return 0;
        }
    }
    write_text(b"No solution.\n");
    0
}
