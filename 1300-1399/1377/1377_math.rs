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

fn index(rows: i64, columns: i64, row: i64, column: i64) -> i64 {
    let layer = row
        .min(column)
        .min(rows - 1 - row)
        .min(columns - 1 - column);
    let (height, width) = (rows - 2 * layer, columns - 2 * layer);
    let (r, c) = (row - layer, column - layer);
    let offset = if height == 1 {
        c
    } else if width == 1 {
        r
    } else if r == 0 {
        c
    } else if c == width - 1 {
        width - 1 + r
    } else if r == height - 1 {
        (width - 1) + (height - 1) + (width - 1) - c
    } else {
        2 * (height + width - 2) - r
    };
    rows * columns - height * width + offset
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (rows, columns) = (number(), number());
    let first = index(rows, columns, number() - 1, number() - 1);
    let second = index(rows, columns, number() - 1, number() - 1);
    write_number((first - second).abs());
    write_byte(b'\n');

    0
}
