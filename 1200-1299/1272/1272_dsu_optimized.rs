use std::io::{self, Read};

fn find(parent: &mut [usize], mut x: usize) -> usize {
    while parent[x] != x {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    x
}

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
    let (n, k) = (input.next(), input.next());
    let m = input.next();
    let mut parent: Vec<usize> = (0..=n).collect();
    // tunnels are free; every bridge joins two of the remaining groups
    let mut groups = n;
    for _ in 0..k {
        let a = find(&mut parent, input.next());
        let b = find(&mut parent, input.next());
        if a != b {
            parent[a] = b;
            groups -= 1;
        }
    }
    // bridges do not change tunnel components; still consume every pair.
    for _ in 0..m {
        input.next();
        input.next();
    }
    println!("{}", groups - 1);
}
