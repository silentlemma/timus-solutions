use std::io::{self, Read, Write};

const INF: i64 = 1 << 30;
const END_OF_INPUT: i64 = -1;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let mut out = String::new();
    loop {
        let n = it.next().unwrap();
        if n == END_OF_INPUT {
            break;
        }
        let n = n as usize;
        let m = it.next().unwrap() as usize;
        // edge: the lightest direct road between two vertices
        let mut edge = vec![vec![INF; n]; n];
        for (i, row) in edge.iter_mut().enumerate() {
            row[i] = 0;
        }
        for _ in 0..m {
            let a = it.next().unwrap() as usize - 1;
            let b = it.next().unwrap() as usize - 1;
            let l = it.next().unwrap();
            if l < edge[a][b] {
                edge[a][b] = l;
                edge[b][a] = l;
            }
        }
        let mut dist = edge.clone();
        let mut next: Vec<Vec<usize>> = (0..n).map(|_| (0..n).collect()).collect();

        // Floyd-Warshall; before vertex k becomes an intermediate, dist[i][j]
        // uses only vertices below k, so i..j plus j-k-i is a simple cycle.
        let mut best = INF;
        let mut cycle: Vec<usize> = Vec::new();
        for k in 0..n {
            for i in 0..k {
                if edge[i][k] == INF {
                    continue;
                }
                for j in i + 1..k {
                    if edge[k][j] == INF || dist[i][j] == INF {
                        continue;
                    }
                    let c = dist[i][j] + edge[i][k] + edge[k][j];
                    if c < best {
                        best = c;
                        cycle.clear();
                        let mut v = i;
                        while v != j {
                            cycle.push(v);
                            v = next[v][j];
                        }
                        cycle.push(j);
                        cycle.push(k);
                    }
                }
            }
            for i in 0..n {
                let dik = dist[i][k];
                if dik == INF {
                    continue;
                }
                let nik = next[i][k];
                for j in 0..n {
                    let d = dik + dist[k][j];
                    if d < dist[i][j] {
                        dist[i][j] = d;
                        next[i][j] = nik;
                    }
                }
            }
        }
        if best == INF {
            out.push_str("No solution.\n");
            continue;
        }
        let line: Vec<String> = cycle.iter().map(|v| (v + 1).to_string()).collect();
        out.push_str(&line.join(" "));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
