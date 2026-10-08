use std::io::{self, Read};

const TOKENS_PER_BRANCH: usize = 3;

// best[k]: the most apples on k branches kept in the subtree of v, all of
// them connected to v; the vector is only as long as k can go
fn solve(adj: &[Vec<(usize, i64)>], q: usize, v: usize, parent: usize) -> Vec<i64> {
    let mut best = vec![0];
    for &(child, apples) in &adj[v] {
        if child == parent {
            continue;
        }
        let sub = solve(adj, q, child, v);
        let size = (best.len() + sub.len()).min(q + 1);
        let mut merged = vec![-1; size];
        for (i, &a) in best.iter().enumerate() {
            // taking j >= 1 branches on the child's side: its edge and j - 1 below
            for j in 0..=sub.len().min(size - 1 - i) {
                let gain = if j == 0 { 0 } else { apples + sub[j - 1] };
                merged[i + j] = merged[i + j].max(a + gain);
            }
        }
        best = merged;
    }
    best
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, q) = (v[0] as usize, v[1] as usize);
    let mut adj = vec![Vec::new(); n + 1];
    for e in v[2..].chunks(TOKENS_PER_BRANCH).take(n - 1) {
        let (a, b) = (e[0] as usize, e[1] as usize);
        adj[a].push((b, e[2]));
        adj[b].push((a, e[2]));
    }
    println!("{}", solve(&adj, q, 1, 0)[q]);
}
