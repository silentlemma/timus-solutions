use std::io::{self, Read, Write};

const MAX_COUNT: usize = 500;
const INPUT_SIZE: usize = 64;
const OUTPUT_SIZE: usize = MAX_COUNT * 6 + 1;
const MAX_DIGITS: usize = 4;

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

    fn next_int(&mut self) -> usize {
        let mut c = self.next_byte();
        while c != 0 && c <= b' ' {
            c = self.next_byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + usize::from(c - b'0');
            c = self.next_byte();
        }
        value
    }
}

fn write_number(output: &mut [u8], used: &mut usize, mut value: usize) {
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
    let n = input.next_int();
    let k = input.next_int();
    let mut output = [0; OUTPUT_SIZE];
    output[0] = b'0';
    let mut used = 1;
    for _ in 0..n - k {
        output[used..used + 2].copy_from_slice(b" 0");
        used += 2;
    }
    // The prefix sums alternate between zero and consecutive positive integers.
    for i in 1..k {
        output[used] = b' ';
        used += 1;
        if i % 2 == 0 {
            output[used] = b'-';
            used += 1;
            write_number(&mut output, &mut used, i / 2);
        } else {
            write_number(&mut output, &mut used, (i + 1) / 2);
        }
    }
    output[used] = b'\n';
    used += 1;
    io::stdout().lock().write_all(&output[..used]).ok();
}
