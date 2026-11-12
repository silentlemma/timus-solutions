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

const LIMIT: usize = 32768;
const MOD_FOUR: u32 = 4;
const MOD_EIGHT: u32 = 8;
const CLASS_THREE: u32 = 3;
const CLASS_FIVE: u32 = 5;
const NUMBER_DIGITS: usize = 5;

fn power(mut base: u32, mut exponent: u32, modulus: u32) -> u32 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 != 0 {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exponent >>= 1;
    }
    result
}

fn root(a: u32, p: u32, cache: &mut [u16; LIMIT]) -> u32 {
    if p == 2 {
        return 1;
    }
    if p % MOD_FOUR == CLASS_THREE {
        let r = power(a, (p + 1) / MOD_FOUR, p);
        return if r * r % p == a { r } else { 0 };
    }
    if p % MOD_EIGHT == CLASS_FIVE {
        let mut r = power(a, (p + CLASS_THREE) / MOD_EIGHT, p);
        if r * r % p != a {
            if cache[p as usize] == 0 {
                cache[p as usize] = power(2, (p - 1) / MOD_FOUR, p) as u16;
            }
            r = r * u32::from(cache[p as usize]) % p;
        }
        return if r * r % p == a { r } else { 0 };
    }
    let (mut q, mut s) = (p - 1, 0);
    while q & 1 == 0 {
        q >>= 1;
        s += 1;
    }
    // Initialize r²=a*t from a single modular exponentiation.
    let mut b = power(a, (q - 1) / 2, p);
    let mut r = a * b % p;
    let mut t = r * b % p;
    let mut c = 0;
    while t != 1 {
        let (mut i, mut square) = (0, t);
        while square != 1 && i < s {
            square = square * square % p;
            i += 1;
        }
        if i == s {
            return 0;
        }
        if c == 0 {
            if cache[p as usize] == 0 {
                let mut z = 2;
                while power(z, (p - 1) / 2, p) != p - 1 {
                    z += 1;
                }
                cache[p as usize] = power(z, q, p) as u16;
            }
            c = u32::from(cache[p as usize]);
        }
        b = c;
        for _ in 0..s - i - 1 {
            b = b * b % p;
        }
        c = b * b % p;
        r = r * b % p;
        t = t * c % p;
        s = i;
    }
    r
}

fn text(bytes: &[u8]) {
    for &c in bytes {
        // SAFETY: putchar takes a byte promoted to int, without pointers.
        unsafe {
            putchar(i32::from(c));
        }
    }
}

fn write_number(mut value: u32) {
    let mut digits = [0_u8; NUMBER_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (value % 10) as u8;
        value /= 10;
        if value == 0 {
            break;
        }
    }
    text(&digits[first..]);
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let count = number();
    let mut cache = [0_u16; LIMIT];
    for _ in 0..count {
        let (a, p) = (number() as u32, number() as u32);
        let r = root(a % p, p, &mut cache);
        if r == 0 {
            text(b"No root\n");
        } else if p == 2 {
            text(b"1\n");
        } else {
            write_number(r.min(p - r));
            text(b" ");
            write_number(r.max(p - r));
            text(b"\n");
        }
    }
    0
}
