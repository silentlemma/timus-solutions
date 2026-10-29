use std::io::{self, Read};

const PLAYERS: usize = 3;
const BUFFER_SIZE: usize = 1 << 10;

// the numbers are parsed by hand from a 1 KB buffer
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

fn main() {
    let stdin = io::stdin();
    let mut input = Input::new(stdin.lock());
    let mut size = input.number() as usize;
    let mut common: Vec<u32> = (0..size).map(|_| input.number()).collect();
    // walk the sorted intersection and each next list together, always moving past the
    // smallest current number
    for _ in 1..PLAYERS {
        let n = input.number();
        let mut at = 0;
        let mut kept = 0;
        for _ in 0..n {
            let value = input.number();
            while at < size && common[at] < value {
                at += 1;
            }
            // kept never overtakes at, so the stored numbers not yet compared stay intact
            if at < size && common[at] == value {
                common[kept] = value;
                kept += 1;
                at += 1;
            }
        }
        size = kept;
    }
    println!("{}", size);
}
