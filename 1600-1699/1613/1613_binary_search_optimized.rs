use std::io::{self, Read, Write};

// refills keep input memory constant, including for the largest cases.
const INPUT_BUFFER: usize = 4096;
struct Input<R> {
    reader: R,
    buffer: [u8; INPUT_BUFFER],
    pos: usize,
    len: usize,
}
impl<R: Read> Input<R> {
    fn new(reader: R) -> Self {
        Self {
            reader,
            buffer: [0; INPUT_BUFFER],
            pos: 0,
            len: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.pos == self.len {
            self.len = self.reader.read(&mut self.buffer).unwrap();
            self.pos = 0;
            if self.len == 0 {
                return 0;
            }
        }
        let c = self.buffer[self.pos];
        self.pos += 1;
        c
    }
    fn next(&mut self) -> usize {
        let mut c = self.byte();
        while c != 0 && c <= b' ' {
            c = self.byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + usize::from(c - b'0');
            c = self.byte();
        }
        value
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input::new(stdin.lock());
    let n = input.next();
    // (passengers, city) pairs in order: the cities with one count are
    // consecutive and sorted by number
    let mut pairs: Vec<(u32, u32)> = (1..=n as u32)
        .map(|city| (input.next() as u32, city))
        .collect();
    pairs.sort_unstable();
    let q = input.next();
    let mut out = Vec::with_capacity(q + 1);
    for _ in 0..q {
        let (lo, hi, x) = (
            input.next() as u32,
            input.next() as u32,
            input.next() as u32,
        );
        // the first city with count x and number at least lo
        let k = pairs.partition_point(|&p| p < (x, lo));
        let found = k < n && pairs[k].0 == x && pairs[k].1 <= hi;
        out.push(if found { b'1' } else { b'0' });
    }
    out.push(b'\n');
    io::stdout().write_all(&out).unwrap();
}
