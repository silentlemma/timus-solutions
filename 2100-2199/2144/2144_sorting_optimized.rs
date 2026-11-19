#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn read_byte() -> i32 {
    // SAFETY: getchar has no pointer arguments.
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

fn write_text(text: &[u8]) {
    for &byte in text {
        write_byte(byte);
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let count = number() as usize;
    let mut boxes = Vec::with_capacity(count);
    let mut okay = true;
    for _ in 0..count {
        let size = number();
        let first = number();
        let mut last = first;
        for _ in 1..size {
            let value = number();
            if value < last {
                okay = false;
            }
            last = value;
        }
        boxes.push((first, last));
    }
    boxes.sort_unstable();
    if boxes.windows(2).any(|pair| pair[0].1 > pair[1].0) {
        okay = false;
    }
    write_text(if okay { b"YES\n" } else { b"NO\n" });
    0
}
