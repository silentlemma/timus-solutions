#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn byte() -> i32 {
    // SAFETY: getchar reads standard input and has no pointer arguments.
    unsafe { getchar() }
}

fn number() -> i64 {
    const SPACE: i32 = b' ' as i32;
    const ZERO: i32 = b'0' as i32;
    const NINE: i32 = b'9' as i32;
    let mut c = byte();
    while c >= 0 && c <= SPACE {
        c = byte();
    }
    let negative = c == b'-' as i32;
    if negative {
        c = byte();
    }
    let mut n = 0;
    while (ZERO..=NINE).contains(&c) {
        n = n * 10 + (c - ZERO) as u64;
        c = byte();
    }
    if negative {
        -(n as i64)
    } else {
        n as i64
    }
}

fn write_number(mut n: u64) {
    const MAX_DIGITS: usize = 20;
    let mut digits = [0_u8; MAX_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (n % 10) as u8;
        n /= 10;
        if n == 0 {
            break;
        }
    }
    for &digit in &digits[first..] {
        // SAFETY: putchar accepts the byte promoted to int, with no pointers.
        unsafe {
            putchar(digit as i32);
        }
    }
}

const STEP_SCALE: i64 = 12;
const CENTER_SCALE: i64 = 6;
const FIRST_SCALE: i64 = 4;
const DECIMAL_SCALE: i64 = 1000000000;
const DECIMAL_DIGITS: usize = 9;

fn write_byte(c: u8) {
    // SAFETY: putchar accepts this ASCII byte without pointers.
    unsafe {
        putchar(c as i32);
    }
}

fn write_fraction(mut numerator: i64, denominator: i64) {
    if numerator < 0 {
        write_byte(b'-');
        numerator = -numerator;
    }
    let (mut whole, mut remainder, mut fraction) =
        (numerator / denominator, numerator % denominator, 0);
    for _ in 0..DECIMAL_DIGITS {
        remainder *= 10;
        fraction = fraction * 10 + remainder / denominator;
        remainder %= denominator;
    }
    if 2 * remainder >= denominator {
        fraction += 1;
        if fraction == DECIMAL_SCALE {
            fraction = 0;
            whole += 1;
        }
    }
    write_number(whole as u64);
    write_byte(b'.');
    let mut power = DECIMAL_SCALE / 10;
    while power != 0 {
        write_byte(b'0' + (fraction / power % 10) as u8);
        power /= 10;
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let n = number();
    let (mut sum, mut weighted) = (0, 0);
    for i in 0..n {
        let value = number();
        sum += value;
        weighted += i * value;
    }
    write_fraction(
        (FIRST_SCALE * n - 2) * sum - CENTER_SCALE * weighted,
        n * (n + 1),
    );
    write_byte(b' ');
    write_fraction(
        STEP_SCALE * weighted - CENTER_SCALE * (n - 1) * sum,
        n * (n * n - 1),
    );
    write_byte(b'\n');
    0
}
