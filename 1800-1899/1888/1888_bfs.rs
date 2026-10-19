use std::collections::VecDeque;
use std::io::{self, Read};

const LONGEST: i32 = 50; // experience is from 1 to 50 years

// distances from start, -1 outside its component
fn distances(adj: &[Vec<usize>], start: usize) -> Vec<i32> {
    let mut dist = vec![-1; adj.len()];
    dist[start] = 0;
    let mut queue = VecDeque::from(vec![start]);
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
    let v: Vec<usize> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let (n, p) = (v[0], v[1]);
    let mut adj = vec![Vec::new(); p + 1];
    for k in 0..n {
        let (a, b) = (v[2 + 2 * k], v[2 + 2 * k + 1]);
        adj[a].push(b);
        adj[b].push(a);
    }
    // the two pilots of a flight differ by exactly one year, so a component
    // must be bipartite; within it no two pilots differ by more than their
    // distance, and BFS layers from one end of a diameter reach it
    let mut seen = vec![false; p + 1];
    let mut roots = Vec::new();
    for s in 1..=p {
        if seen[s] {
            continue;
        }
        let dist = distances(&adj, s);
        for u in 1..=p {
            if dist[u] < 0 {
                continue;
            }
            seen[u] = true;
            if adj[u].iter().any(|&w| (dist[u] - dist[w]) % 2 == 0) {
                println!("-1");
                return;
            }
        }
        roots.push(s);
    }
    let mut years = vec![0i32; p + 1];
    let spread = if roots.len() == 1 {
        let mut spread = -1;
        for s in 1..=p {
            let dist = distances(&adj, s);
            let far = *dist[1..].iter().max().unwrap();
            if far > spread {
                spread = far;
                for u in 1..=p {
                    years[u] = 1 + dist[u];
                }
            }
        }
        spread
    } else {
        // separate groups: one alternates 1 and 2, the others 49 and 50
        for (k, &root) in roots.iter().enumerate() {
            let dist = distances(&adj, root);
            for u in 1..=p {
                if dist[u] >= 0 {
                    years[u] = if k == 0 { 1 + dist[u] % 2 } else { LONGEST - dist[u] % 2 };
                }
            }
        }
        LONGEST - 1
    };
    let line: Vec<String> = years[1..].iter().map(|y| y.to_string()).collect();
    println!("{}\n{}", spread, line.join(" "));
}
