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

#[no_mangle]
pub extern "C" fn main() -> i32 {
    const MOD: u32 = 1_000_000_009;
    const LOW: usize = 100;
    const HIGH: usize = 1000;
    const PAIRS: usize = 100;
    const BASE: usize = 10;
    const WINDOW: usize = 3;
    let length = number() as usize;
    let mut prime = [true; HIGH];
    prime[0] = false;
    prime[1] = false;
    let mut divisor = 2;
    while divisor * divisor < HIGH {
        if prime[divisor] {
            for multiple in (divisor * divisor..HIGH).step_by(divisor) {
                prime[multiple] = false;
            }
        }
        divisor += 1;
    }
    let mut transitions = [(0u8, 0u8); HIGH - LOW];
    let mut used = 0;
    let mut ways = [0u32; PAIRS];
    for value in LOW..HIGH {
        if prime[value] {
            transitions[used] = ((value / BASE) as u8, (value % PAIRS) as u8);
            used += 1;
            ways[value % PAIRS] += 1;
        }
    }
    // Every addition is below twice MOD, so u32 and one subtraction suffice.
    for _ in WINDOW..length {
        let mut next = [0u32; PAIRS];
        for &(from, to) in &transitions[..used] {
            let value = next[usize::from(to)] + ways[usize::from(from)];
            next[usize::from(to)] = if value >= MOD { value - MOD } else { value };
        }
        ways = next;
    }
    let answer = ways.iter().map(|&value| u64::from(value)).sum::<u64>() % u64::from(MOD);
    write_number(answer as i64);
    write_byte(b'\n');

    0
}
