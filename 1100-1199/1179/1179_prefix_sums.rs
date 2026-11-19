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
    const SMALLEST: usize = 2;
    const LARGEST: usize = 36;
    let mut differences = [0i64; LARGEST + 2];
    let mut previous = LARGEST;
    loop {
        let byte = read_byte();
        if byte < 0 {
            break;
        }
        let digit = match byte as u8 {
            b'0'..=b'9' => byte as usize - b'0' as usize,
            b'A'..=b'Z' => byte as usize - b'A' as usize + 10,
            _ => LARGEST,
        };
        // A new number starts exactly for bases digit < base <= previous.
        let low = SMALLEST.max(digit + 1);
        if low <= previous {
            differences[low] += 1;
            differences[previous + 1] -= 1;
        }
        previous = digit;
    }
    let (mut count, mut best, mut radix) = (0, -1, SMALLEST);
    for (base, &delta) in differences
        .iter()
        .enumerate()
        .take(LARGEST + 1)
        .skip(SMALLEST)
    {
        count += delta;
        if count > best {
            best = count;
            radix = base;
        }
    }
    write_number(radix as i64);
    write_byte(b' ');
    write_number(best);
    write_byte(b'\n');
    0
}
