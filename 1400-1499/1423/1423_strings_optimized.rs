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

fn word() -> Vec<u8> {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    let mut result = Vec::new();
    while byte > b' ' as i32 {
        result.push(byte as u8);
        byte = read_byte();
    }
    result
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
    let count = number() as usize;
    let (first, second) = (word(), word());
    let mut fail = vec![0u32; count];
    let mut matched = 0;
    for i in 1..count {
        while matched > 0 && second[i] != second[matched] {
            matched = fail[matched - 1] as usize;
        }
        if second[i] == second[matched] {
            matched += 1;
        }
        fail[i] = matched as u32;
    }
    matched = 0;
    // Chain the two slices instead of storing a doubled string; prefixes fit u32.
    for (i, &byte) in first.iter().chain(first.iter().take(count - 1)).enumerate() {
        while matched > 0 && byte != second[matched] {
            matched = fail[matched - 1] as usize;
        }
        if byte == second[matched] {
            matched += 1;
        }
        if matched == count {
            let start = i + 1 - count;
            write_number(((count - start) % count) as i64);
            write_byte(b'\n');
            return 0;
        }
    }
    write_text(b"-1\n");

    0
}
