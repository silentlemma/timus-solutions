use std::io::{self, Read};

// refilling bounds input storage; coordinates <= 10^6 fit u32, sums < 10^16 fit u64.
const BUFFER_SIZE: usize = 4096;

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
                return b' ';
            }
        }
        let byte = self.buffer[self.position];
        self.position += 1;
        byte
    }

    fn number(&mut self) -> u32 {
        let mut byte = self.byte();
        while byte <= b' ' {
            byte = self.byte();
        }
        let mut value = 0;
        while byte.is_ascii_digit() {
            value = value * 10 + u32::from(byte - b'0');
            byte = self.byte();
        }
        value
    }
}

// the sum of |a_i - a_j| over all pairs: in sorted order the i-th value
// is larger than the i values before it
fn pair_sum(values: &mut [u32]) -> u64 {
    values.sort_unstable();
    let (mut total, mut before) = (0, 0);
    for (i, &value) in values.iter().enumerate() {
        total += u64::from(value) * i as u64 - before;
        before += u64::from(value);
    }
    total
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        reader: stdin.lock(),
        buffer: [0; BUFFER_SIZE],
        position: 0,
        length: 0,
    };
    let n = input.number() as usize;
    let mut x = Vec::with_capacity(n);
    let mut y = Vec::with_capacity(n);
    for _ in 0..n {
        x.push(input.number());
        y.push(input.number());
    }
    // walking along the streets, a visit covers |dx| + |dy|
    let pairs = n as u64 * (n - 1) as u64 / 2;
    println!("{}", (pair_sum(&mut x) + pair_sum(&mut y)) / pairs);
}
