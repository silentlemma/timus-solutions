use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let n = match it.next() {
        Some(v) => v,
        None => return,
    };
    let m = it.next().unwrap();
    let root = it.next().unwrap();
    let mut adj = vec![Vec::new(); n + 1];
    for _ in 0..m {
        let k = it.next().unwrap();
        let mut prev = it.next().unwrap();
        for _ in 1..k {
            let v = it.next().unwrap();
            adj[prev].push(v);
            adj[v].push(prev);
            prev = v;
        }
    }
    // depth-first search without recursion, so every other edge joins a
    // vertex to one of its ancestors
    let mut parent = vec![0; n + 1];
    let mut depth = vec![usize::MAX; n + 1];
    let mut pos = vec![0; n + 1];
    let mut order = vec![root];
    depth[root] = 0;
    let mut stack = vec![root];
    while let Some(&v) = stack.last() {
        if pos[v] == adj[v].len() {
            stack.pop();
            continue;
        }
        let u = adj[v][pos[v]];
        pos[v] += 1;
        if depth[u] == usize::MAX {
            depth[u] = depth[v] + 1;
            parent[u] = v;
            order.push(u);
            stack.push(u);
        }
    }
    // every non-tree edge closes a cycle with the tree path between its ends
    let mut on_cycle = vec![false; n + 1]; // the edge from v to its parent lies on a cycle
    let mut cycles: Vec<Vec<Vec<usize>>> = vec![Vec::new(); n + 1]; // listed at the top vertex
    for v in 1..=n {
        for &u in &adj[v] {
            if depth[u] < depth[v] && u != parent[v] {
                let mut members = Vec::new();
                let mut x = v;
                while x != u {
                    on_cycle[x] = true;
                    members.push(x);
                    x = parent[x];
                }
                cycles[u].push(members);
            }
        }
    }
    // a tree edge to a child of value g is worth g + 1; a cycle fuses into
    // loops on its top vertex: one loop (worth 1) per edge, so its length
    // parity, together with everything hanging from its other vertices
    let mut value = vec![0usize; n + 1];
    for &v in order.iter().rev() {
        let mut g = 0;
        for &u in &adj[v] {
            if parent[u] == v && !on_cycle[u] {
                g ^= value[u] + 1;
            }
        }
        for members in &cycles[v] {
            g ^= (members.len() + 1) % 2; // a cycle has as many edges as vertices
            for &x in members {
                g ^= value[x];
            }
        }
        value[v] = g;
    }
    println!("{}", if value[root] != 0 { "First" } else { "Second" });
}
