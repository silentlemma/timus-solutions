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

const TENTHS_PER_MINUTE: u32 = 600;
const TENTHS_PER_SECOND: u32 = 10;
const START_GAP: u32 = 300;
struct Finish {
    at: u32,
    run: u32,
    name: Vec<u8>,
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let count = number() as u32;
    let mut finishes = Vec::with_capacity(count as usize);
    for position in 0..count {
        let name = word();
        let run = number() as u32 * TENTHS_PER_MINUTE
            + number() as u32 * TENTHS_PER_SECOND
            + number() as u32;
        finishes.push(Finish {
            at: position * START_GAP + run,
            run,
            name,
        });
    }
    finishes.sort_unstable_by(|a, b| {
        (a.at, a.run, a.name.as_slice()).cmp(&(b.at, b.run, b.name.as_slice()))
    });
    let (mut best, mut leaders) = (u32::MAX, 0);
    // Compact record holders into a prefix without retaining a second output list.
    for index in 0..finishes.len() {
        if finishes[index].run < best {
            best = finishes[index].run;
            finishes.swap(leaders, index);
            leaders += 1;
        }
    }
    finishes[..leaders].sort_unstable_by(|a, b| a.name.cmp(&b.name));
    write_number(leaders as i64);
    write_byte(b'\n');
    for entry in &finishes[..leaders] {
        write_text(&entry.name);
        write_byte(b'\n');
    }

    0
}
