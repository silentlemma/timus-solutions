use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let mut out: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n + 1];
    let mut indeg = vec![0usize; n + 1];
    for _ in 0..m {
        let (a, b, c) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
        out[a].push((b, c as i64));
        indeg[b] += 1;
    }
    let (s, f) = (it.next().unwrap(), it.next().unwrap());
    // the network has no cycles: take the stations in topological order and
    // keep the best profit of a route from S to each of them, None if unreachable
    let mut best: Vec<Option<i64>> = vec![None; n + 1];
    best[s] = Some(0);
    let mut order: Vec<usize> = (1..=n).filter(|&v| indeg[v] == 0).collect();
    let mut k = 0;
    while k < order.len() {
        let v = order[k];
        k += 1;
        for &(w, c) in &out[v] {
            if let Some(b) = best[v] {
                if best[w].map_or(true, |x| b + c > x) {
                    best[w] = Some(b + c);
                }
            }
            indeg[w] -= 1;
            if indeg[w] == 0 {
                order.push(w);
            }
        }
    }
    match best[f] {
        Some(x) => println!("{}", x),
        None => println!("No solution"),
    }
}
