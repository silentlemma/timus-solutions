use std::io::{self, Read};

struct Net {
    n: usize,
    cost: Vec<i64>, // n by n, 0 marks a missing link, real values are positive
    dist: Vec<i64>,
}

impl Net {
    /// Prim on the weights c q - d p, exact integers; returns the tree's
    /// total weight, cost and length.
    fn tree(&self, p: i64, q: i64) -> (i64, i64, i64) {
        let n = self.n;
        let mut best = vec![i64::MAX; n];
        let (mut bc, mut bd) = (vec![0i64; n], vec![0i64; n]);
        let mut used = vec![false; n];
        best[0] = 0;
        let (mut total, mut tc, mut td) = (0i64, 0i64, 0i64);
        for _ in 0..n {
            let u = (0..n)
                .filter(|&v| !used[v])
                .min_by_key(|&v| best[v])
                .unwrap();
            used[u] = true;
            total += best[u];
            tc += bc[u];
            td += bd[u];
            let cu = &self.cost[u * n..(u + 1) * n];
            let du = &self.dist[u * n..(u + 1) * n];
            for v in 0..n {
                if cu[v] != 0 && !used[v] {
                    let w = cu[v] * q - du[v] * p;
                    if w < best[v] {
                        best[v] = w;
                        bc[v] = cu[v];
                        bd[v] = du[v];
                    }
                }
            }
        }
        (total, tc, td)
    }
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let m = it.next().unwrap() as usize;
    let mut net = Net {
        n,
        cost: vec![0; n * n],
        dist: vec![0; n * n],
    };
    for _ in 0..m {
        let a = it.next().unwrap() as usize - 1;
        let b = it.next().unwrap() as usize - 1;
        let (d, c) = (it.next().unwrap(), it.next().unwrap());
        net.cost[a * n + b] = c;
        net.cost[b * n + a] = c;
        net.dist[a * n + b] = d;
        net.dist[b * n + a] = d;
    }
    // Dinkelbach: the ratio p / q of the last tree drops until no tree beats it
    let (_, mut p, mut q) = net.tree(0, 1);
    loop {
        let (total, tc, td) = net.tree(p, q);
        if total >= 0 {
            break;
        }
        let g = gcd(tc, td);
        p = tc / g;
        q = td / g;
    }
    println!("{:.10}", p as f64 / q as f64);
}
