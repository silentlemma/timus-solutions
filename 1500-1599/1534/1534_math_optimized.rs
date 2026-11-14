#![no_main]

use std::ffi::{c_int, c_void};

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const BUFFER_SIZE: usize = 128;
const DECIMAL: i64 = 10;
const FIELDS: usize = 3;
const OUTPUT_SIZE: usize = 24;

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

fn write_number(output: &mut [u8], mut end: usize, mut value: i64) -> usize {
    loop {
        end -= 1;
        output[end] = b'0' + (value % DECIMAL) as u8;
        value /= DECIMAL;
        if value == 0 {
            return end;
        }
    }
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let Some([scored, conceded, matches]) = read_values() else {
        return 1;
    };
    let margin = scored - conceded;
    let (mut best, mut worst) = if margin >= 0 {
        (
            matches + 2 * margin.min(matches),
            matches + 2 * i64::from(margin > 0),
        )
    } else {
        (matches - 1, matches - (-margin).min(matches))
    };
    if scored > 0 && conceded > 0 && matches > 1 {
        let other_matches = matches - 1;
        best = best.max(other_matches + 2 * scored.min(other_matches));
        worst = worst.min(matches + 2 - conceded.min(other_matches));
    }
    let mut output = [b'\n'; OUTPUT_SIZE];
    let start_worst = write_number(&mut output, OUTPUT_SIZE - 1, worst);
    output[start_worst - 1] = b' ';
    let start_best = write_number(&mut output, start_worst - 1, best);
    let answer = &output[start_best..];
    // The output buffer stays valid throughout the call.
    if unsafe { write(STDOUT, answer.as_ptr().cast(), answer.len() as _) } as usize == answer.len()
    {
        0
    } else {
        1
    }
}
