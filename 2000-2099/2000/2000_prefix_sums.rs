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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let count = number() as usize;
    // The total is at most one billion, so every prefix sum fits in u32.
    let mut prefix = Vec::with_capacity(count + 1);
    prefix.push(0u32);
    for _ in 0..count {
        prefix.push(*prefix.last().unwrap() + number() as u32);
    }
    let (first, second) = (number() as usize - 1, number() as usize - 1);
    let total = prefix[count];
    let score = if first == second {
        let own = prefix[first + 1] - prefix[first];
        own + prefix[first].max(total - prefix[first + 1])
    } else if first < second {
        prefix[(first + second) / 2 + 1]
    } else {
        total - prefix[(first + second + 1) / 2]
    };
    write_number(i64::from(score));
    write_byte(b' ');
    write_number(i64::from(total - score));
    write_byte(b'\n');

    0
}
