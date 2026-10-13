use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    // rows A x = 1: every player move then earns the same; x scaled to sum 1 is the answer
    let mut rows: Vec<Vec<f64>> = (0..n)
        .map(|_| {
            let mut row: Vec<f64> = (0..n)
                .map(|_| it.next().unwrap().parse().unwrap())
                .collect();
            row.push(1.0);
            row
        })
        .collect();
    for col in 0..n {
        let pivot = (col..n)
            .max_by(|&a, &b| rows[a][col].abs().partial_cmp(&rows[b][col].abs()).unwrap())
            .unwrap();
        rows.swap(col, pivot);
        for r in col + 1..n {
            let f = rows[r][col] / rows[col][col];
            for j in col..=n {
                let v = rows[col][j];
                rows[r][j] -= f * v;
            }
        }
    }
    let mut x = vec![0.0; n];
    for i in (0..n).rev() {
        let s: f64 = rows[i][n] - (i + 1..n).map(|j| rows[i][j] * x[j]).sum::<f64>();
        x[i] = s / rows[i][i];
    }
    let total: f64 = x.iter().sum();
    let mut out = String::new();
    for v in &x {
        writeln!(out, "{:.5}", v / total).unwrap();
    }
    print!("{}", out);
}
