use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut edges = Vec::with_capacity(n - 1);
    let mut start = vec![0usize; n + 1];
    for _ in 1..n {
        let (u, v, w) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
        start[u + 1] += 1;
        start[v + 1] += 1;
        edges.push((u, v, w));
    }
    // adjacency lists packed into one array (both directions of each edge)
    for i in 0..n {
        start[i + 1] += start[i];
    }
    let mut fill = start[..n].to_vec();
    let mut adj = vec![0usize; 2 * (n - 1)];
    let mut weight = vec![0usize; 2 * (n - 1)];
    for &(u, v, w) in &edges {
        adj[fill[u]] = v;
        weight[fill[u]] = w;
        fill[u] += 1;
        adj[fill[v]] = u;
        weight[fill[v]] = w;
        fill[v] += 1;
    }

    // Euler tour from vertex 0: a vertex is written on entry and after each child
    let mut parent = vec![usize::MAX; n];
    let mut depth = vec![0usize; n];
    let mut dist = vec![0usize; n];
    let mut first = vec![0usize; n];
    let mut tour = vec![0usize];
    let mut pointer = start[..n].to_vec();
    let mut stack = vec![0usize];
    while let Some(&v) = stack.last() {
        let p = pointer[v];
        if p < start[v + 1] {
            pointer[v] += 1;
            let u = adj[p];
            if u == parent[v] {
                continue;
            }
            parent[u] = v;
            depth[u] = depth[v] + 1;
            dist[u] = dist[v] + weight[p];
            first[u] = tour.len();
            tour.push(u);
            stack.push(u);
        } else {
            stack.pop();
            if let Some(&top) = stack.last() {
                tour.push(top);
            }
        }
    }

    // sparse table: the shallowest vertex of each run of 2^k tour entries
    let shallower = |a: usize, b: usize| if depth[a] <= depth[b] { a } else { b };
    let len = tour.len();
    let mut table = vec![tour];
    let mut span = 1;
    while 2 * span <= len {
        let prev = table.last().unwrap();
        let level: Vec<usize> = (0..len - 2 * span + 1)
            .map(|i| shallower(prev[i], prev[i + span]))
            .collect();
        table.push(level);
        span *= 2;
    }

    let m = it.next().unwrap();
    let mut out = String::new();
    for _ in 0..m {
        let (a, b) = (it.next().unwrap(), it.next().unwrap());
        let (lo, hi) = (first[a].min(first[b]), first[a].max(first[b]));
        let k = (usize::BITS - 1 - (hi - lo + 1).leading_zeros()) as usize;
        let lca = shallower(table[k][lo], table[k][hi + 1 - (1 << k)]);
        out.push_str(&(dist[a] + dist[b] - 2 * dist[lca]).to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
