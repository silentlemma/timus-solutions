use std::io::{self, Read};

const BUFFER_SIZE: usize = 65536;

// the dates are parsed by hand from a 64 KB buffer instead of reading the
// whole input into a string, and kept as u32
struct Input<R> {
    reader: R,
    buffer: [u8; BUFFER_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> Input<R> {
    fn new(reader: R) -> Self {
        Self {
            reader,
            buffer: [0; BUFFER_SIZE],
            position: 0,
            length: 0,
        }
    }

    fn byte(&mut self) -> Option<u8> {
        if self.position == self.length {
            self.length = self.reader.read(&mut self.buffer).unwrap();
            self.position = 0;
            if self.length == 0 {
                return None;
            }
        }
        let byte = self.buffer[self.position];
        self.position += 1;
        Some(byte)
    }

    fn number(&mut self) -> u32 {
        let mut byte = self.byte();
        while byte.is_some_and(|ch| ch <= b' ') {
            byte = self.byte();
        }
        let mut value = 0;
        while let Some(ch @ b'0'..=b'9') = byte {
            value = value * 10 + u32::from(ch - b'0');
            byte = self.byte();
        }
        value
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input::new(stdin.lock());
    let size = input.number() as usize;
    // the teacher's dates come sorted, so each of the student's dates is
    // looked up by binary search, counting repeats every time
    let known: Vec<u32> = (0..size).map(|_| input.number()).collect();
    let queries = input.number();
    let mut count = 0;
    for _ in 0..queries {
        if known.binary_search(&input.number()).is_ok() {
            count += 1;
        }
    }
    println!("{}", count);
}
