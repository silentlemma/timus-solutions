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

const YEAR_DAYS: u64 = 365;
const LEAP_PERIOD: u64 = 4;
const CENTURY: u64 = 100;
const LEAP_CENTURY: u64 = 400;
const FEBRUARY: usize = 2;
const BEFORE_MONTH: [u64; 12] = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];

fn day_number() -> u64 {
    let (day, month, year) = (number(), number() as usize, number());
    let previous = year - 1;
    let mut days = previous * YEAR_DAYS + previous / LEAP_PERIOD - previous / CENTURY
        + previous / LEAP_CENTURY;
    days += BEFORE_MONTH[month - 1] + day;
    if month > FEBRUARY
        && year % LEAP_PERIOD == 0
        && (year % CENTURY != 0 || year % LEAP_CENTURY == 0)
    {
        days += 1;
    }
    days
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let n = number();
    let (mut best, mut answer) = (0, 0);
    for id in 1..=n {
        let born = day_number();
        day_number();
        let died = day_number();
        let life = died - born + 1;
        if life > best {
            best = life;
            answer = id;
        }
    }
    write_number(answer);
    // SAFETY: putchar accepts this ASCII newline without any pointer arguments.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
