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

fn write_text(text: &[u8]) {
    for &byte in text {
        write_byte(byte);
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const PIECES: usize = 5;
    let (size, x, y) = (number(), number(), number());
    let one_x = i64::from(x > 1) + i64::from(x < size);
    let one_y = i64::from(y > 1) + i64::from(y < size);
    let two_x = i64::from(x > 2) + i64::from(x + 2 <= size);
    let two_y = i64::from(y > 2) + i64::from(y + 2 <= size);
    // The one-step and two-step directions along the two axes are independent.
    let king = (one_x + 1) * (one_y + 1) - 1;
    let knight = one_x * two_y + two_x * one_y;
    let bishop = (x - 1).min(y - 1)
        + (x - 1).min(size - y)
        + (size - x).min(y - 1)
        + (size - x).min(size - y);
    let rook = 2 * (size - 1);
    let counts = [king, knight, bishop, rook, rook + bishop];
    let labels: [&[u8]; PIECES] = [b"King: ", b"Knight: ", b"Bishop: ", b"Rook: ", b"Queen: "];
    for index in 0..PIECES {
        write_text(labels[index]);
        write_number(counts[index]);
        write_byte(b'\n');
    }
    0
}
