use std::io::{self, Read};

const CENTS: u32 = 100;
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
            if digit <= b' ' {
                break;
            }
            if digit.is_ascii_digit() {
                value = value * 10 + u32::from(digit - b'0');
            }
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
    let n = input.next() as usize;
    let k = input.next();
    let mut longest = 0;
    let mut total = 0u64;
    let mut cables = Vec::with_capacity(n);
    for _ in 0..n {
        let length = input.next();
        longest = longest.max(length);
        total += u64::from(length);
        cables.push(length);
    }
    let mut low = longest / k;
    let mut high = u64::from(longest).min(total / u64::from(k)) as u32;
    // Bound in u64 before narrowing: total/k can exceed u32 when k is small.
    // Skipping a decimal dot is exact for the specified two fractional digits.
    while low < high {
        let mid = (low + high + 1) / 2;
        let mut pieces = 0u64;
        for &length in &cables {
            pieces += u64::from(length / mid);
            if pieces >= u64::from(k) {
                break;
            }
        }
        if pieces >= u64::from(k) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    println!("{}.{:02}", low / CENTS, low % CENTS);
}
