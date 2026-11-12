use std::io::{self, Read, Write};

const INPUT_SIZE: usize = 4096;
const OUTPUT_SIZE: usize = 8192;

struct Input<R: Read> {
    stream: R,
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> Input<R> {
    fn next(&mut self) -> u8 {
        if self.position == self.length {
            self.length = self.stream.read(&mut self.bytes).unwrap();
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let c = self.bytes[self.position];
        self.position += 1;
        c
    }

    fn number(&mut self) -> u32 {
        let mut c = self.next();
        while c != 0 && c <= b' ' {
            c = self.next();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + u32::from(c - b'0');
            c = self.next();
        }
        value
    }
}

const NUMBER_RESERVE: usize = 12;
const DECIMAL_DIGITS: usize = 10;
const DECIMAL_BASE: u32 = 10;

struct Output<W: Write> {
    stream: W,
    bytes: [u8; OUTPUT_SIZE],
    used: usize,
    first: bool,
}

impl<W: Write> Output<W> {
    fn flush(&mut self) {
        self.stream.write_all(&self.bytes[..self.used]).unwrap();
        self.used = 0;
    }

    fn number(&mut self, mut value: u32) {
        if self.used + NUMBER_RESERVE > OUTPUT_SIZE {
            self.flush();
        }
        if !self.first {
            self.bytes[self.used] = b' ';
            self.used += 1;
        }
        self.first = false;
        let mut digits = [0_u8; DECIMAL_DIGITS];
        let mut count = 0;
        loop {
            digits[count] = b'0' + (value % DECIMAL_BASE) as u8;
            count += 1;
            value /= DECIMAL_BASE;
            if value == 0 {
                break;
            }
        }
        while count > 0 {
            count -= 1;
            self.bytes[self.used] = digits[count];
            self.used += 1;
        }
    }

    fn line(&mut self) {
        self.bytes[self.used] = b'\n';
        self.used += 1;
        self.first = true;
    }
}

fn arrange<F: FnMut(u32)>(values: &[u32], capacity: u32, mut emit: F) -> u32 {
    let (mut left, mut right, mut trips) = (0, values.len(), 0);
    while right - left >= 2 {
        emit(values[left]);
        if values[left] + values[right - 1] > capacity {
            emit(values[right - 1]);
            left += 1;
            right -= 1;
            trips += 2;
        } else {
            emit(values[left + 1]);
            left += 2;
            trips += 1;
        }
    }
    if left < right {
        emit(values[left]);
        trips += 1;
    }
    trips
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        stream: stdin.lock(),
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let n = input.number() as usize;
    let capacity = input.number();
    let mut values = Vec::with_capacity(n);
    for _ in 0..n {
        values.push(input.number());
    }
    drop(input);
    values.sort_unstable();
    let trips = arrange(&values, capacity, |_| {});
    let stdout = io::stdout();
    let mut output = Output {
        stream: stdout.lock(),
        bytes: [0; OUTPUT_SIZE],
        used: 0,
        first: true,
    };
    output.number(trips);
    output.line();
    arrange(&values, capacity, |value| output.number(value));
    output.line();
    output.flush();
}
