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

const MOD: u32 = 1000000007;
const BYTE_BITS: usize = 8;

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let n = number() as usize;
    let mut fib = vec![0_u32; n + 1];
    fib[1] = 1;
    for i in 2..=n {
        let value = fib[i - 1] + fib[i - 2];
        fib[i] = if value >= MOD { value - MOD } else { value };
    }
    let mut composite = vec![0_u8; (n / 2 + BYTE_BITS) / BYTE_BITS];
    let mut answer = 1_u64;
    let mut p = 2;
    while p <= n {
        let odd = p / 2;
        if p == 2 || composite[odd / BYTE_BITS] >> (odd % BYTE_BITS) & 1 == 0 {
            if p != 2 && p <= n / p {
                for multiple in (p * p..=n).step_by(2 * p) {
                    let index = multiple / 2;
                    composite[index / BYTE_BITS] |= 1_u8 << (index % BYTE_BITS);
                }
            }
            let mut exponent = 0_u64;
            let mut power = p;
            while power <= n {
                for k in (power..=n).step_by(power) {
                    exponent += fib[n - k + 1] as u64;
                }
                if power > n / p {
                    break;
                }
                power *= p;
            }
            answer = answer * (exponent % u64::from(MOD) + 1) % u64::from(MOD);
        }
        p += if p == 2 { 1 } else { 2 };
    }
    write_number(answer);
    // SAFETY: putchar accepts this ASCII newline without pointers.
    unsafe {
        putchar(b'\n' as i32);
    }
    0
}
