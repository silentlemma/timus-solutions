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
    const DIGITS: usize = 9;
    const RADIX: usize = 10;
    const SUMS: usize = DIGITS * (RADIX - 1) + 1;
    let target = number() as usize;
    let mut ways = [0u32; SUMS];
    ways[0] = 1;
    for length in 1..=DIGITS {
        let mut next = [0u32; SUMS];
        let mut window = 0;
        for sum in 0..=length * (RADIX - 1) {
            window += ways[sum];
            if sum >= RADIX {
                window -= ways[sum - RADIX];
            }
            next[sum] = window;
        }
        ways = next;
    }
    write_number(i64::from(ways[target]) + i64::from(target == 1));
    write_byte(b'\n');
    0
}
