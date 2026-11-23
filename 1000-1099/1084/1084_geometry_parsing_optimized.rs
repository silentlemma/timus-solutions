#![no_main]

use std::f64::consts::PI;
#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn printf(format: *const u8, ...) -> i32;
}

const SIDES: f64 = 4.0;

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let (a, r) = (f64::from(input.number()), f64::from(input.number()));
    let half = a / 2.0;
    let area = if r <= half {
        PI * r * r
    } else if r * r >= 2.0 * half * half {
        a * a
    } else {
        // the circle minus the four caps cut off by the sides
        let cap = r * r * (half / r).acos() - half * (r * r - half * half).sqrt();
        PI * r * r - SIDES * cap
    };
    // SAFETY: the NUL-terminated format expects the supplied promoted double.
    unsafe {
        printf(b"%.3f\n\0".as_ptr(), area);
    }
    0
}

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn system_read(fd: i32, buffer: *mut u8, length: u32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn system_read(fd: i32, buffer: *mut u8, length: usize) -> isize;
}

fn read_input(buffer: &mut [u8]) -> usize {
    // SAFETY: the writable slice stays live for the call, and its length is bounded by INPUT_SIZE.
    // Both CRT _read and POSIX read write no more than the supplied length.
    let count = unsafe {
        #[cfg(windows)]
        {
            system_read(0, buffer.as_mut_ptr(), buffer.len() as u32)
        }
        #[cfg(not(windows))]
        {
            system_read(0, buffer.as_mut_ptr(), buffer.len())
        }
    };
    if count > 0 {
        count as usize
    } else {
        0
    }
}

const INPUT_SIZE: usize = 256;

struct Input {
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl Input {
    fn new() -> Self {
        Self {
            bytes: [0; INPUT_SIZE],
            position: 0,
            length: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.position == self.length {
            self.length = read_input(&mut self.bytes);
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let value = self.bytes[self.position];
        self.position += 1;
        value
    }
    fn number(&mut self) -> i32 {
        let mut c = self.byte();
        while c != 0 && c <= b' ' {
            c = self.byte();
        }
        let sign = if c == b'-' {
            c = self.byte();
            -1
        } else {
            1
        };
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.byte();
        }
        sign * value
    }
}
