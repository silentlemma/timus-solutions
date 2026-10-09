use std::collections::VecDeque;
use std::fmt::Write as _;
use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let ends: Vec<(usize, usize)> = (0..m)
        .map(|_| (it.next().unwrap(), it.next().unwrap()))
        .collect();
    let mut adj = vec![Vec::new(); n + 1];
    for (i, &(a, b)) in ends.iter().enumerate() {
        adj[a].push((b, i));
        adj[b].push((a, i));
    }
    let mut parent = vec![0usize; n + 1];
    let mut depth = vec![usize::MAX; n + 1];
    let mut tree = vec![false; m];
    // a breadth-first forest keeps the tree paths, and so the tours, short
    for root in 1..=n {
        if depth[root] != usize::MAX {
            continue;
        }
        depth[root] = 0;
        let mut queue = VecDeque::from([root]);
        while let Some(u) = queue.pop_front() {
            for &(v, i) in &adj[u] {
                if depth[v] == usize::MAX {
                    depth[v] = depth[u] + 1;
                    parent[v] = u;
                    tree[i] = true;
                    queue.push_back(v);
                }
            }
        }
    }
    let mut out = String::new();
    let mut count = 0;
    // every road outside the forest closes its own tour with the tree path
    for (i, &(mut a, mut b)) in ends.iter().enumerate() {
        if tree[i] {
            continue;
        }
        let (mut left, mut right) = (Vec::new(), Vec::new());
        while depth[a] > depth[b] {
            left.push(a);
            a = parent[a];
        }
        while depth[b] > depth[a] {
            right.push(b);
            b = parent[b];
        }
        while a != b {
            left.push(a);
            right.push(b);
            a = parent[a];
            b = parent[b];
        }
        left.push(a);
        left.extend(right.iter().rev());
        write!(out, "{}", left.len()).unwrap();
        for c in &left {
            write!(out, " {}", c).unwrap();
        }
        out.push_str("\n");
        count += 1;
    }
    io::stdout()
        .write_all(format!("{}\n{}", count, out).as_bytes())
        .unwrap();
}
