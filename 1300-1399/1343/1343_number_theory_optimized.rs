#![no_main]

const DIGITS: usize = 12;
const ASCII_ZERO: i32 = b'0' as i32;
const ASCII_NINE: i32 = b'9' as i32;
const ASCII_SPACE: i32 = b' ' as i32;

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn byte() -> i32 {
    // SAFETY: getchar has no pointer arguments and reads the process's standard input.
    unsafe { getchar() }
}

fn digit() -> u64 {
    let mut c = byte();
    while c >= 0 && c <= ASCII_SPACE {
        c = byte();
    }
    (c - ASCII_ZERO) as u64
}

fn mulmod(a: u64, b: u64, n: u64) -> u64 {
    (a as u128 * b as u128 % n as u128) as u64
}

fn powmod(mut a: u64, mut exponent: u64, n: u64) -> u64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 != 0 {
            result = mulmod(result, a, n);
        }
        a = mulmod(a, a, n);
        exponent >>= 1;
    }
    result
}

fn is_prime(n: u64) -> bool {
    if n < 2 {
        return false;
    }
    const BASES: [u64; 6] = [2, 3, 5, 7, 11, 13];
    for prime in BASES {
        if n % prime == 0 {
            return n == prime;
        }
    }
    let twos = (n - 1).trailing_zeros();
    let odd = (n - 1) >> twos;
    // These six bases are deterministic below 3474749660383, above 10^12.
    for base in BASES {
        let mut value = powmod(base, odd, n);
        if value == 1 || value == n - 1 {
            continue;
        }
        for _ in 1..twos {
            value = mulmod(value, value, n);
            if value == n - 1 {
                break;
            }
        }
        if value != n - 1 {
            return false;
        }
    }
    true
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut count = digit() as usize;
    let c = byte();
    if (ASCII_ZERO..=ASCII_NINE).contains(&c) {
        count = count * 10 + (c - ASCII_ZERO) as usize;
    }
    let mut number = 0;
    for _ in 0..count {
        number = number * 10 + digit();
    }
    for _ in count..DIGITS {
        number *= 10;
    }
    if count < DIGITS {
        if number <= 2 {
            number = 2;
        } else {
            number |= 1;
            while !is_prime(number) {
                number += 2;
            }
        }
    }
    let mut output = [b'0'; DIGITS + 1];
    output[DIGITS] = b'\n';
    for index in (0..DIGITS).rev() {
        output[index] += (number % 10) as u8;
        number /= 10;
    }
    for character in output {
        // SAFETY: each value is an unsigned byte promoted to an int for putchar.
        unsafe { putchar(character as i32) };
    }
    0
}
