use std::io::{self, Read};
// refilling bounds input memory even when the input has extra whitespace.
const BUFFER_SIZE: usize = 4096;
struct Input<R: Read> {
    source: R,
    buffer: [u8; BUFFER_SIZE],
    at: usize,
    len: usize,
}
impl<R: Read> Input<R> {
    fn new(source: R) -> Self {
        Self {
            source,
            buffer: [0; BUFFER_SIZE],
            at: 0,
            len: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.at == self.len {
            self.len = self.source.read(&mut self.buffer).unwrap();
            self.at = 0;
            if self.len == 0 {
                return b' ';
            }
        }
        let value = self.buffer[self.at];
        self.at += 1;
        value
    }
    fn number(&mut self) -> i32 {
        let mut c = self.byte();
        while c <= b' ' {
            c = self.byte();
        }
        let sign = if c == b'-' {
            c = self.byte();
            -1
        } else {
            1
        };
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.byte();
        }
        value * sign
    }
}

const TARGET: i32 = 10000;
fn main() {
    let stdin = io::stdin();
    let mut input = Input::new(stdin.lock());
    let n = input.number() as usize;
    // statement values fit signed 16 bits; widen again before adding.
    let up: Vec<i16> = (0..n).map(|_| input.number() as i16).collect();
    let m = input.number();
    let mut at = 0;
    let mut found = false;
    for _ in 0..m {
        let value = input.number();
        while at < n && i32::from(up[at]) + value < TARGET {
            at += 1;
        }
        if at < n && i32::from(up[at]) + value == TARGET {
            found = true;
        }
    }
    println!("{}", if found { "YES" } else { "NO" });
}
