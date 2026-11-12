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

fn number() -> u64 {
    const SPACE: i32 = b' ' as i32;
    const ZERO: i32 = b'0' as i32;
    const NINE: i32 = b'9' as i32;
    let mut c = byte();
    while c >= 0 && c <= SPACE {
        c = byte();
    }
    let mut n = 0;
    while (ZERO..=NINE).contains(&c) {
        n = n * 10 + (c - ZERO) as u64;
        c = byte();
    }
    n
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

const MAX_ROCKETS: usize = 400;
const MAX_INNER: usize = MAX_ROCKETS - 2;
const SECONDS: f64 = 10.0;
const DECIMAL_SCALE: u64 = 1000000000;

const ROUNDING: f64 = 0.5;

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let m = number() as usize - 2;
    let mut first = [0.0; MAX_INNER + 1];
    let mut second = [0.0; MAX_INNER + 1];
    first[0] = 1.0;
    second[0] = 1.0;
    let (mut previous, mut current) = (&mut first, &mut second);
    let mut volleys = 0.0;
    for round in 1..=m {
        volleys += 1.0 - previous[m];
        for size in 1..=m {
            if size <= round {
                current[size] = 1.0;
                continue;
            }
            let mut sum = 0.0;
            for left in 0..size / 2 {
                sum += 2.0 * previous[left] * previous[size - 1 - left];
            }
            if size % 2 != 0 {
                let middle = previous[size / 2];
                sum += middle * middle;
            }
            current[size] = sum / size as f64;
        }
        std::mem::swap(&mut previous, &mut current);
    }
    let scaled = (volleys * SECONDS * DECIMAL_SCALE as f64 + ROUNDING) as u64;
    write_number(scaled / DECIMAL_SCALE);
    // SAFETY: putchar accepts the ASCII decimal separator without pointers.
    unsafe {
        putchar(b'.' as i32);
    }
    let mut power = DECIMAL_SCALE / 10;
    while power != 0 {
        // SAFETY: the computed decimal digit is an unsigned ASCII byte.
        unsafe {
            putchar((b'0' + (scaled / power % 10) as u8) as i32);
        }
        power /= 10;
    }
    // SAFETY: putchar accepts this ASCII newline without pointers.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
