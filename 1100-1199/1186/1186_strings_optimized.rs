#![no_main]

use std::ffi::{c_int, c_void};

const STDIN: c_int = 0;
const STDOUT: c_int = 1;

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

const LETTERS: usize = 26;
const SYMBOLS: usize = LETTERS * (LETTERS + 1);
const DECIMAL: u32 = 10;
const MAX_DEPTH: usize = 50;

fn totals(formula: &[u8]) -> [u16; SYMBOLS] {
    let mut counts = [0; SYMBOLS];
    let mut parents = [1; MAX_DEPTH];
    for term in formula.split(|&c| c == b'+') {
        let mut depth = 0;
        let mut start = 0;
        let mut leading = 0;
        while term[start].is_ascii_digit() {
            leading = leading * DECIMAL + u32::from(term[start] - b'0');
            start += 1;
        }
        let mut product = if start == 0 { 1 } else { leading };
        let mut end = term.len();
        // Reading backwards gives each group's multiplier before its atoms.
        while end > start {
            let (mut count, mut place) = (0, 1);
            while term[end - 1].is_ascii_digit() {
                end -= 1;
                count += u32::from(term[end] - b'0') * place;
                place *= DECIMAL;
            }
            if place == 1 {
                count = 1;
            }
            end -= 1;
            match term[end] {
                b')' => {
                    parents[depth] = product;
                    depth += 1;
                    product *= count;
                }
                b'(' => {
                    depth -= 1;
                    product = parents[depth];
                }
                token => {
                    let suffix = if token.is_ascii_lowercase() {
                        end -= 1;
                        usize::from(token - b'a') + 1
                    } else {
                        0
                    };
                    let symbol = usize::from(term[end] - b'A') * (LETTERS + 1) + suffix;
                    counts[symbol] += (count * product) as u16;
                }
            }
        }
    }
    counts
}

const MAX_FORMULA: usize = 100;
const MAX_RIGHT_SIDES: usize = 10;
const CRLF: usize = 2;
const INPUT_CAPACITY: usize = (MAX_FORMULA + CRLF) * (MAX_RIGHT_SIDES + 1) + 2 + CRLF;
const LINE_CAPACITY: usize = 2 * MAX_FORMULA + 3;

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut input = [0u8; INPUT_CAPACITY];
    let mut len = 0;
    while len < input.len() {
        let remaining = &mut input[len..];
        // The pointer and length refer to the unwritten part of input.
        let count = unsafe { read(STDIN, remaining.as_mut_ptr().cast(), remaining.len() as _) };
        if count < 0 {
            return 1;
        }
        if count == 0 {
            break;
        }
        len += count as usize;
    }
    let mut tokens = input[..len]
        .split(|byte| byte.is_ascii_whitespace())
        .filter(|token| !token.is_empty());
    let left = tokens.next().unwrap();
    let expected = totals(left);
    let mut output = [0; MAX_RIGHT_SIDES * LINE_CAPACITY];
    let mut used = 0;
    for right in tokens.skip(1) {
        let sign = if totals(right) == expected {
            b"=="
        } else {
            b"!="
        };
        let sign_start = used + left.len();
        let right_start = sign_start + sign.len();
        let end = right_start + right.len();
        output[used..sign_start].copy_from_slice(left);
        output[sign_start..right_start].copy_from_slice(sign);
        output[right_start..end].copy_from_slice(right);
        output[end] = b'\n';
        used = end + 1;
    }
    let mut written = 0;
    while written < used {
        let remaining = &output[written..used];
        // The pointer and length refer to the remaining initialized output.
        let count = unsafe { write(STDOUT, remaining.as_ptr().cast(), remaining.len() as _) };
        if count <= 0 {
            return 1;
        }
        written += count as usize;
    }
    0
}
