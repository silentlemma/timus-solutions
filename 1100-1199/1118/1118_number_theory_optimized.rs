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

const FIRST_ODD: i64 = 3;
fn prime(value: i64) -> bool {
    if value < 2 {
        return false;
    }
    if value % 2 == 0 {
        return value == 2;
    }
    let mut divisor = FIRST_ODD;
    while divisor <= value / divisor {
        if value % divisor == 0 {
            return false;
        }
        divisor += 2;
    }
    true
}
fn divisor_sum(value: i64) -> i64 {
    let mut sum = 0;
    let mut divisor = 1;
    while divisor <= value / divisor {
        if value % divisor == 0 {
            sum += divisor;
            if divisor != value / divisor {
                sum += value / divisor;
            }
        }
        divisor += 1;
    }
    sum
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (low, high) = (number(), number());
    if low == 1 {
        write_number(1);
        write_byte(b'\n');
        return 0;
    }
    for candidate in (low..=high).rev() {
        if prime(candidate) {
            // A composite's proper divisor sum is at least three.
            if FIRST_ODD * candidate > high {
                write_number(candidate);
                write_byte(b'\n');
                return 0;
            }
            break;
        }
    }
    let (mut best, mut best_sum) = (low, divisor_sum(low));
    for value in low + 1..=high {
        let sum = divisor_sum(value);
        if sum * best < best_sum * value {
            best = value;
            best_sum = sum;
        }
    }
    write_number(best);
    write_byte(b'\n');

    0
}
