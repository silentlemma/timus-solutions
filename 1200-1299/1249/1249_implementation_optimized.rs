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

fn write_text(text: &[u8]) {
    for &byte in text {
        write_byte(byte);
    }
}

fn cell() -> u8 {
    let mut byte = read_byte();
    while byte != b'0' as i32 && byte != b'1' as i32 {
        byte = read_byte();
    }
    (byte - b'0' as i32) as u8
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const FORBIDDEN: u8 = 3;
    let (rows, columns) = (number() as usize, number() as usize);
    let mut previous = vec![0u8; columns];
    for row in 0..rows {
        let (mut upper_left, mut left) = (0, 0);
        for column in 0..columns {
            let upper = previous[column];
            let current = cell();
            if row > 0 && column > 0 && upper_left + upper + left + current == FORBIDDEN {
                write_text(b"No\n");
                return 0;
            }
            previous[column] = current;
            upper_left = upper;
            left = current;
        }
    }
    write_text(b"Yes\n");

    0
}
