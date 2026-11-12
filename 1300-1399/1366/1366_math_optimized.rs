#![no_main]

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

const BASE: i64 = 1_000_000_000;
const MAX_LIMBS: usize = 334;
const FIRST_PAIR: u32 = 4;
const DECIMAL: u32 = 10;
const LIMB_DIGITS: usize = 9;

fn byte() -> i32 {
    // SAFETY: getchar reads standard input and takes no pointer arguments.
    unsafe { getchar() }
}

fn number() -> u32 {
    let zero = i32::from(b'0');
    let mut ch = byte();
    while ch >= 0 && ch <= i32::from(b' ') {
        ch = byte();
    }
    let mut value = 0;
    while (zero..=i32::from(b'9')).contains(&ch) {
        value = value * DECIMAL + (ch - zero) as u32;
        ch = byte();
    }
    value
}

fn write_byte(ch: u8) {
    // SAFETY: the byte is promoted to the int accepted by putchar.
    unsafe {
        putchar(i32::from(ch));
    }
}

fn write_limb(mut limb: u32, padded: bool) {
    let mut digits = [b'0'; LIMB_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] += (limb % DECIMAL) as u8;
        limb /= DECIMAL;
        if limb == 0 {
            break;
        }
    }
    let start = if padded { 0 } else { first };
    for &digit in &digits[start..] {
        write_byte(digit);
    }
}

fn scale(limbs: &mut [u32; MAX_LIMBS], used: &mut usize, factor: i64, offset: i64) {
    let mut carry = -offset;
    for limb in &mut limbs[..*used] {
        let value = i64::from(*limb) * factor + carry;
        *limb = (value % BASE) as u32;
        carry = value / BASE;
    }
    if carry != 0 {
        limbs[*used] = carry as u32;
        *used += 1;
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let n = number();
    let mut limbs = [0_u32; MAX_LIMBS];
    let mut used = 1;
    limbs[0] = u32::from(n > 1);
    for k in (FIRST_PAIR..=n).step_by(2) {
        scale(
            &mut limbs,
            &mut used,
            i64::from(k * (k - 1)),
            i64::from(k - 1),
        );
    }
    if n > 1 && n % 2 != 0 {
        scale(&mut limbs, &mut used, i64::from(n), 1);
    }

    let (leading, rest) = limbs[..used].split_last().unwrap();
    write_limb(*leading, false);
    for &limb in rest.iter().rev() {
        write_limb(limb, true);
    }
    write_byte(b'\n');
    0
}
