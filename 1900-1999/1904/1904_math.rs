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

const MAX_FOLDS: usize = 10;
const MAX_INTERVALS: usize = 1 << (MAX_FOLDS - 1);

#[derive(Clone, Copy)]
struct Interval {
    left: i16,
    right: i16,
}

fn append(output: &mut [Interval], used: &mut usize, left: i32, right: i32) {
    if *used != 0 && left <= output[*used - 1].right as i32 {
        if right > output[*used - 1].right as i32 {
            output[*used - 1].right = right as i16;
        }
    } else {
        assert!(*used < MAX_INTERVALS);
        output[*used] = Interval {
            left: left as i16,
            right: right as i16,
        };
        *used += 1;
    }
}

fn write_byte(c: u8) {
    // SAFETY: putchar accepts this ASCII byte without pointers.
    unsafe {
        putchar(c as i32);
    }
}

fn write_signed(mut value: i32) {
    if value < 0 {
        write_byte(b'-');
        value = -value;
    }
    write_number(value as u64);
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let k = number() as usize;
    let mut references = [0_i32; MAX_FOLDS];
    for a in &mut references[..k] {
        *a = number() as i32;
    }
    let mut first = [Interval { left: 0, right: 0 }; MAX_INTERVALS];
    let mut second = first;
    first[0] = Interval { left: 0, right: 1 };
    let (mut current, mut next) = (&mut first, &mut second);
    let mut count = 1;
    for &a in references[..k].iter().rev() {
        if count == 0 {
            break;
        }
        let (mut begin, mut used) = (0, 0);
        while begin < count && current[begin].right < 0 {
            begin += 1;
        }
        for interval in current[begin..count].iter().rev() {
            let left = i32::from(interval.left).max(0);
            append(next, &mut used, a - i32::from(interval.right), a - left);
        }
        for interval in &current[begin..count] {
            let left = i32::from(interval.left).max(0);
            append(next, &mut used, a + left, a + i32::from(interval.right));
        }
        count = used;
        std::mem::swap(&mut current, &mut next);
    }
    write_number(count as u64);
    write_byte(b'\n');
    for interval in &current[..count] {
        write_signed(interval.left as i32);
        write_byte(b' ');
        write_signed(interval.right as i32);
        write_byte(b'\n');
    }
    0
}
