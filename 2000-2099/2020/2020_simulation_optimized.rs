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
    const MAXIMUM: usize = 1000;
    fn word(buffer: &mut [u8; MAXIMUM]) -> usize {
        let mut byte = read_byte();
        while byte >= 0 && byte <= b' ' as i32 {
            byte = read_byte();
        }
        let mut size = 0;
        while byte > b' ' as i32 {
            buffer[size] = byte as u8;
            size += 1;
            byte = read_byte();
        }
        size
    }
    let (mut south, mut north) = ([0u8; MAXIMUM], [0u8; MAXIMUM]);
    let (n, m) = (word(&mut south), word(&mut north));
    let (mut i, mut j, mut elapsed) = (0, 0, 0);
    while i < n && j < m {
        let (a, b) = (south[i], north[j]);
        i += usize::from(a != b'L' || b == b'L');
        j += usize::from(b != b'L' || a == b'L');
        elapsed += 1;
    }
    write_number((elapsed + n - i + m - j) as i64);
    write_byte(b'\n');
    0
}
