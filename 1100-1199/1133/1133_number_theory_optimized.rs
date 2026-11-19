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

fn read_number() -> Option<i64> {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    if byte < 0 {
        return None;
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
    Some(value)
}

fn number() -> i64 {
    read_number().unwrap()
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

// a prime above the 4e9 + 1 possible answers and below 2^32, so products fit
// in 64 bits; no Fibonacci number with index up to 2000 is divisible by it
const P: u64 = 4294967291;

fn reduce(v: i64) -> u64 {
    v.rem_euclid(P as i64) as u64
}

fn power(mut b: u64, mut e: u64) -> u64 {
    let mut r = 1;
    while e > 0 {
        if e % 2 == 1 {
            r = r * b % P;
        }
        b = b * b % P;
        e /= 2;
    }
    r
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (mut i, mut fi, mut j, mut fj, n) = (number(), number(), number(), number(), number());
    if i > j {
        std::mem::swap(&mut i, &mut j);
        std::mem::swap(&mut fi, &mut fj);
    }
    // F(j) = A F(i) + B F(i + 1), with A and B found by stepping coefficients
    let (mut a, mut b, mut na, mut nb) = (1u64, 0u64, 0u64, 1u64);
    for _ in i..j {
        let (sa, sb) = ((a + na) % P, (b + nb) % P);
        a = na;
        b = nb;
        na = sa;
        nb = sb;
    }
    let mut cur = reduce(fi);
    let mut next = (reduce(fj) + P - a * cur % P) % P * power(b, P - 2) % P;
    for _ in i..n {
        let s = (cur + next) % P;
        cur = next;
        next = s;
    }
    for _ in n..i {
        let prev = (next + P - cur) % P;
        next = cur;
        cur = prev;
    }
    let answer = if cur > P / 2 {
        cur as i64 - P as i64
    } else {
        cur as i64
    };
    write_number(answer);
    write_byte(b'\n');

    0
}
