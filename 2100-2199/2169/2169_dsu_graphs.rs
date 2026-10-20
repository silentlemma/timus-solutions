use std::io::{self, Read};

const MODULUS: u64 = 1_000_000_007;
const MAX_INCOMING: usize = 3;
const MAX_DEGREE: usize = MAX_INCOMING + 1;

struct DisjointSet {
    parent: Vec<usize>,
    size: Vec<usize>,
    edges: Vec<usize>,
}

impl DisjointSet {
    fn new(count: usize) -> Self {
        Self {
            parent: (0..count).collect(),
            size: vec![1; count],
            edges: vec![0; count],
        }
    }

    fn find(&mut self, mut vertex: usize) -> usize {
        while self.parent[vertex] != vertex {
            self.parent[vertex] = self.parent[self.parent[vertex]];
            vertex = self.parent[vertex];
        }
        vertex
    }

    fn add_edge(&mut self, first: usize, second: usize) {
        let mut first_root = self.find(first);
        let mut second_root = self.find(second);
        if first_root == second_root {
            self.edges[first_root] += 1;
            return;
        }
        if self.size[first_root] < self.size[second_root] {
            std::mem::swap(&mut first_root, &mut second_root);
        }
        self.parent[second_root] = first_root;
        self.size[first_root] += self.size[second_root];
        self.edges[first_root] += self.edges[second_root] + 1;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let vertex_count: usize = tokens.next().unwrap().parse().unwrap();
    let edge_count: usize = tokens.next().unwrap().parse().unwrap();
    let mut components = DisjointSet::new(vertex_count);
    let mut degree = vec![0; vertex_count];
    for _ in 0..edge_count {
        let first = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        let second = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        degree[first] += 1;
        degree[second] += 1;
        components.add_edge(first, second);
    }

    let mut sinks = vec![0_u64; vertex_count];
    for (vertex, &vertex_degree) in degree.iter().enumerate() {
        if vertex_degree > MAX_DEGREE {
            println!("0");
            return;
        }
        if vertex_degree <= MAX_INCOMING {
            sinks[components.find(vertex)] += 1;
        }
    }

    let mut answer = 1;
    for (root, &sink_count) in sinks.iter().enumerate() {
        if components.parent[root] != root {
            continue;
        }
        if components.edges[root] > components.size[root] {
            answer = 0;
            break;
        }
        // Trees choose a sink; a single cycle chooses its direction.
        let choices = if components.edges[root] == components.size[root] {
            2
        } else {
            sink_count
        };
        answer = answer * choices % MODULUS;
    }
    println!("{}", answer);
}
