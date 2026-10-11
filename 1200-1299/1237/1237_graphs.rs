use std::fmt::Write as _;
use std::io::{self, Read};

const INF: i64 = 1 << 60;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let (n, m) = (it.next().unwrap() as usize, it.next().unwrap() as usize);
    let mut read3 = || (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    let buildings: Vec<(i64, i64, i64)> = (0..n).map(|_| read3()).collect();
    let shelters: Vec<(i64, i64, i64)> = (0..m).map(|_| read3()).collect();
    let mut plan: Vec<Vec<i64>> = (0..n)
        .map(|_| (0..m).map(|_| it.next().unwrap()).collect())
        .collect();
    let dist: Vec<Vec<i64>> = buildings
        .iter()
        .map(|&(x, y, _)| {
            shelters
                .iter()
                .map(|&(p, q, _)| (x - p).abs() + (y - q).abs() + 1)
                .collect()
        })
        .collect();
    // nodes 0..m-1 are shelters and m is the spare room; j -> k moves one
    // worker of some building from shelter j to k, j -> m uses a free place
    // at j, and m -> k lets shelter k end up one worker short
    let v = m + 1;
    let mut w = vec![vec![INF; v]; v];
    let mut via = vec![vec![0usize; v]; v];
    for i in 0..n {
        for j in 0..m {
            if plan[i][j] == 0 {
                continue;
            }
            for k in 0..m {
                let c = dist[i][k] - dist[i][j];
                if k != j && c < w[j][k] {
                    w[j][k] = c;
                    via[j][k] = i;
                }
            }
        }
    }
    for j in 0..m {
        let load: i64 = (0..n).map(|i| plan[i][j]).sum();
        if load < shelters[j].2 {
            w[j][m] = 0;
        }
        w[m][j] = 0;
    }
    // Bellman-Ford from all nodes at once; a change in round v means a
    // negative cycle, which the predecessors lead into
    let mut d = vec![0i64; v];
    let mut pred = vec![0usize; v];
    let mut last = None;
    for _ in 0..v {
        last = None;
        for j in 0..v {
            for k in 0..v {
                if w[j][k] < INF && d[j] + w[j][k] < d[k] {
                    d[k] = d[j] + w[j][k];
                    pred[k] = j;
                    last = Some(k);
                }
            }
        }
        if last.is_none() {
            break;
        }
    }
    let mut start = match last {
        None => {
            println!("OPTIMAL");
            return;
        }
        Some(x) => x,
    };
    for _ in 0..v {
        start = pred[start];
    }
    // shift one worker along each shelter-to-shelter edge of the cycle
    let mut k = start;
    loop {
        let j = pred[k];
        if j < m && k < m {
            plan[via[j][k]][j] -= 1;
            plan[via[j][k]][k] += 1;
        }
        k = j;
        if k == start {
            break;
        }
    }
    let mut out = String::from("SUBOPTIMAL\n");
    for row in &plan {
        let line: Vec<String> = row.iter().map(|e| e.to_string()).collect();
        writeln!(out, "{}", line.join(" ")).unwrap();
    }
    print!("{}", out);
}
