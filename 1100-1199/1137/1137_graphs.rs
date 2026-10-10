use std::fmt::Write as _;
use std::io::{self, Read};

// stops are numbered up to this
const STOPS: usize = 1000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = tok.next().unwrap();
    let mut adj: Vec<Vec<usize>> = vec![Vec::new(); STOPS + 1];
    let mut edges = 0;
    let mut start = None;
    for _ in 0..n {
        let m = tok.next().unwrap();
        let route: Vec<usize> = (0..=m).map(|_| tok.next().unwrap()).collect();
        start.get_or_insert(route[0]);
        for w in route.windows(2) {
            adj[w[0]].push(w[1]);
        }
        edges += m;
    }
    // every old route is a cycle, so each stop is left as often as it is
    // entered; Hierholzer's walk then uses every segment once
    let mut ptr = vec![0; STOPS + 1];
    let mut stack = vec![start.unwrap()];
    let mut circuit = Vec::new();
    while let Some(&v) = stack.last() {
        if ptr[v] < adj[v].len() {
            stack.push(adj[v][ptr[v]]);
            ptr[v] += 1;
        } else {
            circuit.push(v);
            stack.pop();
        }
    }
    if circuit.len() != edges + 1 {
        println!("0");
        return;
    }
    let mut out = edges.to_string();
    for v in circuit.iter().rev() {
        write!(out, " {}", v).unwrap();
    }
    println!("{}", out);
}
