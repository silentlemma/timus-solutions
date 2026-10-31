use std::io::{self, Read};

// refills keep input memory constant, including for the largest cases.
const INPUT_BUFFER: usize = 4096;
struct Input<R> {
    reader: R,
    buffer: [u8; INPUT_BUFFER],
    pos: usize,
    len: usize,
}
impl<R: Read> Input<R> {
    fn new(reader: R) -> Self {
        Self {
            reader,
            buffer: [0; INPUT_BUFFER],
            pos: 0,
            len: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.pos == self.len {
            self.len = self.reader.read(&mut self.buffer).unwrap();
            self.pos = 0;
            if self.len == 0 {
                return 0;
            }
        }
        let c = self.buffer[self.pos];
        self.pos += 1;
        c
    }
    fn next(&mut self) -> usize {
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
    let mut input = Input::new(stdin.lock());
    let (n, m) = (input.next(), input.next());
    // subject numbers are at most 1000 and fit u16 exactly.
    let rules: Vec<(u16, u16)> = (0..m)
        .map(|_| (input.next() as u16, input.next() as u16))
        .collect();
    let mut place = vec![0; n + 1];
    for i in 0..n {
        place[input.next()] = i;
    }
    // the plan is right exactly when every rule points forward in it; a
    // rule from a subject to itself can never hold
    let ok = rules
        .iter()
        .all(|&(a, b)| place[usize::from(a)] < place[usize::from(b)]);
    println!("{}", if ok { "YES" } else { "NO" });
}
