use std::collections::VecDeque;
use std::io::{self, Read, Write};

const IDS: usize = 32768; // station indices go up to 32767

fn bfs(adj: &[Vec<usize>], start: usize) -> Vec<i64> {
    let mut dist = vec![-1i64; IDS];
    let mut queue = VecDeque::new();
    dist[start] = 0;
    queue.push_back(start);
    while let Some(u) = queue.pop_front() {
        for &v in &adj[u] {
            if dist[v] < 0 {
                dist[v] = dist[u] + 1;
                queue.push_back(v);
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
    let mut adj = vec![Vec::new(); IDS];
    let mut present = vec![false; IDS];
    let n = it.next().unwrap();
    for _ in 0..n {
        let k = it.next().unwrap();
        let line: Vec<usize> = (0..k).map(|_| it.next().unwrap() as usize).collect();
        for &s in &line {
            present[s] = true;
        }
        for pair in line.windows(2) {
            adj[pair[0]].push(pair[1]);
            adj[pair[1]].push(pair[0]);
        }
    }
    let m = it.next().unwrap();
    let seen: Vec<i64> = (0..m).map(|_| it.next().unwrap()).collect();
    // the stations seen must be a walk through the network ...
    for (i, &s) in seen.iter().enumerate() {
        if s < 0 || s as usize >= IDS || !present[s as usize] {
            return;
        }
        if i > 0 && !adj[seen[i - 1] as usize].contains(&(s as usize)) {
            return;
        }
    }
    let (start, end) = (seen[0] as usize, seen[seen.len() - 1] as usize);
    let first = bfs(&adj, start);
    // ... and a shortest one, or no target fits it
    if first[end] != m - 1 {
        return;
    }
    let last = bfs(&adj, end);
    let mut out = io::BufWriter::new(io::stdout().lock());
    // a target fits when the walk can go on to it along a shortest path
    for t in 0..IDS {
        if first[t] >= 0 && last[t] >= 0 && first[t] == m - 1 + last[t] {
            writeln!(out, "{}", t).unwrap();
        }
    }
}
