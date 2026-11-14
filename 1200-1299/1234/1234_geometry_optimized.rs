#![no_main]

use std::ffi::{c_int, c_void};

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const TENTHS: i64 = 10;
const SIDE_COUNT: usize = 5;
const BUFFER_SIZE: usize = 128;

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

fn read_sides() -> Option<[i64; SIDE_COUNT]> {
    let mut sides = [0; SIDE_COUNT];
    let mut buffer = [0u8; BUFFER_SIZE];
    let (mut index, mut whole, mut fraction) = (0, 0, 0);
    let (mut present, mut after_point) = (false, false);
    loop {
        // The call writes at most the size of the live input buffer.
        let size = unsafe { read(STDIN, buffer.as_mut_ptr().cast(), buffer.len() as _) };
        if size < 0 {
            return None;
        }
        let end = size == 0;
        let bytes = if end {
            &[b' '][..]
        } else {
            &buffer[..size as usize]
        };
        for &byte in bytes {
            match byte {
                byte @ b'0'..=b'9' => {
                    let digit = i64::from(byte - b'0');
                    if after_point {
                        fraction = digit;
                    } else {
                        whole = whole * TENTHS + digit;
                    }
                    present = true;
                }
                b'.' => after_point = true,
                _ if present => {
                    sides[index] = whole * TENTHS + fraction;
                    index += 1;
                    if index == SIDE_COUNT {
                        return Some(sides);
                    }
                    (whole, fraction, present, after_point) = (0, 0, false, false);
                }
                _ => {}
            }
        }
        if end {
            return None;
        }
    }
}

fn fits(q: i64, p: i64, b: i64, a: i64) -> bool {
    if q > b {
        return false;
    }
    if p <= a {
        return true;
    }
    let sum = (p + q).pow(2);
    let difference = (p - q).pow(2);
    (a + b).pow(2) * difference + (a - b).pow(2) * sum >= 2 * sum * difference
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let Some([x, y, z, a, b]) = read_sides() else {
        return 1;
    };
    let mut brick = [x, y, z];
    brick.sort_unstable();
    let answer: &[u8] = if fits(brick[0], brick[1], a.min(b), a.max(b)) {
        b"YES\n"
    } else {
        b"NO\n"
    };
    // The static answer bytes stay valid for the entire call.
    if unsafe { write(STDOUT, answer.as_ptr().cast(), answer.len() as _) } as usize == answer.len()
    {
        0
    } else {
        1
    }
}
