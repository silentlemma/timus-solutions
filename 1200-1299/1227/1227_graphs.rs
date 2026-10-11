use std::io::{self, Read};

fn find(parent: &mut [usize], mut v: usize) -> usize {
    while parent[v] != v {
        parent[v] = parent[parent[v]];
        v = parent[v];
    }
    v
}

// Distances from start within its tree, -1 elsewhere.
fn distances(adj: &[Vec<(usize, i64)>], start: usize) -> Vec<i64> {
    let mut dist = vec![-1i64; adj.len()];
    dist[start] = 0;
    let mut stack = vec![start];
    while let Some(v) = stack.pop() {
        for &(u, r) in &adj[v] {
            if dist[u] < 0 {
                dist[u] = dist[v] + r;
                stack.push(u);
            }
        }
    }
    dist
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let (m, n, s) = (
        it.next().unwrap() as usize,
        it.next().unwrap(),
        it.next().unwrap(),
    );
    let mut parent: Vec<usize> = (0..=m).collect();
    let mut adj = vec![Vec::new(); m + 1];
    for _ in 0..n {
        let (p, q, r) = (
            it.next().unwrap() as usize,
            it.next().unwrap() as usize,
            it.next().unwrap(),
        );
        let (a, b) = (find(&mut parent, p), find(&mut parent, q));
        if a == b {
            // a cycle, a loop or a second road: drive round it as long as needed
            println!("YES");
            return;
        }
        parent[a] = b;
        adj[p].push((q, r));
        adj[q].push((p, r));
    }
    // a forest: the longest route is a diameter of one of its trees
    let mut best = 0;
    let mut seen = vec![false; m + 1];
    for v in 1..=m {
        if seen[v] {
            continue;
        }
        let d = distances(&adj, v);
        let mut end = v;
        for u in 1..=m {
            if d[u] >= 0 {
                seen[u] = true;
                if d[u] > d[end] {
                    end = u;
                }
            }
        }
        best = best.max(*distances(&adj, end).iter().max().unwrap());
    }
    println!("{}", if best >= s { "YES" } else { "NO" });
}
