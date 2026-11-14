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
const INPUT_RADIX: u32 = 10;

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

    fn number(&mut self) -> Option<u32> {
        let mut byte = self.byte()?;
        while byte.is_ascii_whitespace() {
            byte = self.byte()?;
        }
        let mut value = 0;
        while byte.is_ascii_digit() {
            value = value * INPUT_RADIX + u32::from(byte - b'0');
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

const POSITIONS: usize = 31;
const MAX_ONES: usize = 20;
const DECIMAL: u32 = 10;
const OUTPUT_BYTES: usize = 11;

const fn pascal() -> [[u32; MAX_ONES + 1]; POSITIONS + 1] {
    let mut choose = [[0; MAX_ONES + 1]; POSITIONS + 1];
    let mut n = 0;
    while n <= POSITIONS {
        choose[n][0] = 1;
        let mut k = 1;
        while k <= n && k <= MAX_ONES {
            choose[n][k] = choose[n - 1][k - 1] + choose[n - 1][k];
            k += 1;
        }
        n += 1;
    }
    choose
}

static CHOOSE: [[u32; MAX_ONES + 1]; POSITIONS + 1] = pascal();

fn count_at_most(mut bound: u32, mut remaining: usize, base: u32) -> u32 {
    let mut place = 1;
    let mut lower_positions = 0;
    while place <= bound / base {
        place *= base;
        lower_positions += 1;
    }

    let mut count = 0;
    loop {
        let digit = bound / place;
        if digit > 1 {
            // Either 0 or 1 is smaller here, so all lower digits are free.
            return count + CHOOSE[lower_positions + 1][remaining];
        }
        if digit == 1 {
            count += CHOOSE[lower_positions][remaining];
            if remaining == 0 {
                return count;
            }
            remaining -= 1;
        }
        if place == 1 {
            return count + u32::from(remaining == 0);
        }
        bound %= place;
        place /= base;
        lower_positions -= 1;
    }
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut input = Input::new();
    let (Some(x), Some(y), Some(k), Some(base)) = (
        input.number(),
        input.number(),
        input.number(),
        input.number(),
    ) else {
        return 1;
    };
    let k = k as usize;
    let mut answer = count_at_most(y, k, base) - count_at_most(x - 1, k, base);
    let mut output = [0; OUTPUT_BYTES];
    let mut start = output.len() - 1;
    output[start] = b'\n';
    loop {
        start -= 1;
        output[start] = b'0' + (answer % DECIMAL) as u8;
        answer /= DECIMAL;
        if answer == 0 {
            break;
        }
    }
    send(&output[start..])
}
