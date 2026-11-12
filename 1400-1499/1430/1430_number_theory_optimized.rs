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

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        let next = a % b;
        a = b;
        b = next;
    }
    a
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (mut a, mut b, n) = (number(), number(), number());
    let swapped = a < b;
    if swapped {
        std::mem::swap(&mut a, &mut b);
    }
    let divisor = gcd(a, b);
    let limit = (n / a).min(b / divisor - 1);
    let (step, mut remainder) = (a % b, n % b);
    let (mut best, mut bx, lower) = (remainder, 0, n % divisor);
    let mut x = 1;
    while x <= limit && best > lower {
        remainder = if remainder >= step {
            remainder - step
        } else {
            remainder + b - step
        };
        if remainder < best {
            best = remainder;
            bx = x;
        }
        x += 1;
    }
    let mut by = (n - bx * a) / b;
    if swapped {
        std::mem::swap(&mut bx, &mut by);
    }
    write_number(bx);
    // SAFETY: putchar accepts these ASCII bytes without pointers.
    unsafe {
        putchar(b' ' as i32);
    }
    write_number(by);
    // SAFETY: a newline is a valid unsigned character promoted to int.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
