use std::io::{self, Read};

// at most 29 transitions of magnitude 32768 keep finite costs below this sentinel.
const INF: i64 = 1000000;

const INPUT_BUFFER: usize = 4096;
// the refillable buffer holds only a chunk, never the complete input.
struct Reader<R> {
    input: R,
    buffer: [u8; INPUT_BUFFER],
    at: usize,
    size: usize,
}
impl<R: Read> Reader<R> {
    fn new(input: R) -> Self {
        Self {
            input,
            buffer: [0; INPUT_BUFFER],
            at: 0,
            size: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.at == self.size {
            self.size = self.input.read(&mut self.buffer).unwrap();
            self.at = 0;
            if self.size == 0 {
                return 0;
            }
        }
        let c = self.buffer[self.at];
        self.at += 1;
        c
    }
    fn next(&mut self) -> i32 {
        let mut c = self.byte();
        while c != 0 && c != b'-' && !c.is_ascii_digit() {
            c = self.byte();
        }
        let mut sign = 1;
        if c == b'-' {
            sign = -1;
            c = self.byte();
        }
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
    let mut input = Reader::new(stdin.lock());
    let mut it = std::iter::from_fn(|| Some(i64::from(input.next())));
    let levels = it.next().unwrap();
    // the cheapest cost of reaching each planet of the current level
    let mut cost = vec![0i64];
    for _ in 0..levels {
        let k = it.next().unwrap() as usize;
        let mut nxt = vec![INF; k];
        for best in nxt.iter_mut() {
            loop {
                let src = it.next().unwrap() as usize;
                if src == 0 {
                    break;
                }
                let price = it.next().unwrap();
                if cost[src - 1] < INF {
                    *best = (*best).min(cost[src - 1] + price);
                }
            }
        }
        cost = nxt;
    }
    println!("{}", cost.iter().min().unwrap());
}
