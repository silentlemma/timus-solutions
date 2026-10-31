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

fn main() {
    let stdin = io::stdin();
    let mut input = Input::new(stdin.lock());
    let n = input.number() as usize;
    let m = input.number();
    let width = n + 1;
    // costs are 1..10000; zero represents an absent edge in the compact matrix.
    let mut cost = vec![0u16; width * width];
    let mut indegree = vec![0; width];
    for _ in 0..m {
        let a = input.number() as usize;
        let b = input.number() as usize;
        cost[a * width + b] = input.number() as u16;
        indegree[b] += 1;
    }
    let start = input.number() as usize;
    let finish = input.number() as usize;
    // at most 499 edges of cost 10000 keep path sums within signed 32 bits.
    let mut best = vec![-1i32; width];
    best[start] = 0;
    let mut order: Vec<usize> = (1..=n).filter(|&v| indegree[v] == 0).collect();
    let mut at = 0;
    while at < order.len() {
        let v = order[at];
        at += 1;
        for w in 1..=n {
            let c = i32::from(cost[v * width + w]);
            if c == 0 {
                continue;
            }
            if best[v] >= 0 && best[v] + c > best[w] {
                best[w] = best[v] + c;
            }
            indegree[w] -= 1;
            if indegree[w] == 0 {
                order.push(w);
            }
        }
    }
    if best[finish] < 0 {
        println!("No solution");
    } else {
        println!("{}", best[finish]);
    }
}
