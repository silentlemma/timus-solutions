use std::io::{self, Read};

const BUFFER_SIZE: usize = 65_536;
const UNKNOWN: i64 = -1;

struct FastInput<R: Read> {
    reader: R,
    buffer: [u8; BUFFER_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> FastInput<R> {
    fn new(reader: R) -> Self {
        Self {
            reader,
            buffer: [0; BUFFER_SIZE],
            position: 0,
            length: 0,
        }
    }

    fn read_byte(&mut self) -> u8 {
        if self.position == self.length {
            self.length = self.reader.read(&mut self.buffer).unwrap();
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let value = self.buffer[self.position];
        self.position += 1;
        value
    }

    fn next_int(&mut self) -> i64 {
        let mut current = self.read_byte();
        while current <= b' ' {
            current = self.read_byte();
        }
        let negative = current == b'-';
        if negative {
            current = self.read_byte();
        }
        let mut value = 0;
        while current.is_ascii_digit() {
            value = value * 10 + i64::from(current - b'0');
            current = self.read_byte();
        }
        if negative {
            -value
        } else {
            value
        }
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = FastInput::new(stdin.lock());
    let n = input.next_int();
    let mut unknown_count = 0;
    let mut unknown_labels = 0;
    let mut known_occurrences = 0;
    let mut known_weight = 0;
    for label in 1..=n {
        let degree = input.next_int();
        if degree == UNKNOWN {
            unknown_count += 1;
            unknown_labels += label;
        } else {
            let occurrences = degree - 1;
            known_occurrences += occurrences;
            known_weight += label * occurrences;
        }
    }
    let mut answer = n * (n + 1) / 2 + n * known_weight;
    if unknown_count > 0 {
        let remaining = n - 2 - known_occurrences;
        let multiplier = n * remaining;
        // Divide the label sum first to keep every product in signed 64 bits.
        answer += multiplier * (unknown_labels / unknown_count);
        answer += multiplier * (unknown_labels % unknown_count) / unknown_count;
    }
    println!("{answer}");
}
