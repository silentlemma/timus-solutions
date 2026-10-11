use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    // g[a][b]: total conductance between two nodes
    let mut g = vec![vec![0.0f64; n]; n];
    for _ in 0..m {
        let (a, b, r) = (
            it.next().unwrap() - 1,
            it.next().unwrap() - 1,
            it.next().unwrap(),
        );
        g[a][b] += 1.0 / r as f64;
        g[b][a] += 1.0 / r as f64;
    }
    // nodes cut off from node 1 carry no current and would make the
    // system singular
    let mut seen = vec![false; n];
    seen[0] = true;
    let mut stack = vec![0];
    while let Some(u) = stack.pop() {
        for v in 0..n {
            if g[u][v] > 0.0 && !seen[v] {
                seen[v] = true;
                stack.push(v);
            }
        }
    }
    let inner: Vec<usize> = (1..n - 1).filter(|&v| seen[v]).collect();
    // Kirchhoff at each inner node with potential 1 at node 1, 0 at node N
    let k = inner.len();
    let mut a = vec![vec![0.0f64; k + 1]; k];
    for (i, &u) in inner.iter().enumerate() {
        a[i][i] = g[u].iter().sum();
        for (j, &v) in inner.iter().enumerate() {
            a[i][j] -= g[u][v];
        }
        a[i][k] = g[u][0];
    }
    for c in 0..k {
        let p = (c..k)
            .max_by(|&x, &y| a[x][c].abs().partial_cmp(&a[y][c].abs()).unwrap())
            .unwrap();
        a.swap(c, p);
        for r in 0..k {
            if r != c && a[r][c] != 0.0 {
                let f = a[r][c] / a[c][c];
                for j in c..=k {
                    a[r][j] -= f * a[c][j];
                }
            }
        }
    }
    let mut volt = vec![0.0f64; n];
    volt[0] = 1.0;
    for (i, &u) in inner.iter().enumerate() {
        volt[u] = a[i][k] / a[i][i];
    }
    let current: f64 = (1..n).map(|v| g[0][v] * (1.0 - volt[v])).sum();
    println!("{:.2}", 1.0 / current);
}
