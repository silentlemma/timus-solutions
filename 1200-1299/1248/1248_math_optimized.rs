#![no_main]

use std::ffi::{c_int, c_void};

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const BUFFER_SIZE: usize = 1024;
const TOKEN_SIZE: usize = 64;
const OUTPUT_SIZE: usize = 32;
const DIGITS: usize = 19;
// a digit of any input sits at a power of ten from -SHIFT up to TOP - SHIFT
const SHIFT: i32 = 300;
const TOP: usize = 450;
const BASE: i32 = 10;
const HALF: i32 = 5;
const BLOCK_DIGITS: usize = 4;
const BLOCK_BASE: i32 = 10_000;
const BLOCKS: usize = (TOP + BLOCK_DIGITS - 1) / BLOCK_DIGITS;
const POWERS: [i32; BLOCK_DIGITS] = [1, 10, 100, 1000];

#[cfg(unix)]
extern "C" {
    fn read(fd: c_int, buffer: *mut c_void, length: usize) -> isize;
    fn write(fd: c_int, buffer: *const c_void, length: usize) -> isize;
}

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn read(fd: c_int, buffer: *mut c_void, count: u32) -> c_int;
    #[link_name = "_write"]
    fn write(fd: c_int, buffer: *const c_void, count: u32) -> c_int;
}

fn add(mut text: &str, sum: &mut [i32; BLOCKS]) {
    let exp = if let Some(e) = text.find(['e', 'E']) {
        let exp = text[e + 1..].parse::<i32>().unwrap();
        text = &text[..e];
        exp
    } else {
        0
    };
    let (sign, mantissa) = match text.as_bytes()[0] {
        b'-' => (-1, &text[1..]),
        b'+' => (1, &text[1..]),
        _ => (1, text),
    };
    let whole = mantissa.find('.').unwrap_or(mantissa.len()) as i32;
    let place = (SHIFT + whole - 1 + exp) as usize;
    let mut index = place / BLOCK_DIGITS;
    let mut weight = POWERS[place % BLOCK_DIGITS];
    let mut value = 0;
    for byte in mantissa.bytes().filter(|&byte| byte != b'.') {
        value += i32::from(byte - b'0') * weight;
        if weight == 1 {
            sum[index] += sign * value;
            value = 0;
            index -= 1;
            weight = BLOCK_BASE / BASE;
        } else {
            weight /= BASE;
        }
    }
    sum[index] += sign * value;
}

fn settle(sum: &mut [i32; BLOCKS]) -> i32 {
    let mut carry = 0;
    for digit in sum {
        carry += *digit;
        *digit = carry.rem_euclid(BLOCK_BASE);
        carry = (carry - *digit) / BLOCK_BASE;
    }
    carry
}

fn digit(sum: &[i32; BLOCKS], place: usize) -> i32 {
    sum[place / BLOCK_DIGITS] / POWERS[place % BLOCK_DIGITS] % BASE
}

fn read_sum() -> Option<[i32; BLOCKS]> {
    let mut input = [0u8; BUFFER_SIZE];
    let mut token = [0u8; TOKEN_SIZE];
    let mut used = 0;
    let mut remaining = None;
    let mut sum = [0; BLOCKS];
    loop {
        // The read is limited to the size of the live input buffer.
        let size = unsafe { read(STDIN, input.as_mut_ptr().cast(), input.len() as _) };
        if size < 0 {
            return None;
        }
        let eof = size == 0;
        let data = if eof {
            &[b' '][..]
        } else {
            &input[..size as usize]
        };
        for &byte in data {
            if !byte.is_ascii_whitespace() {
                *token.get_mut(used)? = byte;
                used += 1;
            } else if used != 0 {
                let text = std::str::from_utf8(&token[..used]).ok()?;
                let left = if let Some(count) = remaining {
                    add(text, &mut sum);
                    count - 1
                } else {
                    text.parse::<usize>().ok()?
                };
                if left == 0 {
                    return Some(sum);
                }
                remaining = Some(left);
                used = 0;
            }
        }
        if eof {
            return None;
        }
    }
}

fn write_answer(answer: &[u8]) -> c_int {
    // The output slice remains live throughout the call.
    if unsafe { write(STDOUT, answer.as_ptr().cast(), answer.len() as _) } as usize == answer.len()
    {
        0
    } else {
        1
    }
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let Some(original) = read_sum() else {
        return 1;
    };
    let mut sum = original;
    let mut output = [0u8; OUTPUT_SIZE];
    let mut cursor = 0;
    if settle(&mut sum) < 0 {
        for (settled, raw) in sum.iter_mut().zip(original) {
            *settled = -raw;
        }
        output[cursor] = b'-';
        cursor += 1;
        settle(&mut sum);
    }
    let mut top = match sum.iter().rposition(|&d| d != 0) {
        Some(t) => t * BLOCK_DIGITS + BLOCK_DIGITS - 1,
        None => return write_answer(b"0.000000000000000000e0\n"),
    };
    while digit(&sum, top) == 0 {
        top -= 1;
    }
    // keep 19 significant digits, rounding half up on the next one; kept[0]
    // takes a carry out of the first digit
    let mut kept = [0; DIGITS + 1];
    for k in 0..DIGITS {
        kept[k + 1] = if top >= k { digit(&sum, top - k) } else { 0 };
    }
    if top >= DIGITS && digit(&sum, top - DIGITS) >= HALF {
        let mut k = DIGITS;
        kept[k] += 1;
        while kept[k] == BASE {
            kept[k] = 0;
            k -= 1;
            kept[k] += 1;
        }
    }
    let (mut exponent, first) = (top as i32 - SHIFT, if kept[0] == 1 { 0 } else { 1 });
    if first == 0 {
        exponent += 1;
    }
    output[cursor] = b'0' + kept[first] as u8;
    output[cursor + 1] = b'.';
    cursor += 2;
    for &digit in &kept[first + 1..first + DIGITS] {
        output[cursor] = b'0' + digit as u8;
        cursor += 1;
    }
    output[cursor] = b'e';
    cursor += 1;
    if exponent < 0 {
        output[cursor] = b'-';
        cursor += 1;
        exponent = -exponent;
    }
    let start = cursor;
    loop {
        output[cursor] = b'0' + (exponent % BASE) as u8;
        cursor += 1;
        exponent /= BASE;
        if exponent == 0 {
            break;
        }
    }
    output[start..cursor].reverse();
    output[cursor] = b'\n';
    write_answer(&output[..=cursor])
}
