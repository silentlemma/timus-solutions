use std::io::{self, Read, Write};

const MODULUS: i64 = 1_000_000_007;

struct Network {
    direct: Vec<i64>,
    broadcast: Vec<i64>,
    parent: Vec<usize>,
    root: usize,
}

impl Network {
    fn new(initial: &[i64], edges: &[(usize, usize)], root: usize) -> Self {
        let size = initial.len();
        let mut neighbors = vec![Vec::new(); size];
        for &(a, b) in edges {
            neighbors[a].push(b);
            neighbors[b].push(a);
        }
        let mut parent = vec![size; size];
        parent[root] = root;
        let mut order = Vec::with_capacity(size);
        order.push(root);
        let mut at = 0;
        while at < order.len() {
            let vertex = order[at];
            for &next in &neighbors[vertex] {
                if parent[next] == size {
                    parent[next] = vertex;
                    order.push(next);
                }
            }
            at += 1;
        }
        Self {
            direct: initial.to_vec(),
            broadcast: vec![0; size],
            parent,
            root,
        }
    }

    fn process(&mut self, kind: usize, vertex: usize) -> i64 {
        let mut value = self.direct[vertex];
        if vertex != self.root {
            value += self.broadcast[self.parent[vertex]];
            if value >= MODULUS {
                value -= MODULUS;
            }
        }
        if kind == 2 {
            return value;
        }
        self.broadcast[vertex] += value;
        if self.broadcast[vertex] >= MODULUS {
            self.broadcast[vertex] -= MODULUS;
        }
        if vertex != self.root {
            let above = self.parent[vertex];
            self.direct[above] += value;
            if self.direct[above] >= MODULUS {
                self.direct[above] -= MODULUS;
            }
        }
        -1
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let size: usize = match tokens.next() {
        Some(word) => word.parse().unwrap(),
        None => return,
    };
    let initial: Vec<i64> = (0..size)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let edges: Vec<(usize, usize)> = (1..size)
        .map(|_| {
            let a: usize = tokens.next().unwrap().parse().unwrap();
            let b: usize = tokens.next().unwrap().parse().unwrap();
            (a - 1, b - 1)
        })
        .collect();
    let mut network = Network::new(&initial, &edges, 0);
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let stdout = io::stdout();
    let mut output = io::BufWriter::new(stdout.lock());
    for _ in 0..count {
        let kind: usize = tokens.next().unwrap().parse().unwrap();
        let vertex: usize = tokens.next().unwrap().parse().unwrap();
        let answer = network.process(kind, vertex - 1);
        if answer >= 0 {
            writeln!(output, "{}", answer).unwrap();
        }
    }
}
