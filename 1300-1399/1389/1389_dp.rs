use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let (mut a, mut b) = (vec![0usize; m], vec![0usize; m]);
    let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n + 1];
    for i in 0..m {
        a[i] = it.next().unwrap();
        b[i] = it.next().unwrap();
        adj[a[i]].push(i);
        adj[b[i]].push(i);
    }
    // breadth-first order from city 1 with the road to each parent
    let mut parent = vec![0usize; n + 1];
    let mut up: Vec<Option<usize>> = vec![None; n + 1];
    let mut order = vec![1usize];
    let mut k = 0;
    while k < order.len() {
        let v = order[k];
        for &e in &adj[v] {
            let u = a[e] + b[e] - v;
            if u != parent[v] {
                parent[u] = v;
                up[u] = Some(e);
                order.push(u);
            }
        }
        k += 1;
    }
    // leaves first: close the road to the parent while both ends are free
    let mut used = vec![false; n + 1];
    let mut chosen = vec![false; m];
    for &v in order.iter().rev() {
        if let Some(e) = up[v] {
            if !used[v] && !used[parent[v]] {
                used[v] = true;
                used[parent[v]] = true;
                chosen[e] = true;
            }
        }
    }
    let mut out = String::new();
    writeln!(out, "{}", chosen.iter().filter(|&&c| c).count()).unwrap();
    for i in (0..m).filter(|&i| chosen[i]) {
        writeln!(out, "{} {}", a[i], b[i]).unwrap();
    }
    print!("{}", out);
}
