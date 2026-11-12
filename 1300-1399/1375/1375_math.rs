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

const FOUR: u64 = 4;

fn power(mut value: u64, mut exponent: u64, modulus: u64) -> u64 {
    let mut result = 1;
    while exponent != 0 {
        if exponent & 1 != 0 {
            result = result * value % modulus;
        }
        value = value * value % modulus;
        exponent /= 2;
    }
    result
}

fn solve(key: u64, p: u64) -> (u64, u64) {
    if p == 2 || key == 0 {
        return (key, 0);
    }
    if p % FOUR == 1 {
        let mut z = 2;
        while power(z, (p - 1) / 2, p) != p - 1 {
            z += 1;
        }
        let imaginary = power(z, (p - 1) / FOUR, p);
        let odd = if key % 2 == 0 { key + p } else { key };
        return (((odd + 1) / 2) % p, ((odd - 1) / 2) * imaginary % p);
    }
    for x in 0..=p / 2 {
        let residue = (key + p - x * x % p) % p;
        let y = power(residue, (p + 1) / FOUR, p);
        if y * y % p == residue {
            return (x, y);
        }
    }
    unreachable!()
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (key, p) = (number(), number());
    let (x, y) = solve(key, p);
    write_number(x);
    // SAFETY: putchar takes literal bytes promoted to int, without pointers.
    unsafe {
        putchar(b' ' as i32);
    }
    write_number(y);
    // SAFETY: putchar takes a newline byte promoted to int, without pointers.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
