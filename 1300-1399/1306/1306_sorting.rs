use std::collections::BinaryHeap;
use std::io::{self, Read, Write};

// a small fixed input buffer: the memory limit is one megabyte
const BUFFER: usize = 1 << 12;
const BASE: u64 = 10;

struct Input {
    buf: [u8; BUFFER],
    len: usize,
    pos: usize,
}

impl Input {
    // the next byte, or 0 at the end of the input
    fn byte(&mut self) -> u8 {
        if self.pos == self.len {
            self.len = io::stdin().lock().read(&mut self.buf).unwrap_or(0);
            self.pos = 0;
            if self.len == 0 {
                return 0;
            }
        }
        self.pos += 1;
        self.buf[self.pos - 1]
    }

    fn number(&mut self) -> u64 {
        let mut c = self.byte();
        while !c.is_ascii_digit() {
            c = self.byte();
        }
        let mut v = 0;
        while c.is_ascii_digit() {
            v = v * BASE + u64::from(c - b'0');
            c = self.byte();
        }
        v
    }
}

fn main() {
    let mut input = Input {
        buf: [0; BUFFER],
        len: 0,
        pos: 0,
    };
    let n = input.number() as usize;
    // the n / 2 + 1 smallest numbers seen so far, as a max-heap: half the
    // input is enough, because the median is the largest or second largest
    let keep = n / 2 + 1;
    let mut heap: BinaryHeap<u32> = BinaryHeap::with_capacity(keep);
    for _ in 0..n {
        let x = input.number() as u32;
        if heap.len() < keep {
            heap.push(x);
        } else if let Some(mut top) = heap.peek_mut() {
            if x < *top {
                *top = x;
            }
        }
    }
    let top = u64::from(heap.pop().unwrap_or(0));
    let answer = if n % 2 == 1 {
        format!("{}.0", top)
    } else {
        let sum = top + u64::from(heap.pop().unwrap_or(0));
        format!("{}.{}", sum / 2, if sum % 2 == 1 { "5" } else { "0" })
    };
    io::stdout().write_all(answer.as_bytes()).unwrap();
    io::stdout().write_all(b"\n").unwrap();
}
