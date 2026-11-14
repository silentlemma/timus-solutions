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

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const INPUT_SIZE: usize = 64;
const DECIMAL: u64 = 10;
const DIGITS: usize = 5;
// Truncation at twelve decimals preserves the floor up to n = 100000.
const LOG_NUMERATOR: u64 = 301_029_995_663;
const SCALE: u64 = 1_000_000_000_000;

fn read_number() -> Option<u64> {
    let mut input = [0u8; INPUT_SIZE];
    let mut n = 0;
    let mut started = false;
    loop {
        // The C runtime receives a pointer to a live array of the requested size.
        let size = unsafe { read(STDIN, input.as_mut_ptr().cast(), input.len() as _) };
        if size < 0 {
            return None;
        }
        if size == 0 {
            return started.then_some(n);
        }
        for &byte in &input[..size as usize] {
            if byte.is_ascii_digit() {
                n = n * DECIMAL + u64::from(byte - b'0');
                started = true;
            } else if started {
                return Some(n);
            }
        }
    }
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let Some(n) = read_number() else {
        return 1;
    };
    let mut answer = (n & !1) * LOG_NUMERATOR / SCALE;
    let mut output = [b'\n'; DIGITS + 1];
    let mut start = DIGITS;
    loop {
        start -= 1;
        output[start] = b'0' + (answer % DECIMAL) as u8;
        answer /= DECIMAL;
        if answer == 0 {
            break;
        }
    }
    let answer = &output[start..];
    // This slice remains valid for the duration of the write.
    if unsafe { write(STDOUT, answer.as_ptr().cast(), answer.len() as _) } as usize == answer.len()
    {
        0
    } else {
        1
    }
}
