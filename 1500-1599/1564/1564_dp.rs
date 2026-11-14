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
const BUFFER_SIZE: usize = 128;
const INPUT_RADIX: u64 = 10;

struct Input {
    bytes: [u8; BUFFER_SIZE],
    start: usize,
    end: usize,
}

impl Input {
    fn new() -> Self {
        Self {
            bytes: [0; BUFFER_SIZE],
            start: 0,
            end: 0,
        }
    }

    fn byte(&mut self) -> Option<u8> {
        if self.start == self.end {
            // The runtime receives the pointer and size of the live buffer.
            let size = unsafe { read(STDIN, self.bytes.as_mut_ptr().cast(), BUFFER_SIZE as _) };
            if size <= 0 {
                return None;
            }
            self.start = 0;
            self.end = size as usize;
        }
        let byte = self.bytes[self.start];
        self.start += 1;
        Some(byte)
    }

    fn number(&mut self) -> Option<u64> {
        let mut byte = self.byte()?;
        while byte.is_ascii_whitespace() {
            byte = self.byte()?;
        }
        let mut value = 0;
        while byte.is_ascii_digit() {
            value = value * INPUT_RADIX + u64::from(byte - b'0');
            byte = self.byte().unwrap_or(b' ');
        }
        Some(value)
    }
}

fn send(bytes: &[u8]) -> c_int {
    // The answer slice remains initialized for the duration of the call.
    let written = unsafe { write(STDOUT, bytes.as_ptr().cast(), bytes.len() as _) };
    c_int::from(written as usize != bytes.len())
}

const DECIMAL: u64 = 10;
const PLACES: u32 = 18;
const OUTPUT_SIZE: usize = PLACES as usize + 1;

fn floor_for(mut target: u64) -> Option<u64> {
    let (mut floor, mut prefix_ones) = (0, 0);
    let mut width = DECIMAL.pow(PLACES - 1);
    for remaining in (0..PLACES).rev() {
        let fixed_cost = prefix_ones * width + u64::from(remaining) * (width / DECIMAL);
        let digit = if target <= fixed_cost {
            0
        } else if target <= 2 * fixed_cost + width {
            target -= fixed_cost;
            prefix_ones += 1;
            1
        } else {
            // Digits 2 through 9 all contribute the same number of ones.
            target -= 2 * fixed_cost + width;
            if fixed_cost == 0 {
                return None;
            }
            let skipped = (target - 1) / fixed_cost;
            target -= skipped * fixed_cost;
            2 + skipped
        };
        floor = DECIMAL * floor + digit;
        width /= DECIMAL;
    }
    (target == prefix_ones).then_some(floor)
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let Some(target) = Input::new().number() else {
        return 1;
    };
    let Some(mut floor) = floor_for(target) else {
        return send(b"Petr lies\n");
    };
    let mut digits = [0; OUTPUT_SIZE];
    let mut position = digits.len() - 1;
    digits[position] = b'\n';
    loop {
        position -= 1;
        digits[position] = b'0' + (floor % DECIMAL) as u8;
        floor /= DECIMAL;
        if floor == 0 {
            return send(&digits[position..]);
        }
    }
}
