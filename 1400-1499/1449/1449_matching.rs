use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    // the Hungarian method minimises the cost -A; rows and columns from 1, 0 is a helper
    let mut cost = vec![vec![0i64; n + 1]; n + 1];
    for row in cost.iter_mut().skip(1) {
        for cell in row.iter_mut().skip(1) {
            *cell = -it.next().unwrap();
        }
    }
    let (mut u, mut v) = (vec![0i64; n + 1], vec![0i64; n + 1]);
    let mut matched = vec![0usize; n + 1]; // matched[j]: the row matched to column j
    let mut way = vec![0usize; n + 1];
    for i in 1..=n {
        matched[0] = i;
        let mut j0 = 0;
        let mut low = vec![i64::MAX; n + 1];
        let mut used = vec![false; n + 1];
        while matched[j0] != 0 {
            used[j0] = true;
            let i0 = matched[j0];
            let (mut delta, mut j1) = (i64::MAX, 0);
            for j in 1..=n {
                if !used[j] {
                    let cur = cost[i0][j] - u[i0] - v[j];
                    if cur < low[j] {
                        low[j] = cur;
                        way[j] = j0;
                    }
                    if low[j] < delta {
                        delta = low[j];
                        j1 = j;
                    }
                }
            }
            for j in 0..=n {
                if used[j] {
                    u[matched[j]] += delta;
                    v[j] -= delta;
                } else {
                    low[j] -= delta;
                }
            }
            j0 = j1;
        }
        while j0 != 0 {
            let j1 = way[j0];
            matched[j0] = matched[j1];
            j0 = j1;
        }
    }
    // u + v <= -A, so the bribes -u, -v cover every credit and add up to the
    // heaviest matching; shifting them until a row bribe is 0 keeps all >= 0
    let shift = u[1..].iter().map(|&x| -x).min().unwrap();
    let rows: Vec<String> = u[1..].iter().map(|&x| (-x - shift).to_string()).collect();
    let cols: Vec<String> = v[1..].iter().map(|&x| (-x + shift).to_string()).collect();
    println!("{}", rows.join(" "));
    println!("{}", cols.join(" "));
}
