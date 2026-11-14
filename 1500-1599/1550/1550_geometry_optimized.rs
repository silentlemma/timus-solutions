#![no_main]

use std::convert::TryFrom;
use std::f64::consts::PI;
use std::ffi::{c_int, c_void};

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const INPUT_SIZE: usize = 256;
const OUTPUT_SIZE: usize = 24;
const FRACTION_DIGITS: usize = 5;
const SCALE: f64 = 100_000.0;
const DECIMAL: u64 = 10;
const THIRD: f64 = 1.0 / 3.0;

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

fn volume(text: &[u8]) -> f64 {
    let mut numbers = std::str::from_utf8(text)
        .unwrap()
        .split_ascii_whitespace()
        .map(|token| token.parse::<f64>().unwrap());
    let h = numbers.next().unwrap();
    let w = numbers.next().unwrap();
    let x = numbers.next().unwrap();
    let y = numbers.next().unwrap();
    let r = numbers.next().unwrap();
    let centre = h * (1.0 - 2.0 * x.abs().max(y.abs()) / w);
    h * w * w * THIRD - PI * r * r * centre
}

fn read_block(buffer: &mut [u8]) -> Option<usize> {
    // The C runtime writes at most the length of the live slice.
    let count = unsafe { read(STDIN, buffer.as_mut_ptr().cast(), buffer.len() as _) };
    usize::try_from(count).ok()
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut block = [0; INPUT_SIZE];
    let mut size = 0;
    while size < block.len() {
        let Some(count) = read_block(&mut block[size..]) else {
            return 1;
        };
        if count == 0 {
            break;
        }
        size += count;
    }

    // A longer decimal token still gets the standard parser's full precision.
    let value = if size == block.len() {
        let mut long_input = block.to_vec();
        loop {
            let Some(count) = read_block(&mut block) else {
                return 1;
            };
            if count == 0 {
                break;
            }
            long_input.extend_from_slice(&block[..count]);
        }
        volume(&long_input)
    } else {
        volume(&block[..size])
    };
    let mut scaled = (value * SCALE).round() as u64;
    let mut bytes = [0; OUTPUT_SIZE];
    let mut first = bytes.len() - 1;
    bytes[first] = b'\n';
    for _ in 0..FRACTION_DIGITS {
        first -= 1;
        bytes[first] = b'0' + (scaled % DECIMAL) as u8;
        scaled /= DECIMAL;
    }
    first -= 1;
    bytes[first] = b'.';
    loop {
        first -= 1;
        bytes[first] = b'0' + (scaled % DECIMAL) as u8;
        scaled /= DECIMAL;
        if scaled == 0 {
            break;
        }
    }
    let answer = &bytes[first..];
    // These bytes remain valid throughout the write.
    if unsafe { write(STDOUT, answer.as_ptr().cast(), answer.len() as _) } as usize == answer.len()
    {
        0
    } else {
        1
    }
}
