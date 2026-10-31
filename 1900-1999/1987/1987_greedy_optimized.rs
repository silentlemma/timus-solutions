use std::io::{self, Read, Write};

const INPUT_BUFFER: usize = 4096;
// the refillable buffer holds only a chunk, never the complete input.
struct Reader<R> {
    input: R,
    buffer: [u8; INPUT_BUFFER],
    at: usize,
    size: usize,
}
impl<R: Read> Reader<R> {
    fn new(input: R) -> Self {
        Self {
            input,
            buffer: [0; INPUT_BUFFER],
            at: 0,
            size: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.at == self.size {
            self.size = self.input.read(&mut self.buffer).unwrap();
            self.at = 0;
            if self.size == 0 {
                return 0;
            }
        }
        let c = self.buffer[self.at];
        self.at += 1;
        c
    }
    fn next(&mut self) -> i32 {
        let mut c = self.byte();
        while c != 0 && c != b'-' && !c.is_ascii_digit() {
            c = self.byte();
        }
        let mut sign = 1;
        if c == b'-' {
            sign = -1;
            c = self.byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.byte();
        }
        value * sign
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = Reader::new(stdin.lock());
    let n = input.next() as usize;
    let (mut left, mut right) = (Vec::with_capacity(n), Vec::with_capacity(n));
    for _ in 0..n {
        left.push(input.next());
        right.push(input.next());
    }
    let m = input.next();
    let (mut index, mut top) = (0, -1i32);
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    for _ in 0..m {
        let point = input.next();
        while index < n && left[index] <= point {
            while top >= 0 && right[top as usize] < left[index] {
                top = left[top as usize];
            }
            // the consumed endpoint becomes a parent link; n <= 100000 fits i32.
            left[index] = top;
            top = index as i32;
            index += 1;
        }
        while top >= 0 && right[top as usize] < point {
            top = left[top as usize];
        }
        writeln!(out, "{}", if top < 0 { -1 } else { top + 1 }).unwrap();
    }
}
