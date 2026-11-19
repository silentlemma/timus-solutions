#![no_main]

const THREE_DIGIT_MINIMUM: u16 = 100;
const THREE_DIGITS: usize = 3;
const COLUMN_WIDTH: usize = 4;

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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const MAXIMUM: usize = 100;
    let (count, columns) = (number() as usize, number() as usize);
    let mut values = [0u16; MAXIMUM];
    for value in &mut values[..count] {
        *value = number() as u16;
    }
    let height = (count + columns - 1) / columns;
    for row in 0..height {
        for column in 0..columns {
            let at = column * height + row;
            if at >= count {
                break;
            }
            let value = values[at];
            let digits = if value >= THREE_DIGIT_MINIMUM {
                THREE_DIGITS
            } else if value >= 10 {
                2
            } else {
                1
            };
            for _ in digits..COLUMN_WIDTH {
                write_byte(b' ');
            }
            write_number(i64::from(value));
        }
        write_byte(b'\n');
    }
    0
}
