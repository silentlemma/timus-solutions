use std::collections::VecDeque;
use std::io::{self, Read};

/// Distances from the nearest source and the edges of a tree of shortest
/// paths that grows from the sources.
fn bfs(adj: &[Vec<usize>], sources: &[usize]) -> (Vec<i64>, Vec<(usize, usize)>) {
    let mut dist = vec![-1i64; adj.len()];
    let mut tree = Vec::new();
    let mut queue: VecDeque<usize> = sources.iter().copied().collect();
    for &s in sources {
        dist[s] = 0;
    }
    while let Some(v) = queue.pop_front() {
        for &u in &adj[v] {
            if dist[u] < 0 {
                dist[u] = dist[v] + 1;
                tree.push((v, u));
                queue.push_back(u);
            }
        }
    }
    (dist, tree)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<usize> = text
        .split_ascii_whitespace()
        .map(|w| w.parse().unwrap())
        .collect();
    let (n, m) = (v[0], v[1]);
    let edges: Vec<(usize, usize)> = v[2..]
        .chunks(2)
        .take(m)
        .map(|c| (c[0] - 1, c[1] - 1))
        .collect();
    let mut adj = vec![Vec::new(); n];
    for &(a, b) in &edges {
        adj[a].push(b);
        adj[b].push(a);
    }
    let dist: Vec<Vec<i64>> = (0..n).map(|s| bfs(&adj, &[s]).0).collect();
    // the middle of a tree of least diameter is a node or the middle of an edge, and
    // a tree of shortest paths from there has diameter 2 r or 2 r + 1 for the
    // largest distance r from it, and no tree can do better
    let mut best = i64::MAX;
    let mut centre = vec![0];
    for s in 0..n {
        let reach = 2 * dist[s].iter().max().unwrap();
        if reach < best {
            best = reach;
            centre = vec![s];
        }
    }
    for &(a, b) in &edges {
        let far = (0..n).map(|w| dist[a][w].min(dist[b][w])).max().unwrap();
        if 2 * far + 1 < best {
            best = 2 * far + 1;
            centre = vec![a, b];
        }
    }
    let (_, mut tree) = bfs(&adj, &centre);
    if centre.len() > 1 {
        tree.push((centre[0], centre[1]));
    }
    let out: Vec<String> = tree
        .iter()
        .map(|&(a, b)| format!("{} {}", a + 1, b + 1))
        .collect();
    println!("{}", out.join("\n"));
}
