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

const FRAMES: usize = 10;
const PINS: i16 = 10;
const MAX_LAST_ROLLS: i16 = 3;
const STATES: usize = 4;
const INF: i16 = FRAMES as i16 * PINS * MAX_LAST_ROLLS + 1;

fn put(low: &mut [i16; STATES], high: &mut [i16; STATES], state: usize, a: i16, b: i16) {
    low[state] = low[state].min(a);
    high[state] = high[state].max(b);
}

// The C ABI entry avoids unused Rust stdio/startup; all IO buffers are bounded.
#[no_mangle]
pub extern "C" fn main() -> c_int {
    let mut input = Input::new();
    let mut output = Output::new();
    let mut low = [INF; STATES];
    let mut high = [-1; STATES];
    low[0] = 0;
    high[0] = 0;
    for _ in 0..FRAMES - 1 {
        let total = input.number() as i16;
        let mut next_low = [INF; STATES];
        let mut next_high = [-1; STATES];
        for state in 0..STATES {
            if high[state] < 0 {
                continue;
            }
            let (a, b) = (((state + 1) / 2) as i16, (state / 2) as i16);
            if total < PINS {
                put(
                    &mut next_low,
                    &mut next_high,
                    0,
                    low[state] + total * (1 + b),
                    high[state] + total * (1 + a),
                );
            } else {
                put(
                    &mut next_low,
                    &mut next_high,
                    1,
                    low[state] + PINS * (1 + b),
                    high[state] + PINS + (PINS - 1) * a + b,
                );
                // One strike roll shifts the old second pending coefficient.
                let target = 2 + b as usize;
                let bonus = PINS * (1 + a);
                put(
                    &mut next_low,
                    &mut next_high,
                    target,
                    low[state] + bonus,
                    high[state] + bonus,
                );
            }
        }
        low = next_low;
        high = next_high;
    }
    let last = input.number() as i16;
    let (mut answer_low, mut answer_high) = (INF, -1);
    for state in 0..STATES {
        if high[state] < 0 {
            continue;
        }
        let (a, b) = (((state + 1) / 2) as i16, (state / 2) as i16);
        let (lower, upper) = if last < PINS {
            (b * last, a * last)
        } else if last <= 2 * PINS {
            (PINS * b, PINS * a + b * (last - PINS))
        } else {
            let value = PINS * (a + b);
            (value, value)
        };
        answer_low = answer_low.min(low[state] + last + lower);
        answer_high = answer_high.max(high[state] + last + upper);
    }

    output.number(answer_low as u64);
    output.byte(b' ');
    output.number(answer_high as u64);
    output.byte(b'\n');
    output.flush();
    0
}
