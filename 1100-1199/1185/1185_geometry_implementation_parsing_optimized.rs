#![no_main]

macro_rules! native_println {
    () => { native_write_all(b"\n") };
    ($($argument:tt)*) => {{
        let mut output = NativeOutput::new();
        std::fmt::Write::write_fmt(&mut output, format_args!($($argument)*)).unwrap();
        std::fmt::Write::write_str(&mut output, "\n").unwrap();
        output.flush();
    }};
}

use std::f64::consts::PI;

fn cross(o: (i64, i64), a: (i64, i64), b: (i64, i64)) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

fn solve_entry() {
    let mut it = NativeNumbers::new();
    let n = it.next().unwrap() as usize;
    let gap = it.next().unwrap() as f64;
    let mut pts: Vec<(i64, i64)> = (0..n)
        .map(|_| (it.next().unwrap(), it.next().unwrap()))
        .collect();
    pts.sort_unstable();
    // the shortest wall is the convex hull pushed out by L: its straight
    // parts add up to the hull perimeter, and its arcs turn once around a
    // full circle of radius L in total
    let mut hull = Vec::with_capacity(2 * pts.len());
    for &p in &pts {
        while hull.len() >= 2 && cross(hull[hull.len() - 2], hull[hull.len() - 1], p) <= 0 {
            hull.pop();
        }
        hull.push(p);
    }
    let lower = hull.len();
    for &p in pts.iter().rev().skip(1) {
        while hull.len() > lower && cross(hull[hull.len() - 2], hull[hull.len() - 1], p) <= 0 {
            hull.pop();
        }
        hull.push(p);
    }
    if hull.len() > 1 {
        hull.pop();
    }
    let mut length = 2.0 * PI * gap;
    for k in 0..hull.len() {
        let (a, b) = (hull[k], hull[(k + 1) % hull.len()]);
        length += (((a.0 - b.0).pow(2) + (a.1 - b.1).pow(2)) as f64).sqrt();
    }
    native_println!("{}", length.round() as i64);
}

// Return after all native output writes have completed.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    native_setup();
    solve_entry();
    0
}

const NATIVE_INPUT_BYTES: usize = 4096;

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn native_read(fd: i32, data: *mut u8, size: u32) -> i32;
    #[link_name = "_write"]
    fn native_write(fd: i32, data: *const u8, size: u32) -> i32;
    fn _setmode(fd: i32, mode: i32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn native_read(fd: i32, data: *mut u8, size: usize) -> isize;
    #[link_name = "write"]
    fn native_write(fd: i32, data: *const u8, size: usize) -> isize;
}

fn native_setup() {
    #[cfg(windows)]
    {
        const BINARY_MODE: i32 = 0x8000;
        // SAFETY: descriptors zero/one are the inherited standard streams.
        unsafe {
            assert!(_setmode(0, BINARY_MODE) != -1);
            assert!(_setmode(1, BINARY_MODE) != -1);
        }
    }
}

fn native_write_all(mut data: &[u8]) {
    while !data.is_empty() {
        // SAFETY: the live readable slice is bounded by the documented output size.
        let count = unsafe {
            #[cfg(windows)]
            {
                native_write(1, data.as_ptr(), data.len() as u32)
            }
            #[cfg(not(windows))]
            {
                native_write(1, data.as_ptr(), data.len())
            }
        };
        if count < 0 {
            #[cfg(not(windows))]
            if std::io::Error::last_os_error().kind() == std::io::ErrorKind::Interrupted {
                continue;
            }
            panic!("output write failed");
        }
        assert!(count > 0);
        data = &data[count as usize..];
    }
}

struct NativeNumbers {
    data: [u8; NATIVE_INPUT_BYTES],
    position: usize,
    length: usize,
}

impl NativeNumbers {
    fn new() -> Self {
        Self {
            data: [0; NATIVE_INPUT_BYTES],
            position: 0,
            length: 0,
        }
    }

    fn refill(&mut self) -> bool {
        loop {
            // SAFETY: the live writable array is passed with its exact bounded length.
            let count = unsafe {
                #[cfg(windows)]
                {
                    native_read(0, self.data.as_mut_ptr(), self.data.len() as u32)
                }
                #[cfg(not(windows))]
                {
                    native_read(0, self.data.as_mut_ptr(), self.data.len())
                }
            };
            if count < 0 {
                #[cfg(not(windows))]
                if std::io::Error::last_os_error().kind() == std::io::ErrorKind::Interrupted {
                    continue;
                }
                panic!("input read failed");
            }
            self.position = 0;
            self.length = count as usize;
            return count != 0;
        }
    }

    #[inline]
    fn byte(&mut self) -> Option<u8> {
        if self.position == self.length && !self.refill() {
            return None;
        }
        let byte = self.data[self.position];
        self.position += 1;
        Some(byte)
    }
}

impl Iterator for NativeNumbers {
    type Item = i64;

    // Input bounds guarantee that each decimal token fits its destination integer.
    // Accumulate negative values directly so the minimum signed integer also fits.
    #[inline]
    fn next(&mut self) -> Option<i64> {
        let mut byte = self.byte()?;
        while byte.is_ascii_whitespace() {
            byte = self.byte()?;
        }
        let negative = byte == b'-';
        if negative || byte == b'+' {
            byte = self.byte().expect("incomplete integer");
        }
        assert!(byte.is_ascii_digit());
        let mut value = 0_i64;
        loop {
            let digit = i64::from(byte - b'0');
            value = if negative {
                value * 10 - digit
            } else {
                value * 10 + digit
            };
            match self.byte() {
                Some(next) if next.is_ascii_digit() => byte = next,
                Some(next) => {
                    assert!(next.is_ascii_whitespace());
                    break;
                }
                None => break,
            }
        }
        Some(value)
    }
}

const NATIVE_OUTPUT_BYTES: usize = 256;

struct NativeOutput {
    data: [u8; NATIVE_OUTPUT_BYTES],
    size: usize,
}

impl NativeOutput {
    fn new() -> Self {
        Self {
            data: [0; NATIVE_OUTPUT_BYTES],
            size: 0,
        }
    }
    fn flush(&mut self) {
        native_write_all(&self.data[..self.size]);
        self.size = 0;
    }
}

impl std::fmt::Write for NativeOutput {
    fn write_str(&mut self, text: &str) -> std::fmt::Result {
        let bytes = text.as_bytes();
        if bytes.len() > self.data.len() - self.size {
            self.flush();
        }
        if bytes.len() >= self.data.len() {
            native_write_all(bytes);
        } else {
            self.data[self.size..self.size + bytes.len()].copy_from_slice(bytes);
            self.size += bytes.len();
        }
        Ok(())
    }
}
