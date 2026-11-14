#![no_main]

use std::ffi::{c_int, c_void};

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const BUFFER_SIZE: usize = 128;
const DECIMAL: i64 = 10;
const FIELDS: usize = 6;
const PRECISION: u32 = 12;
const SCALE: i64 = DECIMAL.pow(PRECISION);
const OUTPUT_SIZE: usize = 96;
const NO: &[u8] = b"NO\n";

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

fn append_integer(output: &mut [u8], cursor: &mut usize, number: i64) {
    if number < 0 {
        output[*cursor] = b'-';
        *cursor += 1;
    }
    let mut magnitude = number.abs();
    let start = *cursor;
    loop {
        output[*cursor] = b'0' + (magnitude % DECIMAL) as u8;
        *cursor += 1;
        magnitude /= DECIMAL;
        if magnitude == 0 {
            break;
        }
    }
    output[start..*cursor].reverse();
}

fn append_coordinate(output: &mut [u8], cursor: &mut usize, numerator: i64, denominator: i64) {
    let mut magnitude = ((i128::from(numerator.abs()) * i128::from(SCALE)
        + i128::from(denominator / 2))
        / i128::from(denominator)) as i64;
    if numerator < 0 {
        output[*cursor] = b'-';
        *cursor += 1;
    }
    append_integer(output, cursor, magnitude / SCALE);
    output[*cursor] = b'.';
    *cursor += 1;
    let end = *cursor + PRECISION as usize;
    for slot in output[*cursor..end].iter_mut().rev() {
        *slot = b'0' + (magnitude % DECIMAL) as u8;
        magnitude /= DECIMAL;
    }
    *cursor = end;
}

fn write_answer(answer: &[u8]) -> c_int {
    // The buffer stays valid throughout the call.
    if unsafe { write(STDOUT, answer.as_ptr().cast(), answer.len() as _) } as usize == answer.len()
    {
        0
    } else {
        1
    }
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let Some([ax, ay, bx, by, cx, cy]) = read_values() else {
        return 1;
    };
    let (dx, dy) = (cx - ax, cy - ay);
    let squared = dx * dx + dy * dy;
    let other = 2 * ((bx - ax) * dx + (by - ay) * dy) - squared;
    if other <= 0 || other == squared {
        return write_answer(b"YES\n");
    }
    let mut output = [0u8; OUTPUT_SIZE];
    output[..NO.len()].copy_from_slice(NO);
    let mut cursor = NO.len();
    for (value, separator) in [(ax, b' '), (ay, b'\n'), (bx, b' '), (by, b'\n')] {
        append_integer(&mut output, &mut cursor, value);
        output[cursor] = separator;
        cursor += 1;
    }
    append_coordinate(&mut output, &mut cursor, ax * squared + dx * other, squared);
    output[cursor] = b' ';
    cursor += 1;
    append_coordinate(&mut output, &mut cursor, ay * squared + dy * other, squared);
    output[cursor] = b'\n';
    write_answer(&output[..=cursor])
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
