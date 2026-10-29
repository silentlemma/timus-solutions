use std::io::{self, Read};

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

    fn next_int(&mut self) -> usize {
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
    let mut input = Input {
        reader: stdin.lock(),
        buffer: [0; BUFFER_SIZE],
        position: 0,
        length: 0,
    };
    let n = input.next_int();
    // the pocket is a stack: roll the balls in order, and whenever the top
    // one is the next ball the inspector took out, take it out
    // each ball is checked as it is read, so their order is never stored
    let mut pocket = vec![0_u32; n];
    let (mut top, mut next) = (0, 1);
    for _ in 0..n {
        let ball = input.next_int();
        while next <= ball {
            pocket[top] = next as u32;
            top += 1;
            next += 1;
        }
        if top == 0 || pocket[top - 1] != ball as u32 {
            println!("Cheater");
            return;
        }
        top -= 1;
    }
    println!("Not a proof");
}
