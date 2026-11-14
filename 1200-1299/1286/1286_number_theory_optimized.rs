#![no_main]

use std::ffi::{c_int, c_void};

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const BUFFER_SIZE: usize = 128;
const DECIMAL: i64 = 10;
const FIELDS: usize = 6;

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

fn read_values() -> Option<[i64; FIELDS]> {
    let mut values = [0; FIELDS];
    let mut buffer = [0u8; BUFFER_SIZE];
    let (mut index, mut value, mut sign, mut started) = (0, 0, 1, false);
    loop {
        // The C call receives the length of the live stack buffer.
        let size = unsafe { read(STDIN, buffer.as_mut_ptr().cast(), buffer.len() as _) };
        if size < 0 {
            return None;
        }
        let end = size == 0;
        let chunk = if end {
            &[b' '][..]
        } else {
            &buffer[..size as usize]
        };
        for &byte in chunk {
            match byte {
                b'0'..=b'9' => {
                    value = value * DECIMAL + i64::from(byte - b'0');
                    started = true;
                }
                b'-' => sign = -1,
                _ if started => {
                    values[index] = sign * value;
                    index += 1;
                    if index == FIELDS {
                        return Some(values);
                    }
                    (value, sign, started) = (0, 1, false);
                }
                _ => {}
            }
        }
        if end {
            return None;
        }
    }
}

fn binary_gcd(mut a: u32, mut b: u32) -> u32 {
    if a == 0 || b == 0 {
        return a | b;
    }
    let common = (a | b).trailing_zeros();
    a >>= a.trailing_zeros();
    while b != 0 {
        b >>= b.trailing_zeros();
        if a > b {
            std::mem::swap(&mut a, &mut b);
        }
        b -= a;
    }
    a << common
}

fn reachable(p: i64, q: i64, dx: i64, dy: i64) -> bool {
    let (p, q) = (p.unsigned_abs() as u32, q.unsigned_abs() as u32);
    let g = i64::from(binary_gcd(p, q));
    if g == 0 {
        return dx == 0 && dy == 0;
    }
    // Both normalized steps are odd precisely when their powers of two match.
    if p.trailing_zeros() == q.trailing_zeros() {
        dx % g == 0 && (dx + dy) % (2 * g) == 0
    } else {
        dx % g == 0 && dy % g == 0
    }
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let Some([p, q, x, y, x1, y1]) = read_values() else {
        return 1;
    };
    let answer: &[u8] = if reachable(p, q, x1 - x, y1 - y) {
        b"YES\n"
    } else {
        b"NO\n"
    };
    // The static bytes remain valid throughout the C call.
    if unsafe { write(STDOUT, answer.as_ptr().cast(), answer.len() as _) } as usize == answer.len()
    {
        0
    } else {
        1
    }
}
