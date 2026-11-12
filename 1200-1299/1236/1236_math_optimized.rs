use std::io::{self, Read, Write};

const MAX_LENGTH: usize = 10000;
const BUFFER_SIZE: usize = 4096;
const HEX_RADIX: u8 = 16;
const DIGITS: &[u8] = b"0123456789ABCDEF";

struct Input<R: Read> {
    stream: R,
    bytes: [u8; BUFFER_SIZE],
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

    fn encoded(&mut self) -> u8 {
        let mut c = self.next();
        while c != 0 && c <= b' ' {
            c = self.next();
        }
        hex_value(c) * HEX_RADIX + hex_value(self.next())
    }
}

fn hex_value(c: u8) -> u8 {
    if c <= b'9' {
        c - b'0'
    } else {
        c.to_ascii_uppercase() - b'A' + 10
    }
}

fn key(output: &mut impl Write, value: u8) {
    output
        .write_all(&[
            DIGITS[(value / HEX_RADIX) as usize],
            DIGITS[(value % HEX_RADIX) as usize],
        ])
        .unwrap();
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        stream: stdin.lock(),
        bytes: [0; BUFFER_SIZE],
        position: 0,
        length: 0,
    };
    let mut shorter = [0_u8; MAX_LENGTH];
    let mut length = 0;
    let mut c = input.next();
    while c != 0 && c <= b' ' {
        c = input.next();
    }
    while c > b' ' {
        let high = hex_value(c);
        let low = hex_value(input.next());
        shorter[length] = high * HEX_RADIX + low;
        length += 1;
        c = input.next();
    }
    let stdout = io::stdout();
    let mut output = io::BufWriter::with_capacity(BUFFER_SIZE, stdout.lock());
    let mut previous = input.encoded() ^ b' ';
    key(&mut output, previous);
    for &byte in &shorter[..length] {
        // Cancel the common plaintext byte without retaining either decoded longer text or key.
        previous ^= byte ^ input.encoded();
        key(&mut output, previous);
    }
    output.write_all(b"\n").unwrap();
    output.flush().unwrap();
}
