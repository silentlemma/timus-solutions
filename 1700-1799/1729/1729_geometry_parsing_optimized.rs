#![no_main]

use std::f64::consts::PI;
#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn printf(format: *const u8, ...) -> i32;
}

const SCALE: f64 = 1000.0;
const HALF_TURN: u32 = 180_000;

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let radius = input.fixed() as f64 / SCALE;
    let units = input.fixed() as u32;
    let full_chords = f64::from(HALF_TURN / units - 1);
    let remainder = f64::from(HALF_TURN % units);
    let radians_per_unit = PI / f64::from(HALF_TURN);
    let distance = radius
        * (1.0
            + 2.0
                * (full_chords * (f64::from(units) * radians_per_unit).sin()
                    + (remainder * radians_per_unit).sin()));
    // SAFETY: printf receives the double required by the NUL-terminated format.
    unsafe {
        printf(b"%.7f\n\0".as_ptr(), distance);
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
}

impl Input {
    fn fixed(&mut self) -> u64 {
        let mut byte = self.byte();
        while byte != 0 && byte <= b' ' {
            byte = self.byte();
        }
        let (mut value, mut fractional) = (0, None);
        while byte != 0 && byte > b' ' {
            if byte == b'.' {
                fractional = Some(0);
            } else if byte.is_ascii_digit() {
                value = value * 10 + u64::from(byte - b'0');
                if let Some(count) = &mut fractional {
                    *count += 1;
                }
            }
            byte = self.byte();
        }
        for _ in fractional.unwrap_or(0)..3 {
            value *= 10;
        }
        value
    }
}
