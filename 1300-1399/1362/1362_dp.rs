use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut adj = vec![Vec::new(); n + 1];
    for boss in 1..=n {
        loop {
            let v = it.next().unwrap();
            if v == 0 {
                break;
            }
            adj[boss].push(v);
            adj[v].push(boss);
        }
    }
    let root = it.next().unwrap();
    // calls go both up and down, so the news spreads over the tree rooted
    // at Tanya; order parents before children
    let mut parent = vec![usize::MAX; n + 1];
    parent[root] = 0;
    let mut order = vec![root];
    let mut i = 0;
    while i < order.len() {
        let v = order[i];
        for k in 0..adj[v].len() {
            let u = adj[v][k];
            if u != parent[v] {
                parent[u] = v;
                order.push(u);
            }
        }
        i += 1;
    }
    // the time of v is what it needs to tell its whole subtree; the slowest
    // subtrees are called first, the i-th call starting at minute i
    let mut time = vec![0usize; n + 1];
    let mut kids: Vec<Vec<usize>> = vec![Vec::new(); n + 1];
    for &v in order.iter().rev() {
        let mut times = std::mem::take(&mut kids[v]);
        times.sort_unstable_by(|a, b| b.cmp(a));
        for (j, &t) in times.iter().enumerate() {
            time[v] = time[v].max(t + j + 1);
        }
        if parent[v] != 0 {
            kids[parent[v]].push(time[v]);
        }
    }
    println!("{}", time[root]);
}
