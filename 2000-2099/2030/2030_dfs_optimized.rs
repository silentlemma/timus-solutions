use std::io::{self, Read, Write};

const INPUT_SIZE: usize = 4096;
const OUTPUT_SIZE: usize = 8192;

struct Input<R: Read> {
    stream: R,
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> Input<R> {
    fn next(&mut self) -> u8 {
        if self.position == self.length {
            self.length = self.stream.read(&mut self.bytes).unwrap();
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let c = self.bytes[self.position];
        self.position += 1;
        c
    }

    fn number(&mut self) -> u32 {
        let mut c = self.next();
        while c != 0 && c <= b' ' {
            c = self.next();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + u32::from(c - b'0');
            c = self.next();
        }
        value
    }
}

const MODULUS: u32 = 1_000_000_007;

fn add_mod(a: u32, b: u32) -> u32 {
    let sum = a + b;
    if sum >= MODULUS {
        sum - MODULUS
    } else {
        sum
    }
}

#[derive(Clone, Copy)]
struct Edge {
    next: u32,
    vertex: u32,
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        stream: stdin.lock(),
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let n = input.number() as usize;
    let mut direct = vec![0_u32; n + 1];
    let mut parent = vec![0_u32; n + 1];
    for value in &mut direct[1..] {
        *value = input.number();
    }
    {
        let mut head = vec![0_u32; n + 1];
        let mut edges = vec![Edge { next: 0, vertex: 0 }; 2 * n - 1];
        let mut used = 0;
        for _ in 1..n {
            let a = input.number() as usize;
            let b = input.number() as usize;
            used += 1;
            edges[used] = Edge {
                next: head[a],
                vertex: b as u32,
            };
            head[a] = used as u32;
            used += 1;
            edges[used] = Edge {
                next: head[b],
                vertex: a as u32,
            };
            head[b] = used as u32;
        }
        let mut order = Vec::with_capacity(n);
        order.push(1_u32);
        let mut at = 0;
        while at < order.len() {
            let vertex = order[at] as usize;
            at += 1;
            let mut edge = head[vertex];
            while edge != 0 {
                let target = edges[edge as usize].vertex;
                if target != parent[vertex] {
                    parent[target as usize] = vertex as u32;
                    order.push(target);
                }
                edge = edges[edge as usize].next;
            }
        }
    }
    let mut broadcast = vec![0_u32; n + 1];
    let stdout = io::stdout();
    let mut output = io::BufWriter::with_capacity(OUTPUT_SIZE, stdout.lock());
    let count = input.number();
    for _ in 0..count {
        let kind = input.number();
        let vertex = input.number() as usize;
        let above = parent[vertex] as usize;
        let value = add_mod(direct[vertex], broadcast[above]);
        if kind == 2 {
            writeln!(output, "{}", value).unwrap();
        } else {
            broadcast[vertex] = add_mod(broadcast[vertex], value);
            // Sentinel direct[0] is unused; broadcast[0] stays zero, also for a one-node tree.
            direct[above] = add_mod(direct[above], value);
        }
    }
    output.flush().unwrap();
}
