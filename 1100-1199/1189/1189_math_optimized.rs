#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(c: i32) -> i32;
}

const BASE: i64 = 10;
const ELEVEN: i64 = 11;
const MAX_DIGITS: usize = 10;
const MAX_CANDIDATES: usize = 2 * MAX_DIGITS;

fn next() -> i32 {
    // SAFETY: getchar accesses only the process-owned standard input stream.
    unsafe { getchar() }
}

fn byte(value: u8) {
    // SAFETY: value is a valid unsigned character; putchar uses standard output.
    unsafe {
        putchar(i32::from(value));
    }
}

fn number(mut value: i64, width: usize) {
    let mut digits = [b'0'; MAX_DIGITS];
    let mut count = 0;
    loop {
        digits[count] = b'0' + (value % BASE) as u8;
        count += 1;
        value /= BASE;
        if value == 0 {
            break;
        }
    }
    for _ in count..width {
        byte(b'0');
    }
    for &digit in digits[..count].iter().rev() {
        byte(digit);
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut c = next();
    while c >= 0 && c <= i32::from(b' ') {
        c = next();
    }
    let mut n = 0;
    while (i32::from(b'0')..=i32::from(b'9')).contains(&c) {
        n = n * BASE + i64::from(c - i32::from(b'0'));
        c = next();
    }
    let mut found = [0_i64; MAX_CANDIDATES];
    let mut count = 0;
    let mut power = 1;
    while power <= n {
        for carry in 0..2 {
            let twice = n % power + carry * power;
            if twice % 2 != 0 || twice / 2 >= power {
                continue;
            }
            let tail = twice / 2;
            let q = (n - twice) / power;
            let (prefix, digit) = (q / ELEVEN, q % ELEVEN);
            let x = (prefix * BASE + digit) * power + tail;
            if digit >= BASE || x < BASE || (prefix == 0 && digit == 0) {
                continue;
            }
            let mut position = 0;
            while position < count && found[position] < x {
                position += 1;
            }
            if position < count && found[position] == x {
                continue;
            }
            // Two candidates per decimal place fit the fixed twenty-entry sorted set.
            found.copy_within(position..count, position + 1);
            found[position] = x;
            count += 1;
        }
        power *= BASE;
    }
    number(count as i64, 0);
    byte(b'\n');
    for &x in &found[..count] {
        number(x, 0);
        for &c in b" + " {
            byte(c);
        }
        let mut width = 0;
        let mut value = x / BASE;
        while value > 0 {
            width += 1;
            value /= BASE;
        }
        number(n - x, width);
        for &c in b" = " {
            byte(c);
        }
        number(n, 0);
        byte(b'\n');
    }
    0
}
