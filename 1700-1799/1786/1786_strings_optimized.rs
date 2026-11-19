#![no_main]

const RING_SIZE: usize = 6;
const INITIAL_COST: i64 = 60;
const COINS_PER_OPERATION: i64 = 5;

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn read_byte() -> i32 {
    // SAFETY: getchar has no pointer arguments.
    unsafe { getchar() }
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
    const NAME: &[u8] = b"Sandro";
    let mut ring = [0u8; RING_SIZE];
    let (mut size, mut best) = (0usize, INITIAL_COST);
    loop {
        let byte = read_byte();
        if byte < 0 {
            break;
        }
        if !(byte as u8).is_ascii_alphabetic() {
            continue;
        }
        ring[size % NAME.len()] = byte as u8;
        size += 1;
        if size < NAME.len() {
            continue;
        }
        let mut cost = 0;
        for (offset, &letter) in NAME.iter().enumerate() {
            let current = ring[(size + offset) % NAME.len()];
            cost += COINS_PER_OPERATION
                * (i64::from(current.is_ascii_uppercase() != letter.is_ascii_uppercase())
                    + i64::from(!current.eq_ignore_ascii_case(&letter)));
        }
        best = best.min(cost);
    }
    write_number(best);
    write_byte(b'\n');
    0
}
