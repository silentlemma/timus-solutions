use std::io::{self, BufWriter, Read, Write};

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

fn find(parent: &mut [usize], mut v: usize) -> usize {
    while parent[v] != v {
        parent[v] = parent[parent[v]];
        v = parent[v];
    }
    v
}
fn main() {
    let stdin = io::stdin();
    let mut input = Input::new(stdin.lock());
    let (n, m) = (input.next(), input.next());
    // n <= 1000 fits u16; length <= 10^6 fits u32, making each edge eight bytes.
    let mut edges = Vec::with_capacity(m);
    for _ in 0..m {
        let (a, b, length) = (
            input.next() as u16,
            input.next() as u16,
            input.next() as u32,
        );
        edges.push((length, a, b));
    }
    edges.sort_unstable();
    let mut parent: Vec<usize> = (0..=n).collect();
    let mut chosen = Vec::with_capacity(n - 1);
    let mut longest = 0;
    for (length, a, b) in edges {
        let (ra, rb) = (
            find(&mut parent, usize::from(a)),
            find(&mut parent, usize::from(b)),
        );
        if ra != rb {
            parent[ra] = rb;
            chosen.push((a, b));
            longest = length;
            if chosen.len() == n - 1 {
                break;
            }
        }
    }
    let mut out = BufWriter::new(io::stdout().lock());
    writeln!(out, "{}\n{}", longest, chosen.len()).unwrap();
    for (a, b) in chosen {
        writeln!(out, "{} {}", a, b).unwrap();
    }
}
