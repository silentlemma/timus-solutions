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

const PREFECTURE_LIMIT: usize = 30;
fn word() -> [u8; PREFECTURE_LIMIT] {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    let mut result = [0u8; PREFECTURE_LIMIT];
    let mut size = 0;
    while byte > b' ' as i32 {
        result[size] = byte as u8;
        size += 1;
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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let rounds = number() as u32;
    let players = 1usize << rounds;
    let mut prefectures = Vec::with_capacity(players);
    for _ in 0..players {
        // Wrestler names do not affect the prefecture multiplicities.
        let mut byte = read_byte();
        while byte >= 0 && byte <= b' ' as i32 {
            byte = read_byte();
        }
        while byte > b' ' as i32 {
            byte = read_byte();
        }
        prefectures.push(word());
    }
    prefectures.sort_unstable();
    let (mut largest, mut run) = (1u16, 0u16);
    for index in 0..players {
        run = if index != 0 && prefectures[index] == prefectures[index - 1] {
            run + 1
        } else {
            1
        };
        largest = largest.max(run);
    }
    let unsafe_rounds = u16::BITS - (largest - 1).leading_zeros();
    write_number(i64::from(rounds - unsafe_rounds));
    write_byte(b'\n');
    0
}
