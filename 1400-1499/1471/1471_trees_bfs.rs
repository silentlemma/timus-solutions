use std::io::{self, Read, Write};

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
    let n = input.next() as usize;
    let mut edges = vec![Vec::new(); n];
    for _ in 1..n {
        let (u, v, w) = (input.next() as usize, input.next() as usize, input.next());
        edges[u].push((v, w));
        edges[v].push((u, w));
    }
    let mut parent = vec![usize::MAX; n];
    let mut depth = vec![0; n];
    let mut distance = vec![0; n];
    let mut size = vec![1; n];
    let mut heavy = vec![usize::MAX; n];
    let mut top = vec![0; n];
    let mut order = Vec::with_capacity(n);
    order.push(0);
    // n <= 50000 and weights <= 1000 keep distance sums below 100 million.
    for i in 0..n {
        let v = order[i];
        for &(u, w) in &edges[v] {
            if u != parent[v] {
                parent[u] = v;
                depth[u] = depth[v] + 1;
                distance[u] = distance[v] + w;
                order.push(u);
            }
        }
    }
    for i in (1..n).rev() {
        let v = order[i];
        let p = parent[v];
        size[p] += size[v];
        if heavy[p] == usize::MAX || size[v] > size[heavy[p]] {
            heavy[p] = v;
        }
    }
    // each light-edge jump at least doubles the subtree size.
    for &v in order.iter().skip(1) {
        top[v] = if heavy[parent[v]] == v {
            top[parent[v]]
        } else {
            v
        };
    }
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    let m = input.next();
    for _ in 0..m {
        let (mut a, mut b) = (input.next() as usize, input.next() as usize);
        let answer = distance[a] + distance[b];
        while top[a] != top[b] {
            if depth[top[a]] < depth[top[b]] {
                std::mem::swap(&mut a, &mut b);
            }
            a = parent[top[a]];
        }
        if depth[a] > depth[b] {
            a = b;
        }
        writeln!(out, "{}", answer - 2 * distance[a]).unwrap();
    }
}
