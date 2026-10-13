use std::io::{self, Read, Write};

const STEP: i32 = 2; // columns two apart keep every pair of points farther than 1
const LIMIT: i32 = 999; // the leftmost column, so that 1000 columns fit in [-999, 999]

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut adj = vec![Vec::new(); n + 1];
    for _ in 0..n - 1 {
        let (a, b) = (it.next().unwrap(), it.next().unwrap());
        adj[a].push(b);
        adj[b].push(a);
    }
    // column = preorder index, row = depth: the subtrees of the vertices on
    // one row take disjoint ranges of columns, so no two wires cross
    let (mut x, mut y) = (vec![0i32; n + 1], vec![0i32; n + 1]);
    let mut seen = vec![false; n + 1];
    seen[1] = true;
    let mut stack = vec![1usize];
    let mut order = 0;
    while let Some(v) = stack.pop() {
        x[v] = order * STEP - LIMIT;
        order += 1;
        for &u in adj[v].iter().rev() {
            if !seen[u] {
                seen[u] = true;
                y[u] = y[v] + 1;
                stack.push(u);
            }
        }
    }
    let mut out = String::new();
    for v in 1..=n {
        out.push_str(&format!("{} {}\n", x[v], y[v]));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
