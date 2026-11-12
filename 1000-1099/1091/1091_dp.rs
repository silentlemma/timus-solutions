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
    const MAX_DIGITS: usize = 5;
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

const CAPACITY: u32 = 10000;
const MAX_S: usize = 50;

fn count(k: usize, s: usize) -> u32 {
    if k > s / 2 {
        return 0;
    }
    let mut choose = [0_u32; MAX_S / 2 + 1];
    let mut exact = [0_u32; MAX_S / 2 + 1];
    let mut coefficient = 1;
    choose[k] = coefficient;
    for m in k + 1..=s / 2 {
        coefficient = coefficient * m as u32 / (m - k) as u32;
        if coefficient >= CAPACITY {
            return CAPACITY;
        }
        choose[m] = coefficient;
    }
    let limit = s / k;
    let mut total = 0;
    for divisor in (2..=limit).rev() {
        let mut value = choose[s / divisor];
        for multiple in (2 * divisor..=limit).step_by(divisor) {
            value -= exact[multiple];
        }
        exact[divisor] = value;
        total += value;
        if total >= CAPACITY {
            return CAPACITY;
        }
    }
    total
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (k, s) = (number() as usize, number() as usize);
    write_number(u64::from(count(k, s)));
    // SAFETY: putchar takes the newline byte promoted to int, without pointers.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
