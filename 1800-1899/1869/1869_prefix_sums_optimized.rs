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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const SEATS: i64 = 36;
    let count = number() as usize;
    let (mut east, mut west) = (vec![0i64; count], vec![0i64; count]);
    for from in 0..count {
        for to in 0..count {
            let people = number();
            if from < to {
                east[from] += people;
                east[to] -= people;
            }
            if from > to {
                west[to] += people;
                west[from] -= people;
            }
        }
    }
    let (mut load_east, mut load_west, mut peak) = (0, 0, 0);
    for at in 0..count {
        load_east += east[at];
        load_west += west[at];
        peak = peak.max(load_east).max(load_west);
    }
    write_number((peak + SEATS - 1) / SEATS);
    write_byte(b'\n');
    0
}
