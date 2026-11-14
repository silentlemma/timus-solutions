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
const MAX_DISKS: usize = 50;
const DIGITS: usize = 16;
const INPUT_SIZE: usize = 128;
const DECIMAL: u64 = 10;
const PEG_SUM: u8 = b'A' + b'B' + b'C';

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut pegs = [0; MAX_DISKS];
    let mut input = [0u8; INPUT_SIZE];
    let mut count = 0;
    while count < MAX_DISKS {
        // The array accommodates all bytes requested from libc.
        let size = unsafe { read(STDIN, input.as_mut_ptr().cast(), input.len() as _) };
        if size < 0 {
            return 1;
        }
        if size == 0 {
            break;
        }
        for &byte in &input[..size as usize] {
            if (b'A'..=b'C').contains(&byte) {
                pegs[count] = byte;
                count += 1;
                if count == MAX_DISKS {
                    break;
                }
            }
        }
    }

    let mut source = b'A';
    let mut answer = 0;
    // Each target peg determines the next bit, from largest to smallest.
    for &target in pegs[..count].iter().rev() {
        answer <<= 1;
        if target != source {
            answer += 1;
            source = PEG_SUM - source - target;
        }
    }

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
