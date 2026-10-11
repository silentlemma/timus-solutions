use std::io::{self, Read, Write};

// A stack is a chain of blocks of BLOCK values, the newest block first. Only
// the newest block of a stack can be partly full, so the blocks in use never
// exceed OPS / BLOCK + STACKS, which keeps everything well under 0.75 MB.
const STACKS: usize = 1000;
const OPS: usize = 100000;
const BLOCK: usize = 10;
const BLOCKS: usize = OPS / BLOCK + STACKS + 1;
const NONE: u16 = u16::MAX;
const BASE: u32 = 10;
// small fixed buffers for reading and writing, cheap next to the blocks
const BUFFER: usize = 1 << 14;
const DIGITS: usize = 12;

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

    fn number(&mut self) -> u32 {
        let mut c = self.byte();
        while !c.is_ascii_digit() {
            c = self.byte();
        }
        let mut v = 0;
        while c.is_ascii_digit() {
            v = v * BASE + u32::from(c - b'0');
            c = self.byte();
        }
        v
    }
}

struct Output {
    buf: [u8; BUFFER],
    len: usize,
}

impl Output {
    fn flush(&mut self) {
        io::stdout()
            .lock()
            .write_all(&self.buf[..self.len])
            .unwrap();
        self.len = 0;
    }

    fn number(&mut self, mut v: u32) {
        if self.len + DIGITS > BUFFER {
            self.flush();
        }
        let mut digits = [0u8; DIGITS];
        let mut k = 0;
        loop {
            digits[k] = b'0' + (v % BASE) as u8;
            k += 1;
            v /= BASE;
            if v == 0 {
                break;
            }
        }
        while k > 0 {
            k -= 1;
            self.buf[self.len] = digits[k];
            self.len += 1;
        }
        self.buf[self.len] = b'\n';
        self.len += 1;
    }
}

struct Stacks {
    values: Vec<[u32; BLOCK]>, // the blocks, used or free
    below: Vec<u16>,           // the next older block of the same stack
    top: Vec<u16>,             // the newest block of every stack
    size: Vec<usize>,
    free: u16, // the first unused block, the rest chained after it
}

impl Stacks {
    fn new() -> Stacks {
        let mut below = vec![NONE; BLOCKS];
        for (b, next) in below.iter_mut().enumerate().take(BLOCKS - 1) {
            *next = (b + 1) as u16;
        }
        Stacks {
            values: vec![[0; BLOCK]; BLOCKS],
            below,
            top: vec![NONE; STACKS + 1],
            size: vec![0; STACKS + 1],
            free: 0,
        }
    }

    fn push(&mut self, st: usize, v: u32) {
        if self.size[st] % BLOCK == 0 {
            let b = self.free;
            self.free = self.below[b as usize];
            self.below[b as usize] = self.top[st];
            self.top[st] = b;
        }
        self.values[self.top[st] as usize][self.size[st] % BLOCK] = v;
        self.size[st] += 1;
    }

    fn pop(&mut self, st: usize) -> u32 {
        self.size[st] -= 1;
        let b = self.top[st];
        let v = self.values[b as usize][self.size[st] % BLOCK];
        if self.size[st] % BLOCK == 0 {
            self.top[st] = self.below[b as usize];
            self.below[b as usize] = self.free;
            self.free = b;
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
    let mut output = Output {
        buf: [0; BUFFER],
        len: 0,
    };
    let mut stacks = Stacks::new();
    let n = input.number();
    for _ in 0..n {
        // PUSH has a U, POP an O, as their second letter
        let mut c = input.byte();
        while c != b'U' && c != b'O' {
            c = input.byte();
        }
        let st = input.number() as usize;
        if c == b'U' {
            let v = input.number();
            stacks.push(st, v);
        } else {
            output.number(stacks.pop(st));
        }
    }
    output.flush();
}
