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
    const SIDE: usize = 4;
    const TURNS: usize = 4;
    const HALF: usize = SIDE / 2;
    // A quadrant contains only four cells, so its white count fits in one byte.
    let mut counts = [0u8; TURNS];
    for row in 0..SIDE {
        for column in 0..SIDE {
            let mut quadrant = column / HALF;
            if row >= HALF {
                quadrant = TURNS - 1 - quadrant;
            }
            if number() == 1 {
                counts[quadrant] += 1;
            }
        }
    }
    let mut best = SIDE * SIDE;
    for target in 0..TURNS {
        let mut moves = 0;
        for (at, &count) in counts.iter().enumerate() {
            let distance = (at + TURNS - target) % TURNS;
            moves += usize::from(count) * distance.min(TURNS - distance);
        }
        best = best.min(moves);
    }
    write_number(best as i64);
    write_byte(b'\n');

    0
}
