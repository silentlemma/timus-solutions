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

#[derive(Clone, Copy)]
struct Point {
    x: i16,
    y: i16,
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let count = number() as usize;
    let mut points = Vec::with_capacity(count);
    let (mut left, mut right, mut lower, mut upper) = (0, 0, 0, 0);
    for _ in 0..count {
        let (x, y) = (number() as i16, number() as i16);
        left = left.min(x);
        right = right.max(x);
        lower = lower.min(y);
        upper = upper.max(y);
        points.push(Point { x, y });
    }
    points.sort_unstable_by_key(|point| (-point.y, point.x));
    let mut at = 0;
    for y in (lower..=upper).rev() {
        for x in left..=right {
            let byte = if at < points.len() && points[at].x == x && points[at].y == y {
                at += 1;
                b'*'
            } else if x == 0 && y == 0 {
                b'+'
            } else if y == 0 {
                b'-'
            } else if x == 0 {
                b'|'
            } else {
                b'.'
            };
            write_byte(byte);
        }
        write_byte(b'\n');
    }

    0
}
