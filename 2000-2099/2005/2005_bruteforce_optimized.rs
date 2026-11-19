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
    const POINTS: usize = 5;
    const FIRST: usize = 1;
    const FORBIDDEN_LAST: usize = 2;
    const LAST: usize = 3;
    const END: usize = POINTS - 1;
    const MIDDLE_SUM: usize = FIRST + FORBIDDEN_LAST + LAST;
    let mut costs = [0i64; POINTS * POINTS];
    for value in &mut costs {
        *value = number();
    }
    let mut best = i64::MAX;
    let mut route = [0; POINTS];
    for a in FIRST..=LAST {
        for b in FIRST..=LAST {
            if a == b {
                continue;
            }
            let c = MIDDLE_SUM - a - b;
            if c == FORBIDDEN_LAST {
                continue;
            }
            let cost =
                costs[a] + costs[a * POINTS + b] + costs[b * POINTS + c] + costs[c * POINTS + END];
            if cost < best {
                best = cost;
                route = [0, a, b, c, END];
            }
        }
    }
    write_number(best);
    write_byte(b'\n');
    for (index, point) in route.iter().enumerate() {
        if index != 0 {
            write_byte(b' ');
        }
        write_number((point + 1) as i64);
    }
    write_byte(b'\n');

    0
}
