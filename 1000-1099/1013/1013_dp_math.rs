#![no_main]

use std::os::raw::c_int;

const IO_BYTES: usize = 512;
const DECIMAL_BYTES: usize = 20;
const RADIX: u64 = 10;

extern "C" {
    fn read(fd: c_int, buffer: *mut u8, length: usize) -> isize;
    fn write(fd: c_int, buffer: *const u8, length: usize) -> isize;
}

struct Input {
    bytes: [u8; IO_BYTES],
    position: usize,
    length: usize,
}
impl Input {
    fn new() -> Self {
        Self {
            bytes: [0; IO_BYTES],
            position: 0,
            length: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.position == self.length {
            let count = unsafe { read(0, self.bytes.as_mut_ptr(), IO_BYTES) };
            if count <= 0 {
                return 0;
            }
            self.position = 0;
            self.length = count as usize;
        }
        let value = self.bytes[self.position];
        self.position += 1;
        value
    }
    fn number(&mut self) -> i64 {
        let mut ch = self.byte();
        while ch != 0 && !ch.is_ascii_digit() && ch != b'-' {
            ch = self.byte();
        }
        let negative = ch == b'-';
        if negative {
            ch = self.byte();
        }
        let mut value = 0i64;
        while ch.is_ascii_digit() {
            value = value * RADIX as i64 + i64::from(ch - b'0');
            ch = self.byte();
        }
        if negative {
            -value
        } else {
            value
        }
    }
}
struct Output {
    bytes: [u8; IO_BYTES],
    length: usize,
}
impl Output {
    fn new() -> Self {
        Self {
            bytes: [0; IO_BYTES],
            length: 0,
        }
    }
    fn flush(&mut self) {
        let mut start = 0;
        while start < self.length {
            let count = unsafe { write(1, self.bytes[start..].as_ptr(), self.length - start) };
            if count <= 0 {
                break;
            }
            start += count as usize;
        }
        self.length = 0;
    }
    fn byte(&mut self, value: u8) {
        if self.length == IO_BYTES {
            self.flush();
        }
        self.bytes[self.length] = value;
        self.length += 1;
    }
    fn number(&mut self, mut value: u64) {
        let mut digits = [0u8; DECIMAL_BYTES];
        let mut start = DECIMAL_BYTES;
        loop {
            start -= 1;
            digits[start] = b'0' + (value % RADIX) as u8;
            value /= RADIX;
            if value == 0 {
                break;
            }
        }
        for digit in &digits[start..] {
            self.byte(*digit);
        }
    }
}

// The C ABI entry avoids unused Rust stdio/startup; all IO buffers are bounded.
#[no_mangle]
pub extern "C" fn main() -> c_int {
    let mut input = Input::new();
    let mut output = Output::new();
    let n = input.number() as u64;
    let base = input.number() as u64;
    let modulus = input.number() as u64;
    let m = u128::from(modulus);
    let c = (u128::from(base) - 1) % m;
    let (mut a, mut b) = (0u128, 1u128);
    // Every product/sum stays below3*M^2<3*10^36, inside128bits.
    for bit in (0..u64::BITS - n.leading_zeros()).rev() {
        let shared = (a * a % m) * c;
        (a, b) = ((shared + 2 * a * b) % m, (shared + b * b) % m);
        if n >> bit & 1 != 0 {
            let shared = a * c % m;
            (a, b) = ((shared + b) % m, shared);
        }
    }
    output.number(((a * c + b) % m) as u64);
    output.byte(b'\n');
    output.flush();
    0
}
