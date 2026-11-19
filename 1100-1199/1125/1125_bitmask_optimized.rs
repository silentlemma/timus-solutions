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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const SIDE: usize = 50;
    const SQUARED: usize = 2 * SIDE * SIDE;
    let (rows, columns) = (number() as usize, number() as usize);
    if columns == 0 || rows == 0 {
        for _ in 0..rows {
            write_byte(b'\n');
        }
        return 0;
    }
    let mut board = [[0u8; SIDE]; SIDE];
    for row in board.iter_mut().take(rows) {
        for cell in row.iter_mut().take(columns) {
            let mut byte = read_byte();
            while byte <= b' ' as i32 {
                byte = read_byte();
            }
            *cell = byte as u8;
        }
    }
    let mut odd = [0u64; SIDE];
    for mask in odd.iter_mut().take(rows) {
        for column in 0..columns {
            *mask |= (number() as u64 & 1) << column;
        }
    }
    let mut square = [false; SQUARED];
    let mut root = 0;
    while root * root < SQUARED {
        square[root * root] = true;
        root += 1;
    }
    for row in 0..rows {
        let mut flips = 0;
        for (other, &mask) in odd.iter().enumerate().take(rows) {
            let vertical = row.abs_diff(other);
            flips ^= mask;
            for horizontal in 1..columns {
                if square[vertical * vertical + horizontal * horizontal] {
                    flips ^= (mask << horizontal) ^ (mask >> horizontal);
                }
            }
        }
        for column in 0..columns {
            let byte = board[row][column]
                ^ if flips >> column & 1 == 1 {
                    b'B' ^ b'W'
                } else {
                    0
                };
            write_byte(byte);
        }
        write_byte(b'\n');
    }

    0
}
