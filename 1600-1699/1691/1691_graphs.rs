use std::io::{self, Read};

fn reach(start: usize, adj: &[Vec<usize>]) -> Vec<bool> {
    let mut seen = vec![false; adj.len()];
    seen[start] = true;
    let mut stack = vec![start];
    while let Some(v) = stack.pop() {
        for &u in &adj[v] {
            if !seen[u] {
                seen[u] = true;
                stack.push(u);
            }
        }
    }
    seen
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let mut next = || it.next().unwrap();
    let (n, m) = (next(), next());
    let (s, t) = (next() - 1, next() - 1);
    let edges: Vec<(usize, usize)> = (0..m).map(|_| (next() - 1, next() - 1)).collect();
    let mut adj = vec![Vec::new(); n];
    let mut radj = vec![Vec::new(); n];
    for &(a, b) in &edges {
        adj[a].push(b);
        radj[b].push(a);
    }
    // only vertices on some path from s to t matter; they form whole
    // strongly connected components
    let from_s = reach(s, &adj);
    if !from_s[t] {
        println!("0");
        return;
    }
    let to_t = reach(t, &radj);
    let alive: Vec<bool> = (0..n).map(|v| from_s[v] && to_t[v]).collect();
    // Kosaraju: finishing order on the graph, then the reversed graph in
    // reverse finishing order numbers the components in topological order
    let mut order = Vec::new();
    let mut done = vec![false; n];
    for root in 0..n {
        if !alive[root] || done[root] {
            continue;
        }
        done[root] = true;
        let mut stack = vec![(root, 0usize)];
        while let Some(&(v, i)) = stack.last() {
            if i < adj[v].len() {
                stack.last_mut().unwrap().1 += 1;
                let u = adj[v][i];
                if alive[u] && !done[u] {
                    done[u] = true;
                    stack.push((u, 0));
                }
            } else {
                order.push(v);
                stack.pop();
            }
        }
    }
    let mut comp = vec![usize::MAX; n];
    let mut count = 0;
    for &root in order.iter().rev() {
        if comp[root] != usize::MAX {
            continue;
        }
        comp[root] = count;
        let mut stack = vec![root];
        while let Some(v) = stack.pop() {
            for &u in &radj[v] {
                if alive[u] && comp[u] == usize::MAX {
                    comp[u] = count;
                    stack.push(u);
                }
            }
        }
        count += 1;
    }
    let mut size = vec![0; count];
    let mut inside = vec![0; count];
    let mut out = vec![Vec::new(); count];
    for v in 0..n {
        if alive[v] {
            size[comp[v]] += 1;
        }
    }
    for &(a, b) in &edges {
        if alive[a] && alive[b] {
            if comp[a] == comp[b] {
                inside[comp[a]] += 1;
            } else {
                out[comp[a]].push(comp[b]);
            }
        }
    }
    // a component with more arcs than vertices holds two cycles, and paths grow
    // exponentially; otherwise each cyclic component is one simple cycle, and
    // paths through c of them number about N^(c - 1)
    if (0..count).any(|c| inside[c] > size[c]) {
        println!("-1");
        return;
    }
    // best[c]: the most cycles on a path from s into component c; arcs go
    // from lower to higher numbers, so one pass in order settles it
    let mut best = vec![0i64; count];
    for c in 0..count {
        if inside[c] == size[c] {
            best[c] += 1;
        }
        for &d in &out[c] {
            best[d] = best[d].max(best[c]);
        }
    }
    println!("{}", (best[comp[t]] - 1).max(0));
}
