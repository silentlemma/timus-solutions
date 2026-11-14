#![no_main]

use std::ffi::{c_int, c_void};

const STDIN: i32 = 0;
const STDOUT: i32 = 1;
const INPUT_SIZE: usize = 512;
const OUTPUT_SIZE: usize = 16;
const MAX_CARS: usize = 300;
const PER_METRE: u32 = 9;
const LANE_TIME: i32 = 72;
const CAR_LENGTH: u32 = 5;
const INTERVAL_WIDTH: i32 = LANE_TIME + (PER_METRE * CAR_LENGTH) as i32;
const UNITS_PER_SECOND: i32 = 50;
const FRACTION_SCALE: i32 = 1_000_000 / UNITS_PER_SECOND;
const FRACTION_DIGITS: usize = 6;
const DECIMAL: u32 = 10;

#[cfg(unix)]
extern "C" {
    fn read(fd: c_int, buffer: *mut c_void, len: usize) -> isize;
    fn write(fd: c_int, buffer: *const c_void, len: usize) -> isize;
}

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn read(fd: c_int, buffer: *mut c_void, count: u32) -> c_int;
    #[link_name = "_write"]
    fn write(fd: c_int, buffer: *const c_void, count: u32) -> c_int;
}

struct Input {
    buffer: [u8; INPUT_SIZE],
    cursor: usize,
    end: usize,
}

impl Input {
    fn byte(&mut self) -> Option<u8> {
        if self.cursor == self.end {
            // The destination is a live array of the requested length.
            let size = unsafe {
                read(
                    STDIN,
                    self.buffer.as_mut_ptr().cast(),
                    self.buffer.len() as _,
                )
            };
            if size <= 0 {
                return None;
            }
            self.cursor = 0;
            self.end = size as usize;
        }
        let byte = self.buffer[self.cursor];
        self.cursor += 1;
        Some(byte)
    }

    fn number(&mut self) -> Option<u32> {
        let mut byte = self.byte()?;
        while byte.is_ascii_whitespace() {
            byte = self.byte()?;
        }
        let mut value = 0;
        while byte.is_ascii_digit() {
            value = value * DECIMAL + u32::from(byte - b'0');
            byte = self.byte().unwrap_or(b' ');
        }
        Some(value)
    }
}

fn start_time(distance: u32, delay: i32) -> i32 {
    (PER_METRE * distance) as i32 - delay
}

fn earliest_start(input: &mut Input) -> Option<i32> {
    let mut first_lane = [0_u16; MAX_CARS];
    let count = input.number()? as usize;
    if count > MAX_CARS {
        return None;
    }
    for start in &mut first_lane[..count] {
        *start = input.number()? as u16;
    }

    let mut near = first_lane[..count]
        .iter()
        .map(|&d| start_time(u32::from(d), LANE_TIME))
        .peekable();
    let far_count = input.number()?;
    let mut wait = 0;
    // Merge each new far-lane interval with the stored near-lane intervals.
    for _ in 0..far_count {
        let start = start_time(input.number()?, 2 * LANE_TIME);
        while near.peek().is_some_and(|&next| next <= start) {
            let next = near.next().unwrap();
            if next >= wait {
                return Some(wait);
            }
            wait = wait.max(next + INTERVAL_WIDTH);
        }
        if start >= wait {
            return Some(wait);
        }
        wait = wait.max(start + INTERVAL_WIDTH);
    }
    for start in near {
        if start >= wait {
            break;
        }
        wait = wait.max(start + INTERVAL_WIDTH);
    }
    Some(wait)
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut input = Input {
        buffer: [0; INPUT_SIZE],
        cursor: 0,
        end: 0,
    };
    let Some(wait) = earliest_start(&mut input) else {
        return 1;
    };
    let mut seconds = wait / UNITS_PER_SECOND;
    let mut fraction = wait % UNITS_PER_SECOND * FRACTION_SCALE;
    let mut answer = [b'\n'; OUTPUT_SIZE];
    let mut first = OUTPUT_SIZE - 1;
    for _ in 0..FRACTION_DIGITS {
        first -= 1;
        answer[first] = b'0' + (fraction % DECIMAL as i32) as u8;
        fraction /= DECIMAL as i32;
    }
    first -= 1;
    answer[first] = b'.';
    loop {
        first -= 1;
        answer[first] = b'0' + (seconds % DECIMAL as i32) as u8;
        seconds /= DECIMAL as i32;
        if seconds == 0 {
            break;
        }
    }
    let bytes = &answer[first..];
    // The answer slice remains valid until the C runtime returns.
    if unsafe { write(STDOUT, bytes.as_ptr().cast(), bytes.len() as _) } as usize == bytes.len() {
        0
    } else {
        1
    }
}
