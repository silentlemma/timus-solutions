use std::io::{self, Read};

/// Smallest total cost of a perfect matching of rows to columns, with
/// potentials u, v kept so that reduced costs stay non-negative.
fn hungarian(cost: &[Vec<i64>], n: usize) -> i64 {
    let mut u = vec![0i64; n + 1];
    let mut v = vec![0i64; n + 1];
    let mut owner = vec![0usize; n + 1];
    let mut way = vec![0usize; n + 1];
    for row in 1..=n {
        owner[0] = row;
        let mut col = 0;
        let mut low = vec![i64::MAX; n + 1];
        let mut used = vec![false; n + 1];
        loop {
            used[col] = true;
            let r = owner[col];
            let (mut delta, mut next) = (i64::MAX, 0);
            for j in 1..=n {
                if !used[j] {
                    let cur = cost[r - 1][j - 1] - u[r] - v[j];
                    if cur < low[j] {
                        low[j] = cur;
                        way[j] = col;
                    }
                    if low[j] < delta {
                        delta = low[j];
                        next = j;
                    }
                }
            }
            for j in 0..=n {
                if used[j] {
                    u[owner[j]] += delta;
                    v[j] -= delta;
                } else {
                    low[j] -= delta;
                }
            }
            col = next;
            if owner[col] == 0 {
                break;
            }
        }
        while col != 0 {
            let prev = way[col];
            owner[col] = owner[prev];
            col = prev;
        }
    }
    -v[0]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let rows: Vec<Vec<i64>> = (0..n).map(|_| it.by_ref().take(n).collect()).collect();
    let total: i64 = rows.iter().flatten().sum();
    // type j stays in container i; everything else in its column moves
    let cost: Vec<Vec<i64>> = rows
        .iter()
        .map(|row| row.iter().map(|&x| -x).collect())
        .collect();
    println!("{}", total + hungarian(&cost, n));
}
