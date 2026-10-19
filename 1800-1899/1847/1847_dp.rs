use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut xs = vec![0f64; n];
    let mut ys = vec![0f64; n];
    for i in 0..n {
        xs[i] = it.next().unwrap() as f64;
        ys[i] = it.next().unwrap() as f64;
    }
    let mut adjacent = vec![Vec::new(); n];
    for _ in 0..n - 1 {
        let a = it.next().unwrap() as usize - 1;
        let b = it.next().unwrap() as usize - 1;
        adjacent[a].push(b);
        adjacent[b].push(a);
    }
    let mut order = vec![0usize];
    let mut parent = vec![usize::MAX; n];
    let mut i = 0;
    while i < order.len() {
        let u = order[i];
        for &v in &adjacent[u] {
            if v != parent[u] {
                parent[v] = u;
                order.push(v);
            }
        }
        i += 1;
    }
    let far = |a: usize, b: usize| (xs[a] - xs[b]).hypot(ys[a] - ys[b]);
    let inf = f64::INFINITY;
    // the walk through a subtree starts at its root and ends at one of its
    // leaves: ends[u] lists them, cost[u] the shortest walk ending at each
    let mut ends: Vec<Vec<usize>> = vec![Vec::new(); n];
    let mut cost: Vec<Vec<f64>> = vec![Vec::new(); n];
    for &u in order.iter().rev() {
        let children: Vec<usize> =
            adjacent[u].iter().copied().filter(|&v| v != parent[u]).collect();
        if children.is_empty() {
            ends[u] = vec![u];
            cost[u] = vec![0.0];
            continue;
        }
        let k = children.len();
        // link[a][b]: leave child a at its best end and fly to child b
        let mut link = vec![vec![inf; k]; k];
        for a in 0..k {
            let (e, c) = (&ends[children[a]], &cost[children[a]]);
            for b in 0..k {
                for j in 0..e.len() {
                    link[a][b] = link[a][b].min(c[j] + far(e[j], children[b]));
                }
            }
        }
        // enter[m][b]: the children in mask m are done and b, in m, came last
        let mut enter = vec![vec![inf; k]; 1 << k];
        for b in 0..k {
            enter[1 << b][b] = far(u, children[b]);
        }
        for m in 1..1usize << k {
            for a in 0..k {
                if enter[m][a] == inf {
                    continue;
                }
                for b in 0..k {
                    if m >> b & 1 == 0 {
                        let step = enter[m][a] + link[a][b];
                        let next = &mut enter[m | 1 << b][b];
                        *next = next.min(step);
                    }
                }
            }
        }
        let full = enter[(1 << k) - 1].clone();
        let (mut mine, mut costs) = (Vec::new(), Vec::new());
        for (b, &v) in children.iter().enumerate() {
            mine.extend_from_slice(&ends[v]);
            costs.extend(cost[v].iter().map(|c| full[b] + c));
            ends[v] = Vec::new();
            cost[v] = Vec::new();
        }
        ends[u] = mine;
        cost[u] = costs;
    }
    let best = ends[0]
        .iter()
        .zip(&cost[0])
        .map(|(&e, &c)| c + far(e, 0))
        .fold(inf, f64::min);
    println!("{:.10}", best);
}
