use std::fmt::Write as _;
use std::io::{self, Read};

fn multiply(a: &[Vec<u64>], b: &[Vec<u64>], modulus: u64) -> Vec<Vec<u64>> {
    let n = a.len();
    let mut c = vec![vec![0u64; n]; n];
    for i in 0..n {
        for k in 0..n {
            if a[i][k] == 0 {
                continue;
            }
            for j in 0..n {
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % modulus;
            }
        }
    }
    c
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<u64> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let mut it = v.into_iter();
    let mut next = || it.next().unwrap();
    let (n, m, mut d, modulus, q) = (next(), next(), next(), next(), next() as usize);
    let n = n as usize;
    let points: Vec<Vec<u64>> = (0..q).map(|_| (0..n).map(|_| next()).collect()).collect();
    // the number of routes depends only on how many coordinates differ
    // from the target: a move fixes one of them, changes one of them to
    // another wrong value, or spoils one that was right
    let size = n + 1;
    let mut step = vec![vec![0u64; size]; size];
    let mut power = vec![vec![0u64; size]; size];
    for h in 0..size {
        let hh = h as u64;
        if h > 0 {
            step[h][h - 1] = hh % modulus;
            step[h][h] = hh * (m - 2) % modulus;
        }
        if h < n {
            step[h][h + 1] = (n as u64 - hh) * (m - 1) % modulus;
        }
        power[h][h] = 1 % modulus;
    }
    while d > 0 {
        if d & 1 == 1 {
            power = multiply(&power, &step, modulus);
        }
        step = multiply(&step, &step, modulus);
        d >>= 1;
    }
    let mut out = String::new();
    for a in &points {
        let row: Vec<String> = points
            .iter()
            .map(|b| {
                let differ = a.iter().zip(b).filter(|(x, y)| x != y).count();
                power[differ][0].to_string()
            })
            .collect();
        writeln!(out, "{}", row.join(" ")).unwrap();
    }
    print!("{}", out);
}
