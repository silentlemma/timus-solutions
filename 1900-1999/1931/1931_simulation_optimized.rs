use std::io::{self, Read};

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
    let n = input.next();
    let mut champion_value = input.next();
    let (mut champion, mut best, mut current_count, mut best_count) = (0, 0, 0, 0);
    // scores <= 1000000000 and counts <= 100000 fit signed 32-bit integers.
    for index in 1..n {
        let value = input.next();
        current_count += 1;
        if current_count > best_count {
            best_count = current_count;
            best = champion;
        }
        if value < champion_value {
            champion_value = value;
            champion = index;
            current_count = 1;
        }
    }
    println!("{}", best + 1);
}
