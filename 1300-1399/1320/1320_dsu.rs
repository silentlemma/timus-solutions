use std::io::{self, Read};

const VERTICES: usize = 1000;

fn find(parent: &mut [usize], mut v: usize) -> usize {
    while parent[v] != v {
        parent[v] = parent[parent[v]];
        v = parent[v];
    }
    v
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let ends: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let mut parent: Vec<usize> = (0..=VERTICES).collect();
    let mut edges = vec![0usize; VERTICES + 1]; // edges of each component, kept at its root
    for pair in ends.chunks_exact(2) {
        let ra = find(&mut parent, pair[0]);
        let rb = find(&mut parent, pair[1]);
        if ra != rb {
            parent[ra] = rb;
            edges[rb] += edges[ra];
        }
        edges[rb] += 1;
    }
    let even = (1..=VERTICES).all(|v| parent[v] != v || edges[v] % 2 == 0);
    println!("{}", if even { 1 } else { 0 });
}
