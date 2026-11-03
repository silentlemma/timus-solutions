use std::io::{self, Read, Write};

const UNVISITED: u16 = u16::MAX;

struct Tree {
    head: Vec<u16>,
    to: Vec<u16>,
    following: Vec<u16>,
    ask_head: Vec<u16>,
    ask_next: Vec<u16>,
    distance: Vec<u16>,
    answer: Vec<u16>,
    depth: Vec<u16>,
    path: Vec<u16>,
    stack: Vec<u16>,
}

impl Tree {
    fn walk(&mut self, root: usize) -> usize {
        self.depth.fill(UNVISITED);
        self.depth[root] = 0;
        self.stack[0] = root as u16;
        let (mut top, mut deepest) = (1, root);
        while top > 0 {
            top -= 1;
            let vertex = self.stack[top] as usize;
            let dv = self.depth[vertex];
            self.path[dv as usize] = vertex as u16;
            if dv > self.depth[deepest] {
                deepest = vertex;
            }
            let mut query = self.ask_head[vertex] as usize;
            while query != 0 {
                if self.answer[query] == 0 && self.distance[query] <= dv {
                    self.answer[query] = self.path[(dv - self.distance[query]) as usize];
                }
                query = self.ask_next[query] as usize;
            }
            let mut edge = self.head[vertex] as usize;
            while edge != 0 {
                let child = self.to[edge] as usize;
                if self.depth[child] == UNVISITED {
                    self.depth[child] = dv + 1;
                    self.stack[top] = child as u16;
                    top += 1;
                }
                edge = self.following[edge] as usize;
            }
        }
        deepest
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<usize>().unwrap());
    let (n, q) = (numbers.next().unwrap(), numbers.next().unwrap());
    // Vertex<=20000, edge<=39998, query<=50000: every ID fits u16.
    // One-based list indices reserve zero as the missing-link sentinel.
    let mut tree = Tree {
        head: vec![0; n + 1],
        to: vec![0; 2 * n],
        following: vec![0; 2 * n],
        ask_head: vec![0; n + 1],
        ask_next: vec![0; q + 1],
        distance: vec![0; q + 1],
        answer: vec![0; q + 1],
        depth: vec![0; n + 1],
        path: vec![0; n + 1],
        stack: vec![0; n + 1],
    };
    let mut edge = 0;
    for _ in 0..n - 1 {
        let (a, b) = (numbers.next().unwrap(), numbers.next().unwrap());
        edge += 1;
        tree.to[edge] = b as u16;
        tree.following[edge] = tree.head[a];
        tree.head[a] = edge as u16;
        edge += 1;
        tree.to[edge] = a as u16;
        tree.following[edge] = tree.head[b];
        tree.head[b] = edge as u16;
    }
    for i in 1..=q {
        let vertex = numbers.next().unwrap();
        tree.distance[i] = numbers.next().unwrap() as u16;
        tree.ask_next[i] = tree.ask_head[vertex];
        tree.ask_head[vertex] = i as u16;
    }
    // A path towards one diameter end reaches every feasible distance.
    let a = tree.walk(1);
    let b = tree.walk(a);
    tree.walk(b);
    let stdout = io::stdout();
    let mut output = io::BufWriter::new(stdout.lock());
    for value in &tree.answer[1..] {
        writeln!(output, "{}", value).unwrap();
    }
}
