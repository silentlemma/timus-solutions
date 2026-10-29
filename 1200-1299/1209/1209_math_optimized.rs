use std::io::{self, BufWriter, Read, Write};

const DISCRIMINANT_FACTOR: i64 = 8;
const BUFFER_SIZE: usize = 1 << 10;

// the positions are parsed by hand from a 1 KB buffer, and each answer goes
// out as two bytes, without a String of the whole input or output
struct Input<R> {
    source: R,
    buffer: [u8; BUFFER_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> Input<R> {
    fn new(source: R) -> Self {
        Self {
            source,
            buffer: [0; BUFFER_SIZE],
            position: 0,
            length: 0,
        }
    }

    fn byte(&mut self) -> u8 {
        if self.position == self.length {
            self.length = self.source.read(&mut self.buffer).unwrap();
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let result = self.buffer[self.position];
        self.position += 1;
        result
    }

    fn number(&mut self) -> u32 {
        let mut c = self.byte();
        while c <= b' ' && c != 0 {
            c = self.byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + u32::from(c - b'0');
            c = self.byte();
        }
        value
    }
}

// whether v is a perfect square, with the floating root corrected exactly.
fn is_square(v: i64) -> bool {
    let mut r = (v as f64).sqrt() as i64;
    while r * r > v {
        r -= 1;
    }
    while (r + 1) * (r + 1) <= v {
        r += 1;
    }
    r * r == v
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input::new(stdin.lock());
    let stdout = io::stdout();
    let mut output = BufWriter::with_capacity(BUFFER_SIZE, stdout.lock());
    let n = input.number();
    for i in 0..n {
        let k = i64::from(input.number());
        // the ones stand at 1 + m(m - 1) / 2, that is where 8(k - 1) + 1 is a
        // perfect square
        let digit = if is_square(DISCRIMINANT_FACTOR * (k - 1) + 1) {
            b'1'
        } else {
            b'0'
        };
        let separator = if i + 1 < n { b' ' } else { b'\n' };
        output.write_all(&[digit, separator]).unwrap();
    }
    output.flush().unwrap();
}
