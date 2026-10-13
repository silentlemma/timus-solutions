use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};

// weights in grams, times in minutes
const TRUCK: i64 = 3_000_000;
const CUP: i64 = 100;
const ORDER: i64 = 10_000_000;
const DAY: i64 = 24 * 60;

/// Can a truck of this weight reach n within a day?
fn in_time(adj: &[Vec<(usize, i64, i64)>], n: usize, weight: i64) -> bool {
    let mut dist = vec![DAY + 1; n + 1];
    dist[1] = 0;
    let mut heap = BinaryHeap::new();
    heap.push(Reverse((0i64, 1usize)));
    while let Some(Reverse((d, v))) = heap.pop() {
        if v == n {
            return true;
        }
        if d > dist[v] {
            continue;
        }
        for &(u, t, limit) in &adj[v] {
            if limit >= weight && d + t < dist[u] {
                dist[u] = d + t;
                heap.push(Reverse((d + t, u)));
            }
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let (n, m) = (next() as usize, next() as usize);
    if n == 1 {
        println!("{}", ORDER); // the cups are already there
        return;
    }
    let mut adj = vec![Vec::new(); n + 1];
    let mut limits = Vec::new();
    for _ in 0..m {
        let (a, b, t, limit) = (next() as usize, next() as usize, next(), next());
        adj[a].push((b, t, limit));
        adj[b].push((a, t, limit));
        if limit >= TRUCK {
            limits.push(limit);
        }
    }
    // the heaviest possible truck weighs as much as some road allows, and
    // fewer roads are open to a heavier one, so search the road limits
    limits.sort_unstable();
    limits.dedup();
    let mut best = -1;
    let (mut lo, mut hi) = (0i64, limits.len() as i64 - 1);
    while lo <= hi {
        let mid = (lo + hi) / 2;
        if in_time(&adj, n, limits[mid as usize]) {
            best = limits[mid as usize];
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    let answer = if best < 0 {
        0
    } else {
        ORDER.min((best - TRUCK) / CUP)
    };
    println!("{}", answer);
}
