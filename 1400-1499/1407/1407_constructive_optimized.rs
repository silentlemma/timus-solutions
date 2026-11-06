use std::io::{self, Read, Write};

const MAX_DIGITS: usize = 100;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let first = input.find(|byte| byte.is_ascii_digit()).unwrap();
    let mut n = usize::from(first - b'0');
    for digit in input.take_while(u8::is_ascii_digit) {
        n = 10 * n + usize::from(digit - b'0');
    }
    let mut answer = [b'\n'; MAX_DIGITS + 1];
    let (mut value, mut power) = (0u128, 1u128);
    for k in 0..n {
        // The lower k bits are already zero, so only bit k chooses the digit.
        value = value.wrapping_add(power);
        let digit = if (value >> k) & 1 == 0 {
            b'1'
        } else {
            value = value.wrapping_add(power);
            b'2'
        };
        answer[n - k - 1] = digit;
        power = power.wrapping_mul(10);
    }
    io::stdout().lock().write_all(&answer[..=n])
}
