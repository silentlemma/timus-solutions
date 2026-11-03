use std::io::{self, Read, Write};

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

    fn next(&mut self) -> i32 {
        let mut c = self.byte();
        while c.is_some() && c.unwrap() <= b' ' {
            c = self.byte();
        }
        let sign = if c == Some(b'-') {
            c = self.byte();
            -1
        } else {
            1
        };
        let mut value = 0;
        while let Some(digit) = c {
            if !digit.is_ascii_digit() {
                break;
            }
            value = value * 10 + i32::from(digit - b'0');
            c = self.byte();
        }
        value * sign
    }
}

fn popped_coins(operations: &[i32], output: &mut impl Write) {
    let mut remaining = operations
        .iter()
        .filter(|&&operation| operation == -1)
        .count();
    if remaining == 0 {
        return;
    }
    let capacity = remaining;
    let mut coins = vec![0; capacity];
    let mut bottom = 0;
    let mut size = 0;
    for &operation in operations {
        if remaining == 0 {
            break;
        }
        if operation > 0 {
            if size == remaining {
                bottom = (bottom + 1) % capacity;
                size -= 1;
            }
            coins[(bottom + size) % capacity] = operation;
            size += 1;
        } else if operation == -1 {
            remaining -= 1;
            size -= 1;
            writeln!(output, "{}", coins[(bottom + size) % capacity]).unwrap();
        } else {
            let extra = size.min(remaining - size);
            let new_bottom = (bottom + capacity - extra) % capacity;
            let mut source = (bottom + size - extra) % capacity;
            let mut destination = new_bottom;
            for _ in 0..extra {
                coins[destination] = coins[source];
                source += 1;
                destination += 1;
                if source == capacity {
                    source = 0;
                }
                if destination == capacity {
                    destination = 0;
                }
            }
            bottom = new_bottom;
            size += extra;
        }
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
    let count = input.next() as usize;
    let operations: Vec<i32> = (0..count).map(|_| input.next()).collect();
    let stdout = io::stdout();
    let mut output = io::BufWriter::with_capacity(BUFFER_SIZE, stdout.lock());
    popped_coins(&operations, &mut output);
}
