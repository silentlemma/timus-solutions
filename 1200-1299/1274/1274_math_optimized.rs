#![no_main]

use std::ffi::{c_int, c_void};

#[cfg(unix)]
extern "C" {
    fn read(fd: c_int, buffer: *mut c_void, count: usize) -> isize;
    fn write(fd: c_int, buffer: *const c_void, count: usize) -> isize;
}

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn read(fd: c_int, buffer: *mut c_void, count: u32) -> c_int;
    #[link_name = "_write"]
    fn write(fd: c_int, buffer: *const c_void, count: u32) -> c_int;
}

const DECIMAL: i64 = 10;
const OUTPUT_SIZE: usize = 64;

fn number(token: &[u8]) -> i64 {
    token
        .iter()
        .fold(0, |value, &digit| value * DECIMAL + i64::from(digit - b'0'))
}

fn fraction(line: &[u8]) -> (i64, i64) {
    let mut fields = line
        .split(|byte| byte.is_ascii_whitespace())
        .filter(|token| !token.is_empty());
    let first = fields.next().unwrap();
    let negative = first[0] == b'-';
    let first = if negative { &first[1..] } else { first };
    let (whole, part) = match fields.next() {
        Some(part) => (number(first), part),
        None => (0, first),
    };
    let (num, den) = match part.iter().position(|&byte| byte == b'/') {
        Some(slash) => {
            let den = number(&part[slash + 1..]);
            (whole * den + number(&part[..slash]), den)
        }
        None => (number(part), 1),
    };
    (if negative { -num } else { num }, den)
}

fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

// Fill a number from right to left so a single write emits the answer.
fn prepend(output: &mut [u8], mut start: usize, mut value: i64) -> usize {
    loop {
        start -= 1;
        output[start] = b'0' + (value % DECIMAL) as u8;
        value /= DECIMAL;
        if value == 0 {
            return start;
        }
    }
}

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const INPUT_SIZE: usize = 128;

fn read_into(block: &mut [u8]) -> Option<usize> {
    let mut filled = 0;
    while filled < block.len() {
        let slice = &mut block[filled..];
        // The unwritten part of the buffer can hold the requested bytes.
        let size = unsafe { read(STDIN, slice.as_mut_ptr().cast(), slice.len() as _) };
        if size < 0 {
            return None;
        }
        if size == 0 {
            break;
        }
        filled += size as usize;
    }
    Some(filled)
}

fn send(bytes: &[u8]) -> c_int {
    // The answer slice remains valid for the duration of the call.
    let written = unsafe { write(STDOUT, bytes.as_ptr().cast(), bytes.len() as _) };
    c_int::from(written as usize != bytes.len())
}

fn solve(data: &[u8]) -> c_int {
    let mut lines = data.split(|&byte| byte == b'\n');
    let (an, ad) = fraction(lines.next().unwrap());
    let operation = lines
        .next()
        .unwrap()
        .iter()
        .copied()
        .find(|byte| !byte.is_ascii_whitespace())
        .unwrap();
    let (bn, bd) = fraction(lines.next().unwrap());

    let (num, den) = match operation {
        b'+' => (an * bd + bn * ad, ad * bd),
        b'-' => (an * bd - bn * ad, ad * bd),
        b'*' => (an * bn, ad * bd),
        _ => (an * bd, ad * bn),
    };
    let negative = num != 0 && (num < 0) != (den < 0);
    let (num, den) = (num.abs(), den.abs());
    let unit = gcd(num, den);
    let (num, den) = (num / unit, den / unit);
    let (whole, rest) = (num / den, num % den);

    let mut output = [0; OUTPUT_SIZE];
    let mut start = output.len() - 1;
    output[start] = b'\n';
    if rest != 0 {
        start = prepend(&mut output, start, den) - 1;
        output[start] = b'/';
        start = prepend(&mut output, start, rest);
        if whole != 0 {
            start -= 1;
            output[start] = b' ';
        }
    }
    if rest == 0 || whole != 0 {
        start = prepend(&mut output, start, whole);
    }
    if negative {
        start -= 1;
        output[start] = b'-';
    }
    send(&output[start..])
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut block = [0; INPUT_SIZE];
    let Some(filled) = read_into(&mut block) else {
        return 1;
    };
    if filled < block.len() {
        return solve(&block[..filled]);
    }

    // Handle inputs padded with more whitespace than the stack buffer holds.
    let mut data = block.to_vec();
    loop {
        let Some(filled) = read_into(&mut block) else {
            return 1;
        };
        data.extend_from_slice(&block[..filled]);
        if filled < block.len() {
            return solve(&data);
        }
    }
}
