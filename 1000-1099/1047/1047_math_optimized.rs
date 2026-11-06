use std::io::{self, Read, Write};

const CENTS: i64 = 100;
const INPUT_SIZE: usize = 64;
const OUTPUT_SIZE: usize = 32;
const MAX_DIGITS: usize = 20;

struct Input<R> {
    reader: R,
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> Input<R> {
    fn next_byte(&mut self) -> u8 {
        if self.position == self.length {
            self.length = self.reader.read(&mut self.bytes).unwrap_or(0);
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let value = self.bytes[self.position];
        self.position += 1;
        value
    }

    fn scaled_number(&mut self) -> i64 {
        let mut c = self.next_byte();
        while c != 0 && c <= b' ' {
            c = self.next_byte();
        }
        let negative = c == b'-';
        if negative || c == b'+' {
            c = self.next_byte();
        }
        let mut value = 0;
        // Removing the point preserves N and scales two-decimal values to cents.
        while c.is_ascii_digit() || c == b'.' {
            if c != b'.' {
                value = value * 10 + i64::from(c - b'0');
            }
            c = self.next_byte();
        }
        if negative {
            -value
        } else {
            value
        }
    }
}

fn write_number(output: &mut [u8], used: &mut usize, mut value: i64) {
    let mut digits = [0; MAX_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (value % 10) as u8;
        value /= 10;
        if value == 0 {
            break;
        }
    }
    let length = digits.len() - first;
    output[*used..*used + length].copy_from_slice(&digits[first..]);
    *used += length;
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        reader: stdin.lock(),
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let n = input.scaled_number();
    let first = input.scaled_number();
    let last = input.scaled_number();
    let mut weighted = 0;
    for weight in (1..=n).rev() {
        weighted += weight * input.scaled_number();
    }
    let (num, den) = (n * first + last - 2 * weighted, n + 1);
    let value = (2 * num.abs() + den) / (2 * den);
    let mut output = [0; OUTPUT_SIZE];
    let mut used = 0;
    if num < 0 && value != 0 {
        output[used] = b'-';
        used += 1;
    }
    write_number(&mut output, &mut used, value / CENTS);
    let fraction = [
        b'.',
        b'0' + ((value % CENTS) / 10) as u8,
        b'0' + (value % 10) as u8,
        b'\n',
    ];
    output[used..used + fraction.len()].copy_from_slice(&fraction);
    used += fraction.len();
    io::stdout().lock().write_all(&output[..used]).ok();
}
