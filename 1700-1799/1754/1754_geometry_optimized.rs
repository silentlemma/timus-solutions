#![no_main]

use std::ffi::{c_int, c_void};

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const BUFFER_SIZE: usize = 128;
const DECIMAL: i64 = 10;
const FIELDS: usize = 13;
const CORNERS: usize = 3;

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

fn escapes(values: [i64; FIELDS]) -> bool {
    let [mana, height, top, x, y, ax, ay, bx, by, cx, cy, tx, ty] = values;
    let radius = mana - height;
    if radius <= 0 {
        return false;
    }
    if radius >= height {
        return true;
    }
    let base = [(ax, ay), (bx, by), (cx, cy)];
    let radius_squared = i128::from(radius * radius);
    for (index, &(sx, sy)) in base.iter().enumerate() {
        let (ex, ey) = base[(index + 1) % CORNERS];
        let (ux, uy) = (ex - sx, ey - sy);
        let (nx, ny) = (uy * top, -ux * top);
        let nz = ux * (ty - sy) - uy * (tx - sx);
        // Compare squared distance to the plane without dividing by the normal length.
        let distance = i128::from(nx * (x - sx) + ny * (y - sy) + nz * height);
        let norm_squared = i128::from(nx * nx + ny * ny + nz * nz);
        if distance * distance <= radius_squared * norm_squared {
            return true;
        }
    }
    false
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let Some(values) = read_values() else {
        return 1;
    };
    let answer: &[u8] = if escapes(values) { b"YES\n" } else { b"NO\n" };
    // The static answer bytes stay valid for the duration of the call.
    if unsafe { write(STDOUT, answer.as_ptr().cast(), answer.len() as _) } as usize == answer.len()
    {
        0
    } else {
        1
    }
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
