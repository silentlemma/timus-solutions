use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let m = it.next().unwrap() as usize;
    let q = it.next().unwrap() as usize;
    let mut edges = Vec::with_capacity(m);
    let mut size = n;
    for _ in 0..m {
        let u = it.next().unwrap() as usize;
        let v = it.next().unwrap() as usize;
        let s = it.next().unwrap();
        let w = it.next().unwrap();
        size = size.max(u).max(v);
        edges.push((u, v, s, w));
    }
    let mut adj: Vec<Vec<(usize, i64, i64)>> = vec![Vec::new(); size + 1];
    let mut indegree = vec![0usize; size + 1];
    for &(u, v, s, w) in &edges {
        adj[u].push((v, s, w));
        indegree[v] += 1;
    }

    // The best route maximizes its smallest ratio s / w, stored as a
    // numerator and denominator; 1 / 0 stands for the empty route at 1.
    let mut num = vec![0i64; size + 1];
    let mut den = vec![0i64; size + 1];
    let mut reached = vec![false; size + 1];
    reached[1] = true;
    num[1] = 1;
    let mut order: Vec<usize> = (1..=size).filter(|&v| indegree[v] == 0).collect();
    let mut head = 0;
    while head < order.len() {
        let u = order[head];
        head += 1;
        for &(v, s, w) in &adj[u] {
            indegree[v] -= 1;
            if indegree[v] == 0 {
                order.push(v);
            }
            if !reached[u] {
                continue;
            }
            let (mut a, mut b) = (num[u], den[u]);
            if s * b < a * w {
                a = s;
                b = w;
            }
            if !reached[v] || num[v] * b < a * den[v] {
                reached[v] = true;
                num[v] = a;
                den[v] = b;
            }
        }
    }

    let mut out = String::new();
    for _ in 0..q {
        let price_s = it.next().unwrap();
        let price_w = it.next().unwrap();
        let good = reached[n] && price_s * num[n] > price_w * den[n];
        out.push_str(if good { "YES\n" } else { "NO\n" });
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
