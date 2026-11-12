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

const FORBIDDEN_CHOICES: u64 = 3;

fn count(n: u64) -> (u64, u64) {
    if n % 2 != 0 {
        let size = (n - FORBIDDEN_CHOICES) / 2;
        return (if size >= 2 { n * size } else { 0 }, 0);
    }
    let half = n / 2;
    let first = half - 1;
    let second = half - 2;
    (
        half * ((if first >= 2 { first } else { 0 }) + (if second >= 2 { second } else { 0 })),
        half * (n - FORBIDDEN_CHOICES),
    )
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (parallel, perpendicular) = count(number());
    write_number(parallel);
    // SAFETY: putchar has no pointer arguments; both values are ASCII bytes.
    unsafe {
        putchar(b' ' as i32);
    }
    write_number(perpendicular);
    // SAFETY: the newline is a valid unsigned character promoted to int.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
