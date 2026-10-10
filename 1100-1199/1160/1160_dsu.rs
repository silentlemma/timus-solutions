use std::fmt::Write as _;
use std::io::{self, Read};

fn find(parent: &mut [usize], mut v: usize) -> usize {
    while parent[v] != v {
        parent[v] = parent[parent[v]];
        v = parent[v];
    }
    v
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (tok.next().unwrap(), tok.next().unwrap());
    let mut edges: Vec<(usize, usize, usize)> = (0..m)
        .map(|_| {
            (
                tok.next().unwrap(),
                tok.next().unwrap(),
                tok.next().unwrap(),
            )
        })
        .collect();
    edges.sort_by_key(|e| e.2);
    let mut parent: Vec<usize> = (0..=n).collect();
    // Kruskal's tree: its longest cable is the smallest possible longest cable
    // of any plan that connects every hub
    let mut chosen = Vec::new();
    for &(a, b, length) in &edges {
        let (ra, rb) = (find(&mut parent, a), find(&mut parent, b));
        if ra != rb {
            parent[ra] = rb;
            chosen.push((a, b, length));
        }
    }
    let mut out = format!("{}\n{}\n", chosen.last().unwrap().2, chosen.len());
    for (a, b, _) in &chosen {
        writeln!(out, "{} {}", a, b).unwrap();
    }
    print!("{}", out);
}
