use std::io::{self, Read};

const SHORTEST: u32 = 3; // a route has at least three stops

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (n, m) = (v[0], v[1]);
    let mut adj = vec![0usize; n];
    let roads = &v[2..];
    for i in 0..m {
        let (a, b) = (roads[2 * i] - 1, roads[2 * i + 1] - 1);
        adj[a] |= 1 << b;
        adj[b] |= 1 << a;
    }

    // paths[mask * n + v]: simple paths from the lowest stop of mask through
    // all of mask, ending at v; a path that can close counts its cycle twice
    let full = (1usize << n) - 1;
    let mut paths = vec![0u64; (full + 1) * n];
    let mut cycles = vec![0u64; full + 1];
    for s in 0..n {
        paths[(1 << s) * n + s] = 1;
    }
    for mask in 1..=full {
        let low = mask & mask.wrapping_neg();
        let start = mask.trailing_zeros();
        let free = !mask & !((low << 1) - 1) & full; // stops that may still join
        let mut closing = 0u64;
        for v in 0..n {
            let count = paths[mask * n + v];
            if count == 0 {
                continue;
            }
            if adj[v] >> start & 1 == 1 {
                closing += count;
            }
            let mut step = adj[v] & free;
            while step != 0 {
                let u = step.trailing_zeros() as usize;
                paths[(mask | 1 << u) * n + u] += count;
                step &= step - 1;
            }
        }
        if mask.count_ones() >= SHORTEST {
            cycles[mask] = closing / 2;
        }
    }

    // the bipartite graph of routes and stops needs as many rows as its
    // largest degree: the longest route or the busiest stop
    let mut best = 0u64;
    let mut through = vec![0u64; n];
    for mask in 1..=full {
        if cycles[mask] == 0 {
            continue;
        }
        best = best.max(mask.count_ones() as u64);
        for (v, t) in through.iter_mut().enumerate() {
            if mask >> v & 1 == 1 {
                *t += cycles[mask];
            }
        }
    }
    best = through.into_iter().fold(best, u64::max);
    println!("{}", best);
}
