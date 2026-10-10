use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut next = || it.next().unwrap();
    let walk: f64 = next().parse().unwrap();
    let metro: f64 = next().parse().unwrap();
    let n: usize = next().parse().unwrap();
    let (total, start, goal) = (n + 2, n, n + 1);
    let mut pts = vec![(0.0f64, 0.0f64); total];
    for p in pts.iter_mut().take(n) {
        *p = (next().parse().unwrap(), next().parse().unwrap());
    }
    let mut linked = vec![vec![false; total]; total];
    loop {
        let a: usize = next().parse().unwrap();
        let b: usize = next().parse().unwrap();
        if a == 0 && b == 0 {
            break;
        }
        linked[a - 1][b - 1] = true;
        linked[b - 1][a - 1] = true;
    }
    pts[start] = (next().parse().unwrap(), next().parse().unwrap());
    pts[goal] = (next().parse().unwrap(), next().parse().unwrap());
    // nodes: the stations, then A and B; the subway is never slower than
    // walking, so a linked pair always goes by train
    let mut dist = vec![f64::INFINITY; total];
    let mut prev = vec![usize::MAX; total];
    let mut done = vec![false; total];
    dist[start] = 0.0;
    for _ in 0..total {
        let u = (0..total)
            .filter(|&v| !done[v])
            .min_by(|&p, &q| dist[p].partial_cmp(&dist[q]).unwrap())
            .unwrap();
        done[u] = true;
        for v in 0..total {
            if !done[v] {
                let speed = if linked[u][v] { metro } else { walk };
                let d = (pts[v].0 - pts[u].0).hypot(pts[v].1 - pts[u].1) / speed;
                if dist[u] + d < dist[v] {
                    dist[v] = dist[u] + d;
                    prev[v] = u;
                }
            }
        }
    }
    let mut path = Vec::new();
    let mut v = prev[goal];
    while v != start {
        path.push(v + 1);
        v = prev[v];
    }
    path.reverse();
    let mut line = path.len().to_string();
    for s in &path {
        line += &format!(" {}", s);
    }
    println!("{:.10}\n{}", dist[goal], line);
}
