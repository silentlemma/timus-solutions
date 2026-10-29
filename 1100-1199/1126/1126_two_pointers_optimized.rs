use std::collections::VecDeque;
use std::io::{self, Read, Write};

const BUFFER_SIZE: usize = 4096;

// the numbers are parsed by hand from a 4 KB buffer instead of reading the
// whole input into a string
struct Input<R> {
    reader: R,
    buffer: [u8; BUFFER_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> Input<R> {
    fn byte(&mut self) -> u8 {
        if self.position == self.length {
            self.length = self.reader.read(&mut self.buffer).unwrap();
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let c = self.buffer[self.position];
        self.position += 1;
        c
    }

    fn next_int(&mut self) -> i32 {
        let mut c = self.byte();
        while c != 0 && c <= b' ' {
            c = self.byte();
        }
        if c == 0 || c == b'-' {
            return -1;
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.byte();
        }
        value
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        reader: stdin.lock(),
        buffer: [0; BUFFER_SIZE],
        position: 0,
        length: 0,
    };
    let width = input.next_int();
    // indices of the window whose values decrease from front to back: the
    // front is the maximum, and a value never matters once a later one is larger
    let mut window: VecDeque<(i32, i32)> = VecDeque::with_capacity(width as usize);
    // each answer goes out through a buffered writer as soon as it is known
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    let mut index = 0;
    loop {
        let value = input.next_int();
        if value < 0 {
            break;
        }
        if window.front().map_or(false, |&(_, i)| i <= index - width) {
            window.pop_front();
        }
        while window.back().map_or(false, |&(v, _)| v <= value) {
            window.pop_back();
        }
        window.push_back((value, index));
        if index + 1 >= width {
            writeln!(out, "{}", window[0].0).unwrap();
        }
        index += 1;
    }
}
