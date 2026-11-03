use std::io::{self, Read};

const BUFFER_SIZE: usize = 4096;

struct Input<R: Read> {
    stream: R,
    data: [u8; BUFFER_SIZE],
    position: usize,
    end: usize,
}

impl<R: Read> Input<R> {
    fn byte(&mut self) -> Option<u8> {
        if self.position == self.end {
            self.end = self.stream.read(&mut self.data).unwrap();
            self.position = 0;
            if self.end == 0 {
                return None;
            }
        }
        let value = self.data[self.position];
        self.position += 1;
        Some(value)
    }

    fn next(&mut self) -> u32 {
        let mut c = self.byte();
        while c.is_some() && c.unwrap() <= b' ' {
            c = self.byte();
        }
        let mut value = 0;
        while let Some(digit) = c {
            if !digit.is_ascii_digit() {
                break;
            }
            value = value * 10 + u32::from(digit - b'0');
            c = self.byte();
        }
        value
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        stream: stdin.lock(),
        data: [0; BUFFER_SIZE],
        position: 0,
        end: 0,
    };
    let n = input.next();
    let m = input.next();
    let first_v = input.next();
    let (mut last_v, mut max_v) = (first_v, first_v);
    for _ in 1..n {
        last_v = input.next();
        max_v = max_v.max(last_v);
    }
    let first_h = input.next();
    let (mut last_h, mut max_h) = (first_h, first_h);
    for _ in 1..m {
        last_h = input.next();
        max_h = max_h.max(last_h);
    }
    // Both directions and both endpoints suffice because all streets cross.
    println!(
        "{}",
        max_v
            .min(max_h)
            .min(first_v.max(first_h))
            .min(last_v.max(last_h))
    );
}
