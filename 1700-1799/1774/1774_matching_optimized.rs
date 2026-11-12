use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const SHAVES: usize = 2;
const MAX_TIME: usize = 2000;
const OUTPUT_RESERVE: usize = 1200;

#[derive(Clone, Copy, Default)]
struct Edge {
    to: u16,
    next: u16,
    cap: u16,
}

struct Flow {
    edges: Vec<Edge>,
    head: Vec<u16>,
    at: Vec<u16>,
    level: Vec<u16>,
    queue: Vec<u16>,
}

impl Flow {
    fn new(nodes: usize, edge_count: usize) -> Self {
        let mut edges = Vec::with_capacity(edge_count);
        edges.resize(SHAVES, Edge::default());
        Self {
            edges,
            head: vec![0; nodes],
            at: vec![0; nodes],
            level: vec![0; nodes],
            queue: vec![0; nodes],
        }
    }

    fn add(&mut self, a: usize, b: usize, cap: usize) {
        self.edges.push(Edge {
            to: b as u16,
            next: self.head[a],
            cap: cap as u16,
        });
        self.head[a] = (self.edges.len() - 1) as u16;
        self.edges.push(Edge {
            to: a as u16,
            next: self.head[b],
            cap: 0,
        });
        self.head[b] = (self.edges.len() - 1) as u16;
    }

    fn push(&mut self, v: usize, sink: usize, limit: u16) -> u16 {
        if v == sink {
            return limit;
        }
        while self.at[v] != 0 {
            let e = self.at[v] as usize;
            let w = self.edges[e].to as usize;
            if self.edges[e].cap != 0 && self.level[w] == self.level[v] + 1 {
                let got = self.push(w, sink, limit.min(self.edges[e].cap));
                if got != 0 {
                    self.edges[e].cap -= got;
                    self.edges[e ^ 1].cap += got;
                    return got;
                }
            }
            self.at[v] = self.edges[e].next;
        }
        0
    }

    fn solve(&mut self, sink: usize, need: usize) -> usize {
        let mut total = 0;
        while total < need {
            self.level.fill(0);
            self.at.copy_from_slice(&self.head);
            self.queue[0] = 0;
            self.level[0] = 1;
            let (mut cursor, mut length) = (0, 1);
            while cursor < length {
                let v = self.queue[cursor] as usize;
                cursor += 1;
                let mut e = self.head[v] as usize;
                while e != 0 {
                    let w = self.edges[e].to as usize;
                    if self.edges[e].cap != 0 && self.level[w] == 0 {
                        self.level[w] = self.level[v] + 1;
                        self.queue[length] = w as u16;
                        length += 1;
                    }
                    e = self.edges[e].next as usize;
                }
            }
            if self.level[sink] == 0 {
                break;
            }
            while total < need {
                let got = self.push(0, sink, (need - total) as u16);
                if got == 0 {
                    break;
                }
                total += got as usize;
            }
        }
        total
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_ascii_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let (n, k) = (tokens.next().unwrap(), tokens.next().unwrap());
    let mut start = vec![0; n];
    let mut end = vec![0; n];
    let mut index = [0_u16; MAX_TIME + 1];
    for i in 0..n {
        start[i] = tokens.next().unwrap();
        end[i] = start[i] + tokens.next().unwrap();
        index[start[i]] = 1;
        index[end[i]] = 1;
    }
    let mut cuts = Vec::with_capacity(SHAVES * n);
    for (t, entry) in index.iter_mut().enumerate() {
        if *entry != 0 {
            *entry = cuts.len() as u16;
            cuts.push(t);
        }
    }
    let blocks = cuts.len() - 1;
    let sink = n + blocks + 1;
    let mut edge_count = n + blocks;
    for i in 0..n {
        start[i] = index[start[i]] as usize;
        end[i] = index[end[i]] as usize;
        edge_count += end[i] - start[i];
    }
    let mut flow = Flow::new(sink + 1, SHAVES * (edge_count + 1));
    for i in 0..n {
        flow.add(0, i + 1, SHAVES);
        for j in start[i]..end[i] {
            flow.add(i + 1, n + j + 1, SHAVES.min(cuts[j + 1] - cuts[j]));
        }
    }
    for j in 0..blocks {
        flow.add(
            n + j + 1,
            sink,
            (SHAVES * n).min(k * (cuts[j + 1] - cuts[j])),
        );
    }
    if flow.solve(sink, SHAVES * n) < SHAVES * n {
        println!("No");
        return;
    }
    let mut output = String::with_capacity(OUTPUT_RESERVE);
    output.push_str("Yes\n");
    let mut dealt = vec![0; blocks];
    for i in 1..=n {
        let mut times = [0; SHAVES];
        let mut used = 0;
        let mut e = flow.head[i] as usize;
        while e != 0 {
            let w = flow.edges[e].to as usize;
            if w > n && w < sink {
                let block = w - n - 1;
                for _ in 0..flow.edges[e ^ 1].cap {
                    times[used] = cuts[block] + dealt[block] % (cuts[block + 1] - cuts[block]);
                    used += 1;
                    dealt[block] += 1;
                }
            }
            e = flow.edges[e].next as usize;
        }
        if times[0] > times[1] {
            times.swap(0, 1);
        }
        writeln!(&mut output, "{} {}", times[0], times[1]).unwrap();
    }
    io::stdout().write_all(output.as_bytes()).unwrap();
}
