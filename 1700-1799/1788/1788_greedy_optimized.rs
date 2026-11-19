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
    let (n, m) = (number() as usize, number() as usize);
    let mut girls = Vec::with_capacity(n);
    let mut boys = Vec::with_capacity(m);
    for _ in 0..n {
        girls.push(number());
    }
    for _ in 0..m {
        boys.push(number());
    }
    girls.sort_unstable();
    boys.sort_unstable();
    let mut left_girls: i64 = girls.iter().sum();
    let mut left_boys: i64 = boys.iter().sum();
    let mut best = left_girls;
    // Maintain both prefix sums instead of rescanning two slices for every k.
    for pairs in 1..=n.min(m) {
        left_girls -= girls[n - pairs];
        left_boys -= boys[m - pairs];
        best = best.min(left_girls + left_boys * pairs as i64);
    }
    write_number(best);
    write_byte(b'\n');
    0
}
