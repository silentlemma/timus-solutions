#![no_main]

use std::ffi::{c_int, c_void};

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const DIM: usize = 3;
const POINTS: usize = 4;
const BUFFER: usize = 1024;
const DECIMAL: i64 = 10;
type Point = [i64; DIM];

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

fn read_points() -> Option<[Point; POINTS]> {
    let mut points = [[0; DIM]; POINTS];
    let mut count = 0;
    let mut digits = false;
    let mut value = 0;
    let mut negative = false;
    let mut buffer = [0u8; BUFFER];
    loop {
        // `read` fills at most BUFFER bytes of this local array.
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
                b'0'..=b'9' => {
                    value = value * DECIMAL + i64::from(byte - b'0');
                    digits = true;
                }
                b'-' => negative = true,
                _ if digits => {
                    points[count / DIM][count % DIM] = if negative { -value } else { value };
                    count += 1;
                    if count == POINTS * DIM {
                        return Some(points);
                    }
                    (digits, value, negative) = (false, 0, false);
                }
                _ => {}
            }
        }
        if end {
            return None;
        }
    }
}

fn sub(a: Point, b: Point) -> Point {
    [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
}

fn dot(a: Point, b: Point) -> i64 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

fn valid([a, b, c, d]: [Point; POINTS]) -> bool {
    let ab = sub(b, a);
    let bc = sub(c, b);
    let cd = sub(d, c);
    if dot(ab, cd) != 0 || dot(ab, bc) < 0 || dot(bc, cd) < 0 {
        return false;
    }
    let [x, y, z] = ab;
    let [u, v, w] = cd;
    let cross = [y * w - z * v, z * u - x * w, x * v - y * u];
    // Dot products fit in i64. The scalar triple product needs i128.
    bc.iter()
        .zip(cross)
        .map(|(&a, b)| i128::from(a) * i128::from(b))
        .sum::<i128>()
        == 0
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let Some(points) = read_points() else {
        return 1;
    };
    let answer: &[u8] = if valid(points) {
        b"Valid\n"
    } else {
        b"Invalid\n"
    };
    // The byte slice stays valid throughout the call.
    if unsafe { write(STDOUT, answer.as_ptr().cast(), answer.len() as _) } as usize == answer.len()
    {
        0
    } else {
        1
    }
}
