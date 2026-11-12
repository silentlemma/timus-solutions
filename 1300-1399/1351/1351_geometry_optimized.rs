use std::io::{self, Read, Write};

const INPUT_SIZE: usize = 4096;
const OUTPUT_SIZE: usize = 8192;
const WORD_RESERVE: usize = 4;

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

    fn number(&mut self) -> i32 {
        let mut c = self.next();
        while c != 0 && c <= b' ' {
            c = self.next();
        }
        let negative = c == b'-';
        if negative {
            c = self.next();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.next();
        }
        if negative {
            -value
        } else {
            value
        }
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        stream: stdin.lock(),
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let (reach, rx, ry) = (input.number(), input.number(), input.number());
    let (lx, ly, n) = (input.number(), input.number(), input.number());
    let radius_squared = reach * reach;
    let stdout = io::stdout();
    let mut stream = stdout.lock();
    let mut output = [0_u8; OUTPUT_SIZE];
    let mut used = 0;
    for _ in 0..n {
        let (x, y) = (input.number(), input.number());
        let (right, left) = (rx * y - ry * x, x * ly - y * lx);
        let behind = (right == 0 && rx * x + ry * y < 0) || (left == 0 && lx * x + ly * y < 0);
        let hit = right >= 0 && left >= 0 && !behind && x * x + y * y <= radius_squared;
        let word: &[u8] = if hit { b"YES\n" } else { b"NO\n" };
        output[used..used + word.len()].copy_from_slice(word);
        used += word.len();
        if used + WORD_RESERVE > OUTPUT_SIZE {
            stream.write_all(&output[..used]).unwrap();
            used = 0;
        }
    }
    stream.write_all(&output[..used]).unwrap();
}
