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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const MAXIMUM_LENGTH: usize = 43;
    let (length, mut rank) = (number() as usize, number() as u32);
    // For the stated length bound all Fibonacci counts fit in u32.
    let mut counts = [1u32; MAXIMUM_LENGTH + 1];
    counts[1] = 2;
    for size in 2..=length {
        counts[size] = counts[size - 1] + counts[size - 2];
    }
    if rank > counts[length] {
        write_text(b"-1\n");
        return 0;
    }
    let mut previous_one = false;
    for position in 0..length {
        let smaller = counts[length - position - 1];
        let one = !previous_one && rank > smaller;
        if one {
            rank -= smaller;
        }
        write_byte(b'0' + u8::from(one));
        previous_one = one;
    }
    write_byte(b'\n');

    0
}
