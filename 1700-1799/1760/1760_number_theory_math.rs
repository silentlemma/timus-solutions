#![no_main]

use std::ffi::{c_int, c_void};

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

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const BUFFER_SIZE: usize = 128;
const INPUT_RADIX: u32 = 10;

struct Input {
    bytes: [u8; BUFFER_SIZE],
    start: usize,
    end: usize,
}

impl Input {
    fn new() -> Self {
        Self {
            bytes: [0; BUFFER_SIZE],
            start: 0,
            end: 0,
        }
    }

    fn byte(&mut self) -> Option<u8> {
        if self.start == self.end {
            // The runtime receives the pointer and size of the live buffer.
            let size = unsafe { read(STDIN, self.bytes.as_mut_ptr().cast(), BUFFER_SIZE as _) };
            if size <= 0 {
                return None;
            }
            self.start = 0;
            self.end = size as usize;
        }
        let byte = self.bytes[self.start];
        self.start += 1;
        Some(byte)
    }

    fn number(&mut self) -> Option<u32> {
        let mut byte = self.byte()?;
        while byte.is_ascii_whitespace() {
            byte = self.byte()?;
        }
        let mut value = 0;
        while byte.is_ascii_digit() {
            value = value * INPUT_RADIX + u32::from(byte - b'0');
            byte = self.byte().unwrap_or(b' ');
        }
        Some(value)
    }
}

fn send(bytes: &[u8]) -> c_int {
    // The answer slice remains initialized for the duration of the call.
    let written = unsafe { write(STDOUT, bytes.as_ptr().cast(), bytes.len() as _) };
    c_int::from(written as usize != bytes.len())
}

const SUM_OF_SQUARES_DIVISOR: i128 = 6;

fn index_sum(n: i128) -> i128 {
    n * (n - 1) / 2
}

fn square_sum(n: i128) -> i128 {
    n * (n - 1) * (2 * n - 1) / SUM_OF_SQUARES_DIVISOR
}

// For 0 <= i < n, return the sums of q, i*q and q*q, where q = (a*i+b)/m.
fn floor_moments(n: i128, m: i128, a: i128, b: i128) -> (i128, i128, i128) {
    if n == 0 {
        return (0, 0, 0);
    }
    let (slope, offset) = (a / m, b / m);
    let (a, b) = (a % m, b % m);
    let height = (a * (n - 1) + b) / m;
    let indices = index_sum(n);
    let squares = square_sum(n);
    let (mut sum, mut weighted, mut squared) = (0, 0, 0);
    if height != 0 {
        // For row j >= 1, the first index with q >= j is ceil((m*j-b)/a).
        let (starts, weighted_starts, squared_starts) = floor_moments(height, a, m, m + a - 1 - b);
        sum = height * n - starts;
        weighted = height * indices - (squared_starts - starts) / 2;
        squared = n * height * height - 2 * weighted_starts - starts;
    }
    (
        sum + slope * indices + offset * n,
        weighted + slope * squares + offset * indices,
        squared
            + 2 * (slope * weighted + offset * sum + slope * offset * indices)
            + slope * slope * squares
            + offset * offset * n,
    )
}

fn pairs(n: i128, page: i128) -> i128 {
    n / page * index_sum(page) + index_sum(n % page)
}

fn count_pairs(a: i128, b: i128, n: i128) -> i128 {
    let (large, small) = (a.max(b), a.min(b));
    let cuts = (n - 1) / large;
    let stride = large % small;
    let (sum, weighted, squared) = floor_moments(cuts, small, stride, 0);
    let residues = stride * index_sum(cuts) - small * sum;
    let residue_squares = stride * stride * square_sum(cuts) - 2 * stride * small * weighted
        + small * small * squared;
    let mut split = small * residues - residue_squares;
    if cuts != 0 {
        // The last cut may split a page that is only partially filled.
        let last = cuts * large;
        let left = last % small;
        split += left * (small - left).min(n - last);
    }
    pairs(n, a) - pairs(n, small) + split
}

const OUTPUT_SIZE: usize = 24;

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut input = Input::new();
    let (Some(a), Some(b), Some(n)) = (input.number(), input.number(), input.number()) else {
        return 1;
    };
    // The answer cannot exceed the number of pairs of input positions.
    let mut answer = count_pairs(i128::from(a), i128::from(b), i128::from(n)) as u64;
    let mut output = [b'\n'; OUTPUT_SIZE];
    let mut start = OUTPUT_SIZE - 1;
    let radix = u64::from(INPUT_RADIX);
    loop {
        start -= 1;
        output[start] = b'0' + (answer % radix) as u8;
        answer /= radix;
        if answer == 0 {
            break;
        }
    }
    send(&output[start..])
}
