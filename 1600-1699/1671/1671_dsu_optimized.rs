use std::io::{self, BufWriter, Read, Write};

fn find(parent: &mut [i32], mut v: usize) -> usize {
    let mut root = v;
    while parent[root] >= 0 {
        root = parent[root] as usize;
    }
    while v != root {
        let next = parent[v] as usize;
        parent[v] = root as i32;
        v = next;
    }
    root
}

fn join(parent: &mut [i32], edge: (u32, u32)) -> usize {
    let (mut a, mut b) = (find(parent, edge.0 as usize), find(parent, edge.1 as usize));
    if a == b {
        return 0;
    }
    // roots store negative sizes; attach the smaller tree to the larger.
    if parent[a] > parent[b] {
        std::mem::swap(&mut a, &mut b);
    }
    parent[a] += parent[b];
    parent[b] = a as i32;
    1
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut tokens = input
        .split(|c| c.is_ascii_whitespace())
        .filter(|s| !s.is_empty());
    // decimal byte parsing avoids allocating a second vector of input integers.
    let mut next = || {
        tokens
            .next()
            .unwrap()
            .iter()
            .fold(0usize, |value, &c| value * 10 + (c - b'0') as usize)
    };
    let (n, m) = (next(), next());
    // n, m and q are at most 100000; endpoints and answers fit u32, sizes fit i32.
    let edges: Vec<(u32, u32)> = (0..m).map(|_| (next() as u32, next() as u32)).collect();
    let q = next();
    let mut cuts: Vec<u32> = (0..q).map(|_| (next() - 1) as u32).collect();
    let mut cut = vec![false; m];
    for &edge in &cuts {
        cut[edge as usize] = true;
    }
    let mut parent = vec![-1; n + 1];
    // run backwards: start from the web after all cuts and put the threads
    // back one by one, last cut first
    let mut pieces = n;
    for (i, &edge) in edges.iter().enumerate() {
        if !cut[i] {
            pieces -= join(&mut parent, edge);
        }
    }
    for k in (0..q).rev() {
        let edge = cuts[k] as usize;
        // this cut has been processed, so its slot can hold the answer.
        cuts[k] = pieces as u32;
        pieces -= join(&mut parent, edges[edge]);
    }
    let stdout = io::stdout();
    let mut output = BufWriter::new(stdout.lock());
    for (k, answer) in cuts.iter().enumerate() {
        write!(output, "{}{}", answer, if k + 1 == q { "\n" } else { " " }).unwrap();
    }
}
