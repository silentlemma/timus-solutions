use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::fmt::Write as _;
use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let code: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = code.len() + 1;
    // a vertex stays until all its neighbours but one are removed, and each
    // removed neighbour writes the vertex once
    let mut deg = vec![1usize; n + 1];
    for &c in &code {
        deg[c] += 1;
    }
    let mut leaves: BinaryHeap<Reverse<usize>> =
        (1..=n).filter(|&u| deg[u] == 1).map(Reverse).collect();
    let mut adj = vec![Vec::new(); n + 1];
    for &c in &code {
        let Reverse(leaf) = leaves.pop().unwrap();
        adj[leaf].push(c);
        adj[c].push(leaf);
        deg[c] -= 1;
        if deg[c] == 1 {
            leaves.push(Reverse(c));
        }
    }
    let mut out = String::new();
    for u in 1..=n {
        adj[u].sort_unstable();
        write!(out, "{}:", u).unwrap();
        for &x in &adj[u] {
            write!(out, " {}", x).unwrap();
        }
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
