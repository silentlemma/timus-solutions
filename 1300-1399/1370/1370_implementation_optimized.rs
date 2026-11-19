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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const WINDOW: usize = 10;
    let count = number() as usize;
    let start = number() as usize % count;
    let mut visible = [0u8; WINDOW];
    for index in 0..count {
        let digit = number() as u8;
        // Only these ten offsets survive the rotation; other digits need no storage.
        let offset = (index + count - start) % count;
        if offset < WINDOW {
            visible[offset] = digit;
        }
    }
    for digit in visible {
        write_byte(b'0' + digit);
    }
    write_byte(b'\n');
    0
}
