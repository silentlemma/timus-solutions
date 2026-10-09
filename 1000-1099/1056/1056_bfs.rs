use std::io::{self, Read};

// distances from s and the predecessors on the shortest paths
fn bfs(adj: &[Vec<usize>], s: usize) -> (Vec<i64>, Vec<usize>) {
    let mut dist = vec![-1i64; adj.len()];
    let mut prev = vec![0usize; adj.len()];
    dist[s] = 0;
    let mut queue = vec![s];
    let mut i = 0;
    while i < queue.len() {
        let v = queue[i];
        for &w in &adj[v] {
            if dist[w] < 0 {
                dist[w] = dist[v] + 1;
                prev[w] = v;
                queue.push(w);
            }
        }
        i += 1;
    }
    (dist, prev)
}

fn farthest(dist: &[i64]) -> usize {
    (1..dist.len()).fold(1, |best, v| if dist[v] > dist[best] { v } else { best })
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0];
    let mut adj = vec![Vec::new(); n + 1];
    for i in 2..=n {
        let p = v[i - 1];
        adj[i].push(p);
        adj[p].push(i);
    }
    // the farthest computer from any start is an end of a longest path; the
    // farthest one from it is the other end
    let (dist, _) = bfs(&adj, 1);
    let u = farthest(&dist);
    let (dist, prev) = bfs(&adj, u);
    let end = farthest(&dist);
    // the centers are the middle one or two computers of that path
    let length = dist[end] as usize;
    let mut path = vec![end];
    while path.len() <= length {
        path.push(prev[*path.last().unwrap()]);
    }
    let mut centers = vec![path[length / 2], path[(length + 1) / 2]];
    centers.sort();
    centers.dedup();
    let out: Vec<String> = centers.iter().map(|c| c.to_string()).collect();
    println!("{}", out.join(" "));
}
