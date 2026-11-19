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
    const MAX_SIDE: usize = 9;
    const LOW: u8 = 170;
    const HIGH: u8 = 200;
    const HEIGHTS: usize = (HIGH - LOW + 1) as usize;
    let side = number() as usize;
    let middle = side / 2;
    let mut frequencies = [0u8; HEIGHTS];
    for _ in 0..side * side {
        frequencies[(number() - i64::from(LOW)) as usize] += 1;
    }
    let mut grid = [0u8; MAX_SIDE * MAX_SIDE];
    let mut height = HEIGHTS - 1;
    // Enumerate centre-distance keys directly instead of sorting allocated cell tuples.
    for near in 0..=middle {
        for far in near..=middle {
            for row in 0..side {
                for column in 0..side {
                    let (a, b) = (row.abs_diff(middle), column.abs_diff(middle));
                    if a.min(b) == near && a.max(b) == far {
                        while frequencies[height] == 0 {
                            height -= 1;
                        }
                        grid[row * side + column] = LOW + height as u8;
                        frequencies[height] -= 1;
                    }
                }
            }
        }
    }
    for row in 0..side {
        for column in 0..side {
            if column != 0 {
                write_byte(b' ');
            }
            write_number(i64::from(grid[row * side + column]));
        }
        write_byte(b'\n');
    }

    0
}
