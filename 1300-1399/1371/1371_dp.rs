use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n + 1];
    for _ in 0..n - 1 {
        let (a, b, c) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
        adj[a].push((b, c as i64));
        adj[b].push((a, c as i64));
    }
    // an edge with s branches on one side carries the s (n - s) pairs that
    // it separates; sizes come from a parents-first order read backwards
    let (mut parent, mut cost) = (vec![0usize; n + 1], vec![0i64; n + 1]);
    let mut order = vec![1usize];
    let mut i = 0;
    while i < order.len() {
        let v = order[i];
        for k in 0..adj[v].len() {
            let (u, c) = adj[v][k];
            if u != parent[v] {
                parent[u] = v;
                cost[u] = c;
                order.push(u);
            }
        }
        i += 1;
    }
    let mut size = vec![1i64; n + 1];
    let mut total = 0i64;
    for &v in order.iter().skip(1).rev() {
        size[parent[v]] += size[v];
        total += cost[v] * size[v] * (n as i64 - size[v]);
    }
    // every pair is counted in both directions
    println!("{:.4}", 2.0 * total as f64 / (n as f64 * (n - 1) as f64));
}
