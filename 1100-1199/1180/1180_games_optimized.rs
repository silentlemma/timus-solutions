#![no_main]

const DIVISOR: i32 = 3;

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
    let mut remainder = 0;
    loop {
        let byte = read_byte();
        if byte < 0 {
            break;
        }
        if (b'0' as i32..=b'9' as i32).contains(&byte) {
            remainder = (remainder * 10 + byte - b'0' as i32) % DIVISOR;
        }
    }
    if remainder == 0 {
        write_text(b"2\n");
    } else {
        write_text(b"1\n");
        write_number(i64::from(remainder));
        write_byte(b'\n');
    }
    0
}
