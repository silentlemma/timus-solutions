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
    let (words, modulus) = (number() as usize, number() as u64);
    if words < 2 {
        write_text(b"0\n");
        return 0;
    }
    let top = words / 2;
    let half = top / 2;
    let capacity = half / 2 + 1;
    let mut ring = vec![0u32; capacity];
    let mut current = 1 % modulus;
    if half >= 1 {
        ring[1 % capacity] = current as u32;
    }
    let (mut read_at, mut write_at) = (1 % capacity, 2 % capacity);
    for index in 2..=top {
        current = (current + u64::from(ring[read_at])) % modulus;
        // g(j) is last read at 2j+1, before this slot can be reused.
        if index <= half {
            ring[write_at] = current as u32;
            write_at += 1;
            if write_at == capacity {
                write_at = 0;
            }
        }
        if index & 1 != 0 {
            read_at += 1;
            if read_at == capacity {
                read_at = 0;
            }
        }
    }
    write_number(current as i64);
    write_byte(b'\n');
    0
}
