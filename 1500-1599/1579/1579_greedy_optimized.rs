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

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        stream: stdin.lock(),
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let n = input.number() as usize;
    let r = input.number();
    let mut sizes = Vec::with_capacity(n);
    for _ in 0..n {
        sizes.push(input.number());
    }
    let (mut trips, mut left) = (0, 0);
    for right in 0..n {
        while sizes[right] - sizes[left] > r {
            left += 1;
        }
        trips = trips.max(right - left + 1);
    }
    let stdout = io::stdout();
    let mut output = io::BufWriter::with_capacity(OUTPUT_SIZE, stdout.lock());
    writeln!(output, "{}", trips).unwrap();
    // Taking indices modulo trips attains the maximum-window lower bound.
    for trip in 0..trips {
        write!(output, "{}", (n - trip + trips - 1) / trips).unwrap();
        for coat in (trip + 1..=n).step_by(trips) {
            write!(output, " {}", coat).unwrap();
        }
        output.write_all(b"\n").unwrap();
    }
    output.flush().unwrap();
}
