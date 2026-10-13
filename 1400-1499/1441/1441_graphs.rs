use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let mut ends: Vec<usize> = it.take(2 * m).collect();
    let mut degree = vec![0usize; n + 1];
    for &v in &ends {
        degree[v] += 1;
    }
    // vertex 0 is a helper joined to every room with an odd number of tunnels
    for v in 1..=n {
        if degree[v] % 2 == 1 {
            ends.push(0);
            ends.push(v);
        }
    }
    let edges = ends.len() / 2;
    let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n + 1];
    for e in 0..edges {
        adj[ends[2 * e]].push(e);
        adj[ends[2 * e + 1]].push(e);
    }
    // an Euler circuit, found without recursion
    let mut used = vec![false; edges];
    let mut pos = vec![0usize; n + 1];
    let mut stack = vec![if adj[0].is_empty() { 1 } else { 0 }];
    let mut circuit = Vec::new();
    while let Some(&v) = stack.last() {
        while pos[v] < adj[v].len() && used[adj[v][pos[v]]] {
            pos[v] += 1;
        }
        if pos[v] == adj[v].len() {
            circuit.push(v);
            stack.pop();
            continue;
        }
        let e = adj[v][pos[v]];
        used[e] = true;
        stack.push(ends[2 * e] + ends[2 * e + 1] - v);
    }
    // the helper edges cut the circuit into trails of real tunnels
    let trails: Vec<String> = circuit
        .split(|&v| v == 0)
        .filter(|t| !t.is_empty())
        .map(|t| {
            t.iter()
                .map(|v| v.to_string())
                .collect::<Vec<_>>()
                .join(" ")
        })
        .collect();
    let mut out = format!("{}\n", trails.len());
    for t in &trails {
        out.push_str(t);
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
