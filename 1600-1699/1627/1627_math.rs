use std::io::{self, Read};

const MOD: i64 = 1_000_000_000;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let m: usize = words.next().unwrap().parse().unwrap();
    let grid: Vec<&[u8]> = words.take(n).map(|w| w.as_bytes()).collect();
    let mut id = vec![vec![usize::MAX; m]; n];
    let mut v = 0;
    for i in 0..n {
        for j in 0..m {
            if grid[i][j] == b'.' {
                id[i][j] = v;
                v += 1;
            }
        }
    }
    // the Laplacian of the bedroom graph; by the matrix-tree theorem any
    // cofactor counts its spanning trees (0 when it is disconnected)
    let mut lap = vec![vec![0i64; v]; v];
    for i in 0..n {
        for j in 0..m {
            let u = id[i][j];
            if u == usize::MAX {
                continue;
            }
            let below = if i + 1 < n { id[i + 1][j] } else { usize::MAX };
            let right = if j + 1 < m { id[i][j + 1] } else { usize::MAX };
            for w in [below, right] {
                if w != usize::MAX {
                    lap[u][u] += 1;
                    lap[w][w] += 1;
                    lap[u][w] -= 1;
                    lap[w][u] -= 1;
                }
            }
        }
    }
    let size = v - 1;
    let mut a: Vec<Vec<i64>> = (0..size)
        .map(|i| (0..size).map(|j| lap[i][j].rem_euclid(MOD)).collect())
        .collect();
    // Elimination by Euclid's algorithm on rows: it only subtracts multiples
    // of rows and swaps them, so it works modulo 10^9, which is not prime.
    let mut det = 1i64;
    for k in 0..size {
        for i in k + 1..size {
            while a[i][k] != 0 {
                let q = a[k][k] / a[i][k];
                for j in k..size {
                    a[k][j] = (a[k][j] - q * a[i][j]).rem_euclid(MOD);
                }
                a.swap(k, i);
                det = (MOD - det) % MOD;
            }
        }
        det = det * a[k][k] % MOD;
    }
    println!("{}", det);
}
